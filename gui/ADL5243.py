
from collections import OrderedDict as OD

from util.data import Data, find_from_table
from util.mainwnd import control_cb
from util.callbacks import util_io_cb
from .AD7814 import columns
from .callbacks import spi_efc_cmd_cb

def fmt_cb(val, read=True):
    if read:
        assert False
    else:
        _t = {0.0:0x00, +31.5:0x3F}
        val = find_from_table(_t, float(val))
        return "%.2X" % val

def write_cb(ctrl):
    ctrl.write_cb()

def get_menu(dev):
    return OD([('Control', control_cb)])

def get_ctrl(dev):
    data = Data(name='atten', send=True, buttons=OD([('Write', write_cb)]), io_cb=util_io_cb)
    cmd_cb = lambda dev, cmd, val: spi_efc_cmd_cb(dev, cmd, val, ncpha='1', cpol='0')
    data.add('atten', label='Attenuation, dB', wdgt='spin', value=Data.spn(0, 31.5, .5), fmt_cb=fmt_cb, cmd_cb=cmd_cb)
    return data

