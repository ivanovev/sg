
from collections import OrderedDict as OD

from util.columns import *
from util import Data, control_cb, util_io_cb
from .callbacks import spi_efc_cmd_cb

gain_list = OD()
gain_list[2] = ['3dB', '6dB']
gain_list[1] = ['6dB', '12dB']
gain_list[0] = ['22dB', '28dB']

def gain_fmt_cb(val, read=True, n=0):
    if read:
        val = int(val, 16)
        return gain_list[n][val >> n & 1]
    else:
        gl = gain_list[n]
        gain_fmt_cb.gain[n] = 0 if val == gl[0] else 1
        return '%d' % gain_fmt_cb.gain[n]
gain_fmt_cb.gain = OD()

def lpf_fmt_cb(val, read=True):
    if read:
        val = int(val, 16)
        val >>= 3
        val &= 0x1F
        return '%d' % val
    else:
        val = int(val)
        val &= 0x1F
        val <<= 3
        val |= 0x80
        val |= gain_fmt_cb.gain[2] << 2
        val |= gain_fmt_cb.gain[1] << 1
        val |= gain_fmt_cb.gain[0] << 0
        return '%.2X' % val

def lpf_cmd_cb(dev, cmd, val=None):
    if val == None:
        val = 'FF'
    return spi_efc_cmd_cb(dev, cmd, val)

def columns():
    return get_columns([c_ip_addr, c_spi])

def get_menu(dev):
    return OD([('Control', control_cb)])

def get_ctrl(dev):
    data = Data(name='LPF', io_cb=util_io_cb)
    data.add('lpf', label='LPF, MHz', wdgt='spin', value={'min':0, 'max':31, 'step':1}, fmt_cb=lpf_fmt_cb, cmd_cb=lpf_cmd_cb, send=True)
    data.add('g3', label='Preamplifier gain', wdgt='radio', value=gain_list[2], fmt_cb=lambda v,r: gain_fmt_cb(v,r,2), send=False)
    data.add('g2', label='Postamplifier gain', wdgt='radio', value=gain_list[1], fmt_cb=lambda v,r: gain_fmt_cb(v,r,1), send=False)
    data.add('g1', label='VGA max gain', wdgt='radio', value=gain_list[0], fmt_cb=lambda v,r: gain_fmt_cb(v,r,0), send=False)

    return data

