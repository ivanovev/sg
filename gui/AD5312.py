
from collections import OrderedDict as OD

from util.columns import *
from util import Data, find_from_table, control_cb, util_io_cb
from .callbacks import spi_efc_cmd_cb

def columns():
    return get_columns([c_ip_addr, c_spi, c_refin])

def tooltips():
    return {c_refin:'Reference input voltage, V:\nVref if Vref1 == Vref2 else Vref1,Vref2'}

def get_menu(dev):
    return OD([('Control', control_cb)])

def dac_fmt_cb(val, read=True, ref=2.5, dac=0):
    _t = {0.0:0x00, ref:0x3FF}
    if read:
        val = int(val, 16)
        val >>= 2
        val &= 0x3FF
        val = find_from_table(_t, val, False)
        return '%.2f' % val
    else:
        ret = dac << 15
        ret |= 1 <<  14
        v = find_from_table(_t, float(val))
        ret |= int(v) << 2
        return '%.2X' % ret

def dac_cmd_cb(dev, cmd, val, dac='0'):
    return spi_efc_cmd_cb(dev, 'R' + dac, val, ncpha='0', cpol='0')

def get_ctrl(dev):
    data = Data(name='Voltage', send=True, io_cb=util_io_cb)
    ref = dev[c_refin].split(',')
    ref0 = ref[0]
    if len(ref) == 1:
        data.add('ref', label='Vref, V', wdgt='entry', state='readonly', send=False, text=ref0)
    else:
        data.add('ref0', label='Vref1, V', wdgt='entry', state='readonly', send=False, text=ref0)
    ref0 = float(ref0)
    cmd_cb = lambda dev, cmd, val: dac_cmd_cb(dev, cmd, val, dac='0')
    data.add('dac1', label='DAC1 Uout, V', wdgt='spin', value=Data.spn(0, ref0, .01), cmd_cb=cmd_cb, fmt_cb=lambda val,read=True: dac_fmt_cb(val,read,ref=ref0,dac=0))
    if len(ref) == 2:
        ref1 = ref[1]
        data.add('ref1', label='Vref2, V', wdgt='entry', state='readonly', send=False, text=ref1)
        ref1 = float(ref1)
    else:
        ref1 = ref0
    cmd_cb = lambda dev, cmd, val: dac_cmd_cb(dev, cmd, val, dac='1')
    data.add('dac2', label='DAC2 Uout, V', wdgt='spin', value=Data.spn(0, ref1, .01), cmd_cb=cmd_cb, fmt_cb=lambda val,read=True: dac_fmt_cb(val,read,ref=ref1,dac=1))
    return data

