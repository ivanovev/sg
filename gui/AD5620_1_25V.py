
from collections import OrderedDict as OD

from util import Data, find_from_table, control_cb, util_io_cb
from .callbacks import spi_efc_cmd_cb
from util.columns import *

def float_fmt_cb(val, read=True, spn_max=2.5):
    _t = {0.0:0x00, spn_max:0xFFF}
    if read:
        val = int(val, 16)
        val >>= 2
        val = find_from_table(_t, val, False)
        return '%.3g' % val
    else:
        val = find_from_table(_t, float(val))
        val = int(val)
        val <<= 2
        return "%.4X" % val

def columns():
    return get_columns([c_ip_addr, c_spi])

def get_menu(dev):
    return OD([('Control', control_cb)])

def get_ctrl(dev):
    spn_max, spn_step = 2.5, 0.05
    if dev['type'] == 'AD5620_2_5V':
        spn_max = 5
    data = Data(name='Voltage', send=True, io_cb=util_io_cb)
    fmt_cb = lambda val, read, spn_max=spn_max: float_fmt_cb(val, read, spn_max)
    cmd_cb = lambda dev, cmd, val: spi_efc_cmd_cb(dev, cmd, val, ncpha='0', cpol='0')
    data.add('out', label='OUT, V', wdgt='spin', value=Data.spn(0, spn_max, spn_step), fmt_cb=fmt_cb, cmd_cb=cmd_cb)
    return data

