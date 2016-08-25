
from collections import OrderedDict as OD

from util.columns import *
from util import Data, control_cb, util_io_cb
from .callbacks import spi_efc_cmd_cb

gain_list = OD()
gain_list[2] = ['3dB', '6dB']
gain_list[1] = ['6dB', '12dB']
gain_list[0] = ['22dB', '28dB']

def bit_swap(v):
    ret = 0
    for i in range(0, 5):
        if v & (1 << i):
            ret |= (1 << (4 - i))
    return ret

def gain_fmt_cb(val, read=True, n=0):
    if read:
        val = int(val, 16)
        return gain_list[n][val >> (n+12) & 1]
    else:
        gl = gain_list[n]
        gain_fmt_cb.gain[n] = 0 if val == gl[0] else 1
        return '%d' % gain_fmt_cb.gain[n]
gain_fmt_cb.gain = OD()

def lpf_fmt_cb(val, read=True):
    lpf_fmt_cb.read = read
    if read:
        if val[0:2] == '0x':
            v = int(val, 16)
            v >>= 7
            v &= 0x1F
            v = bit_swap(v)
            val = '%d' % v
        return val
    else:
        print('lpf_fmt_cb')
        v = bit_swap(int(val))
        v |= 0x8000
        v |= gain_fmt_cb.gain[2] << 7
        v |= gain_fmt_cb.gain[1] << 6
        v |= gain_fmt_cb.gain[0] << 5
        print('0x%.4X' % v)
        return '0x%.4X' % v

def lpf_cmd_cb(dev, cmd, val=None):
    val = int(val, 16)
    if lpf_fmt_cb.read:
        val = 0x7FFF
    val = '0x%.4X' % val
    if c_spi in dev:
        return 'spi %s %s 0 0' % (dev[c_spi], val)
    else:
        if lpf_fmt_cb.read:
            return cmd
        else:
            return '%s %s' % (cmd, val)

def columns():
    return get_columns([c_ip_addr, c_spi])

def get_menu(dev):
    return OD([('Control', control_cb)])

def get_lpf_ctrl(data=None, cmd=None):
    if not data:
        data = Data(name='LPF', io_cb=util_io_cb)
    if not cmd:
        cmd = 'lpf'
    data.add(cmd, label='LPF, MHz', wdgt='spin', text='15', value={'min':0, 'max':31, 'step':1}, fmt_cb=lpf_fmt_cb, cmd_cb=lpf_cmd_cb, send=True)
    data.add('g3', label='Preamplifier gain', wdgt='radio', text=gain_list[2][0], value=gain_list[2], fmt_cb=lambda v,r: gain_fmt_cb(v,r,2), send=False)
    data.add('g2', label='Postamplifier gain', wdgt='radio', text=gain_list[1][0], value=gain_list[1], fmt_cb=lambda v,r: gain_fmt_cb(v,r,1), send=False)
    data.add('g1', label='VGA max gain', wdgt='radio', text=gain_list[0][0], value=gain_list[0], fmt_cb=lambda v,r: gain_fmt_cb(v,r,0), send=False)

def get_ctrl(dev):
    data = Data(name='LPF', io_cb=util_io_cb)
    get_lpf_ctrl(data)
    return data

