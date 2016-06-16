
from collections import OrderedDict as OD
from copy import deepcopy

from util.columns import *
from util import Data, control_cb, util_io_cb
from .callbacks import gpio_cmd_cb, gpio_list_fmt_cb, spi_efc_cmd_cb, strip0x_fmt_cb

def reverse_bits(val, sz):
    return sum([(1 if val & 1 << i else 0) << (sz -1 - i) for i in range(0, sz)])

def lpf_fmt_cb(val, read=True):
    if read:
        val = int(val, 16) - 0x80
        v1 = reverse_bits(val, 5)
        v1 += 1
        return '%d' % v1
    else:
        val = int(val) - 1
        v1 = reverse_bits(val, 5)
        print(bin(val), bin(v1))
        return strip0x_fmt_cb(hex(0x80 + int(v1)))

def columns():
    return get_columns([c_ip_addr, c_spi, c_gpio])

def tooltips():
    return {c_gpio:'GNSW,OFDS'}

def get_menu(dev):
    return OD([('Control', control_cb)])

def get_ctrl(dev):
    gnsw_list = ['6dB', '12dB']
    gnsw_fmt_cb = lambda val, read=True: gpio_list_fmt_cb(val, read, gnsw_list, 0)
    gnsw_cmd_cb = lambda dev, cmd, val: gpio_cmd_cb(dev, cmd, val, 0)

    ofds_list = ['Enable', 'Disable']
    ofds_fmt_cb = lambda val, read=True: gpio_list_fmt_cb(val, read, ofds_list, 1)
    ofds_cmd_cb = lambda dev, cmd, val: gpio_cmd_cb(dev, cmd, val, 1)

    lpf_cmd_cb = lambda dev, cmd, val: spi_efc_cmd_cb(dev, cmd, val, ncpha='1', cpol='1')

    data = Data(name='LPF', send=True, io_cb=util_io_cb)
    data.add('gnsw', label='Gain switch', wdgt='radio', value=gnsw_list, fmt_cb=gnsw_fmt_cb, cmd_cb=gnsw_cmd_cb)
    data.add('ofds', label='Offset correction loop', wdgt='radio', value=ofds_list, fmt_cb=ofds_fmt_cb, cmd_cb=ofds_cmd_cb)
    data.add('lpf', label='LPF, MHz', wdgt='spin', value={'min':1, 'max':30, 'step':1}, fmt_cb=lpf_fmt_cb, cmd_cb=lpf_cmd_cb)

    return data

