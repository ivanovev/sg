
from .DAT31SP import *

def fmt_cb(val, read=True):
    if read:
        pp = val & 1 != 0
        val = int(val, 16)
        val >>= 1
        val = '%d' % val
        if pp:
            val += '.5'
        return val
    else:
        pp = val.find('.5') != -1
        val = int(float(val))
        val <<= 1
        if pp:
            val |= 1
        return "%.2X" % val

def get_ctrl(dev):             
    data = Data(name='atten', send=True, io_cb=util_io_cb)
    cmd_cb = lambda dev, cmd, val: spi_efc_cmd_cb(dev, cmd, val, ncpha='1', cpol='0')
    data.add('atten', label='Attenuation, dB', wdgt='spin', value=Data.spn(0, 31, step=0.5), fmt_cb=fmt_cb, cmd_cb=cmd_cb)
    return data

