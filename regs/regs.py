#!/usr/bin/env python3

import asyncio
import tkinter as tk
import tkinter.ttk as ttk

from collections import OrderedDict as OD
from math import log

from util.control import Control
from util.tooltip import ToolTip
from util.server import proxy
from util.myio import MyAIO
from util.data import Obj

from .regsdata import RegsData, get_bits, set_bits

import pdb

class Regs(Control):
    def __init__(self, dev, data, parent=None, standalone=True):
        self.standalone = standalone
        Control.__init__(self, dev=dev, data=data, parent=parent, center=True)
        self.fileext = 'txt'
        self.root.resizable(0, 0)
        self.root.protocol('WM_DELETE_WINDOW', self.close_window_cb)
        self.update_bin()
        self.update_calc()
        self.io_start = lambda *args, **kwargs: asyncio.async(self.io.start(*args, **kwargs))

    def init_io(self):
        self.io = MyAIO(self)
        self.io.add(self.regs_cb1, self.ctrl_cb2, self.regs_cb3, proxy.io_cb)

    def regs_cb1(self):
        self.data.select('hex')
        oo = []
        for obj in self.data.iter_cmds2(self.io.read):
            oo.append(obj)
        #oo = list(reversed(sorted(oo, key=lambda o: o.cmdid)))
        for obj in reversed(oo):
            self.io.qo.put(obj)
        return True

    def regs_cb3(self):
        ret = True
        self.data.select('hex')
        for k,v in self.data.cmds.items():
            if not self.hex_data_valid(k):
                self.change_bk_color(k, 'red')
                ret = False
            else:
                self.change_bk_color(k, 'white')
        if not ret:
            return False
        self.update_bin()
        self.update_calc()
        self.ctrl_cb3()

    def init_layout(self):
        if self.standalone:
            self.add_menu_file(file_save=False)
        if self.data['hex']:
            self.data.select('hex')
        self.init_common_layout()
        self.init_custom_layout()

    def init_common_layout(self):
        self.ft = tk.Frame(self.frame)
        self.ft.grid(row=0, column=0, sticky=tk.NSEW)

        self.fcalc = tk.Frame(self.ft)
        self.fcalc.grid(row=0, column=0, sticky=tk.NSEW)
        self.fexp = tk.Frame(self.ft)
        self.fexp.grid(row=1, column=0, sticky=tk.E+tk.S+tk.W)
        self.ft.rowconfigure(0, weight=1)
        self.ft.columnconfigure(0, weight=1)
        self.expand = tk.BooleanVar(value=1)
        expand = ttk.Checkbutton(self.fexp, text='Expand/Collapse', variable=self.expand, command=self.expand_collapse_cb)
        expand.pack(fill=tk.X, expand=1)

        self.fbut = tk.Frame(self.frame)
        self.fbut.grid(row=0, column=1, sticky=tk.N+tk.E)

        self.fb = tk.Frame(self.frame)
        self.fb.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.add_buttons_read_write()

    def init_calc(self, f, prefix1='calc', prefix2=None):
        ncalc = 0
        if self.standalone:
            for k,v in self.data.iterkw(prefix1, prefix2):
                self.add_row(v, f)
                ncalc += 1
        if ncalc == 0:
            self.add_row({'label1':Obj(label='.'.join([self.data.dev['name'], self.data.dev['type']]))}, f)

    def init_custom_layout(self):
        self.init_calc(self.fcalc)

        for k,v in self.data.cmds.items():
            if not self.standalone:
                if 'l' in v:
                    if v.l.get() != '1':
                        continue
            f = tk.Frame(self.fb)
            f.pack(side=tk.LEFT)
            self.make_reg(k, f)
        #self.fb.rowconfigure(1, weight=1)
        self.init_hex()

    def add_buttons_read_write(self):
        read = tk.Button(self.fbut, text='Read', command=self.read_cb)
        read.grid(row=0, column=0, sticky=tk.E+tk.W, padx=5, pady=5)
        write = tk.Button(self.fbut, text='Write', command=self.write_cb)
        write.grid(row=0, column=1, sticky=tk.E+tk.W, padx=5, pady=5)
        if self.standalone:
            self.pb = ttk.Progressbar(self.fbut, orient=tk.HORIZONTAL, maximum=10)
            self.pb.grid(row=1, column=0, columnspan=2, sticky=tk.E+tk.W, padx=5, pady=5)

    def make_reg(self, k, f):
        fhex = tk.Frame(f, borderwidth=2)
        fhex.grid(column=0, row=0, sticky=tk.N+tk.E+tk.W)
        self.data.cmds[k].trace_cb = self.hex_cb
        l, w = self.make_cmdw(fhex, k, self.data.cmds)
        width = 10
        if hasattr(self.data, 'sz'):
            width = int(self.data.sz/4) + 3
        l.grid(column=0, row=0, sticky=tk.NSEW, ipadx=5)
        w.configure(width=width)
        w.grid(column=1, row=0)
        for k1,v1 in self.data[k].items():
            v1.trace_cb = self.bin_cb
        fbin = self.init_frame(f, self.data[k])
        fbin.grid(column=0, row=1, sticky=tk.NSEW)
        
    def add_row(self, row, frame):
        f1 = tk.Frame(frame)
        for k,v in row.items():
            v.trace_cb = self.calc_cb
            l,w = self.make_cmdw(f1, k, row)
            if l != None:
                l.pack(side='left', padx=5)
            if w:
                if v.wdgt in ['entry', 'spin', 'combo']:
                    w.configure(width=(v.width if v.width else 10))
                w.pack(side='left')
        f1.pack(fill=tk.X, anchor=tk.W)

    def init_hex(self):
        #print('init_hex', name)
        cmds = self.data.cmds
        if self.standalone:
            if hasattr(self.data, 'init'):
                l = self.data.init
                kk = list(cmds.keys())
                for k in kk:
                    self.data.set_value(k, l[kk.index(k)], set_send=False)
                self.update_bin()
                self.update_calc()
            '''
            else:
                for k,v in cmds.items():
                    hv = self.get_hex_from_bin(k)
                    self.data.set_value(k, hv, set_send=False)
                self.update_calc()
            '''

    def get_hex_from_bin(self, k):
        s = ''
        for i in range(0, self.data.sz):
            s1 = self.data.get_value('%s.%d' % (k, i))
            s = s1 + s if s1 else '0' + s
        f = '%%.%dX' % (self.data.sz/4)
        return f % int(s, 2)

    def hex_data_valid(self, k=None):
        if k == None:
            for k,v in self.data.cmds.items():
                if not self.hex_data_valid(k):
                    print('hex data invalid', k)
                    return False
            return True
        v = self.data.find_v(k)
        if v.state == 'readonly':
            return True
        if not v.t:
            return True
        hv = v.t.get()
        if not hv:
            return False
        hv = int(hv, 16)
        for i in range(0, self.data.sz):
            bw = self.data.find_v('%s.%d' % (k, i))
            if bw.state == tk.DISABLED and bw.t and bw.text != None:
                if ((hv >> i) & 1) != int(bw.text):
                    return False
        return True

    def bin_cb(self, k, data):
        r,n = k.split('.')
        n = int(n)
        vr = self.get_hex_from_bin(r)
        vb = self.data.get_value(k)
        hv = set_bits(vr, int(vb), n, n)
        self.data.set_value(r, hv)
        self.change_bk_color(r, 'white')
        self.update_calc()

    def hex_cb(self, k, data):
        print('hex_cb', k)
        if not self.hex_data_valid(k):
            self.change_bk_color(k, 'red')
            return
        self.change_bk_color(k, 'white')
        self.update_bin(k)
        self.update_calc()

    def calc_cb(self, k, data):
        cv = self.data.get_value(k)
        if cv == '':
            return
        v = self.data.find_v(k)
        if v.src:
            v.src(self.data, cv)
        self.update_bin()
        self.update_calc()

    def update_bin(self, k=None):
        if not self.hex_data_valid(k):
            return
        if not k:
            self.data.select('hex')
            for k,v in self.data.cmds.items():
                if k in self.data.cmds:
                    self.update_bin(k)
            return
        hv = self.data.get_value(k)
        if hv == '':
            return
        hv = int(self.data.get_value(k), 16)
        for i in range(0, self.data.sz):
            self.data.set_value('%s.%d' % (k, i), '1' if (hv >> i) & 1 else '0')

    def update_calc(self):
        if not self.hex_data_valid():
            return
        prefix1, prefix2 = self.data.calc_prefix12()
        for k,v in reversed(list(self.data.iterkw(prefix1, prefix2))):
            kk = reversed(list(v.keys()))
            for k1 in kk:
                v1 = v[k1]
                if v1.src:
                    self.data.set_value(k1, v1.src(self.data,None))

    def upd_cb(self):
        self.update_bin()
        self.update_calc()

    def change_bk_color(self, k, color):
        v = self.data.find_v(k)
        if not v.state and v.w:
            v.w.configure(background=color)

    def fileopen(self, fname, *args):
        in_file = open(fname, 'rt')
        for in_line in in_file.readlines():
            if not in_line:
                break
            in_line = in_line.strip('\n\r')
            ll = in_line.split()
            if len(ll) != 2:
                print('error: %s' % ll)
                break
            k,v = ll
            self.data.set_value(k, v)
        in_file.close()
        self.update_bin()
        self.update_calc()

    def get_initialfile(self, read=True):
        dev = self.data.dev
        default = dev['type']
        if not read:
            if 'refin' in dev:
                default += '_'  + dev['refin'] + 'MHz'
            mhz = None
            for k,v in self.data.iterkw('calc'):
                for k1,v1 in v.items():
                    if v1.t and v1.wdgt == 'entry' and v1.wdgt == 'readonly':
                        mhz = '%g' % float(v1.t.get())
                        default += '_' + mhz + 'MHz'
                        break
                if mhz: break
        return '%s.%s' % (default, self.fileext)

    def filesave(self, fname):
        out_file = open(fname, 'wt')
        for k,v in self.data['hex'].items():
            if int(v.l.get()):
                out_file.write(' '.join([k, v.t.get()]) + '\n')
        out_file.close()

    def close_window_cb(self, *args):
        self.root.withdraw()
        if hasattr(self, 'parent'):
            if self.parent != None:
                self.parent.update_idletasks()
        self.root.destroy()

    def expand_collapse_cb(self, *args):
        self.root.update_idletasks()
        if self.expand.get():
            self.fb.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
        else:
            self.fb.grid_forget()
        self.frame.pack()

    def read_cb(self, *args):
        self.data.select('hex')
        self.io.read = True
        self.io_start()

