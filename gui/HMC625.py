

from collections import OrderedDict as OD

from util import Data, control_cb, util_io_cb
from .AD7814 import columns
from .callbacks import spi_efc_cmd_cb

def fmt_cb(val, read=True):
    if read:
        val = int(val, 16)
        val >>= 1
        return '%d' % val
    else:
        val = round(2*(float(val) + 13.5))
        return "%.2X" % val

def get_menu(dev):             
    return OD([('Control', control_cb)])
  
def get_ctrl(dev):             
    data = Data(name='atten', send=True, io_cb=util_io_cb)
    cmd_cb = lambda dev, cmd, val: spi_efc_cmd_cb(dev, cmd, val, cpha='0', cpol='0')
    data.add('atten', label='Attenuation, dB', wdgt='spin', text='0', value=Data.spn(-13.5, 18, 0.5), fmt_cb=fmt_cb, cmd_cb=cmd_cb)
    return data

