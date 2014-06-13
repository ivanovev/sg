
import tkinter as tk
from collections import OrderedDict as OD

from math import log
from copy import deepcopy
from itertools import chain

from util import Data, Obj, util_io_cb
import sys
import pdb

def find_reg_bit(reg, reg_len, bit_num):
    name, value, grayed, msg = '', None, False, None
    entry_num = 0
    for i in range(0, reg_len):
        if i in reg:
            name, value, grayed, msg = '', None, False, ''
            bb = reg[i]
            if 'name' in bb:
                name = bb['name']
            if 'value' in bb:
                value = bb['value']
                entry_num = i
            if 'grayed' in bb:
                grayed = bb['grayed']
        if i == bit_num:
            if 'msg' in bb:
                msg = bb['msg']
            break
    if value != None:
        value = 1 & (value >> (bit_num - entry_num))
    return name, value, grayed, msg

def get_bits(val, N1, N2):
    if type(val) == str:
        val = int(val, 16)
    FF = (1 << (N2 - N1 + 1)) - 1
    return (val >> N1) & FF

def set_bits(r, v, N1, N2):
    FF = (1 << (N2 - N1 + 1)) - 1
    l = len(r)
    r = int(r, 16)
    v = v & FF
    r = r & ~(FF << N1)
    r = r | (v << N1)
    f = '%%.%dX' % l
    return f % r

def bits_src(reg_io, k, n1, n2, val=None, coef=1, minimum=None, maximum=None):
    hv = reg_io(k)
    if val:
        n = int(int(val)/coef)
        hv = set_bits(hv, n, n1, n2)
        reg_io(k, hv)
        return val
    else:
        n = get_bits(hv, n1, n2)
        n *= coef
        if minimum != None:
            n = minimum if n < minimum else n
        if maximum != None:
            n = maximum if n > maximum else n
        return '%d' % n

def list_src(reg_io, r, n1, n2, l, val=None):
    hv = reg_io(r)
    if val:
        if val not in l:
            return
        v = l.index(val)
        hv = set_bits(hv, v, n1, n2)
        reg_io(r, hv)
        return val
    else:
        v = get_bits(hv, n1, n2)
        if v < len(l):
            return l[v]
        else:
            return l[0]

class RegsData(Data):
    def __init__(self, sz=32, io_cb=util_io_cb):
        Data.__init__(self, io_cb=io_cb)
        self.cur = 0
        self.sz = sz

    def add_bit(self, i, name, grayed=None, msg=None, v0=None):
        k = self.cmds.name
        obj = self.add('%s.%d' % (k, i), name=name, grayed=grayed)
        if v0 != None:
            v0 = int(v0)
            obj.v0 = v0
            obj.text = v0 & 1
        if msg: obj.msg1 = msg
        obj.msg = 'b%d: %s' % (i, msg) if msg else 'b%d' % i
        obj.wdgt = 'check'
        if grayed:
            obj.state = tk.DISABLED
        return obj

    def add_bits(self, i, name, grayed=None, msg=None, value=None, finalize=False):
        v0 = value
        if not len(self.cmds):
            o = self.add_bit(i, name, grayed, msg, v0)
        else:
            k,v = list(self.cmds.items())[-1]
            l = len(self.cmds)
            for j in range(l, i):
                v10 = None if v.v0 == None else v.v0 >> (j - l + 1) & 1
                v1 = self.add_bit(j, v.name, v.grayed, v.msg1, v0=v10)
            o = self.add_bit(i, name, grayed, msg, v0)
        if finalize:
            for j in range(i+1, self.sz):
                v10 = None if o.v0 == None else o.v0 >> (j - l + 1) & 1
                v1 = self.add_bit(j, name, grayed, msg, v0=v10)

    def bits_src(self, k, n1, n2, val=None, coef=1, minimum=None, maximum=None):
        return bits_src(self.io, k, n1, n2, val, coef, minimum, maximum)

    def list_src(self, r, n1, n2, l, val=None):
        return list_src(self.io, r, n1, n2, l, val)

    def dev_src(self, k):
        if k in self.dev:
            return self.dev[k]
        return 0

    def log_src(self, k, n1, n2, b=None):
        hv = self.get_value(k)
        if b == None:
            n = get_bits(hv, n1, n2)
            return '%d' % (2**n)
        else:
            n = int(b)
            n = int(log(n, 2))
            hv = set_bits(hv, n, n1, n2)
            self.set_value(k, hv)

    def parse_hex_data(self, s):
        d = {}
        rr = set()
        a = s.split('\n')
        for i in a:
            j = i.split('|')
            if len(j) < 3:
                continue
            rr.add(j[0])
            d[j[0]] = (j[1], j[2])
        kk = sorted(list(rr), key=lambda r: int(r[1:], 16))
        return OD([(i, d[i]) for i in kk])

    def add_hex_data(self, s, cmd_cb=None, fmt_cb=None):
        hd = self.parse_hex_data(s)
        self.add_page('hex')
        for k,v in hd.items():
            text = v[0]
            if not text: text = '0' * int(self.sz/4)
            v1 = self.add(k, label=k, wdgt='entry', text=text, msg=v[1], send=True, cmd_cb=cmd_cb, fmt_cb=fmt_cb)
                
    def add_bin_data(self, s):
        d = {}
        rr = set()
        a = s.split('\n')
        for i in a:
            j = i.split('|')
            if len(j) < 3:
                continue
            rr.add(j[0])
            k = '%s.%d' % (j[0], int(j[1]))
            if k in d:
                print('%s ???' % k)
                continue
            d[k] = Obj(name=j[2])
            if j[3] != '' if len(j) >= 4 else False:
                gg = j[3].split(':')
                d[k].grayed = bool(int(gg[0]))
                if len(gg) > 1:
                    d[k].value = int(gg[1])
            if j[4] != '' if len(j) >= 5 else False:
                d[k].msg = j[4]
        kk = sorted(list(rr), key=lambda r: int(r[1:], 16))
        for r in kk:
            rk = list(filter(lambda x: x.find(r + '.') == 0, d.keys()))
            f = lambda k: int(k.split('.')[-1])
            rk = sorted(rk, key=f)
            self.add_page(r)
            for j in rk:
                self.add_bits(f(j), finalize=(j == rk[-1]), **d[j])
        return kk

    def add_group(self, name, hex_data, start, end, pos, cmd_cb=None, fmt_cb=None):
        if not hasattr(self, 'groups'):
            self.groups = []
        self.groups.append(name)
        l = list(hex_data.keys())
        sl = RegsData.sublist(l, start, end)
        self.add_page(name, pos=pos)
        for i in sl:
            text = hex_data[i][0]
            msg = hex_data[i][1] if hex_data[i][1] else None
            self.add(i, label=i, wdgt='entry', text=text, msg=msg, send=True, cmd_cb=cmd_cb, fmt_cb=fmt_cb)

    def calc_prefix12(self):
        if hasattr(self, 'groups'):
            return 'calc', self.cmds.name
        else:
            return 'calc', None

    def set_value(self, k, s, set_send=True, skip_trace_cb=True):
        return Data.set_value(self, k, s, set_send, skip_trace_cb)

    def io(self, r, val=None):
        if val == None:
            return self.get_value(r)
        else:
            self.set_value(r, val)
            return val

    def src_upd(self, c):
        v = self.find_v(c)
        if not v.src if v else True:
            print('src_upd: %s.src not found' % c)
            return
        v1 = v.src(self, None)
        self.set_value(c, v1)

    def init_groups(self, groups, cmd_cb=None, fmt_cb=None):
        self.groups = groups
        self.all_regs = list(chain(*groups.values()))

        for k,v in groups.items():
            self.add_page(k)
            for r in v:
                self.add(r, label=r, wdgt='entry', send=True, cmd_cb=cmd_cb, fmt_cb=fmt_cb)

    @staticmethod
    def sublist(l, start, end):
        try:
            i1 = l.index(start)
        except:
            i1 = 0
        try:
            i2 = l.index(end)
        except:
            i2 = len(l)
        return l[i1:i2+1]

