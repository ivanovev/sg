
from collections import OrderedDict as OD
from util.columns import *
from util import Data, find_from_table, util_io_cb, monitor_cb

def cmd_cb(dev, cmd, val=None):
    return 'spi %s 0000' % dev['spi']

def fmt_cb(val, read=True):
    if not read:
        return
    t = int(val, 16)
    t = t >> 5
    if t & (1 << 10):
        _t = {0b1000000000:-128., 0b1111111111:-0.25}
        return find_from_table(_t, t)
    else:
        _t = {0b0:0., 0b0111111100:127.}
    return find_from_table(_t, t)

def get_menu(dev):
    return OD([('Monitor', monitor_cb)])

def columns():
    return get_columns([c_ip_addr, c_spi])

def get_mntr(dev):
    data = Data('mntr', send=True, io_cb=util_io_cb)
    data.add('temp', wdgt='entry', msg='Temperature', fmt_cb=fmt_cb, cmd_cb=cmd_cb)
    return data

