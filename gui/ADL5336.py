
from collections import OrderedDict as OD
from .ADF4350 import columns
from ..regs import RegsData, regs_cb
from .callbacks import strip0x_fmt_cb, spi_efc_cmd_cb
from util.columns import *
from math import ceil

hex_data = '''
R0|FEF|
'''

bin_data = '''
R0|0|VGA1 Setpoint
R0|3|VGA2 Setpoint
R0|6|VGA2 Switch
R0|7|VGA1 Maximum Gain
R0|9|VGA2 Maximum Gain
'''

def columns():
    return get_columns([c_ip_addr, c_spi])

def get_menu(dev):
    return OD([('Registers', regs_cb)])

vga_setpoints=['+62.5/−24', '+88/−21', '+125/−18', '+176/−15', '+250/−12', '+353/−9', '+500/−6', '+707/−3']
vga2_input=['IP2A, IM2A', 'IP2B, IM2B']
vga1_gain=['9.5', '12', '14', '15.6']
vga2_gain=['14', '16.9', '19', '20.9']
def get_regs(dev):
    data = RegsData(sz=11)
    data.add_page('calc0')
    data.add('vga1_setpoint', wdgt='combo', state='readonly', label='VGA1 RMS Output, mV rms/dBV', value=vga_setpoints, src=lambda d,v: d.list_src('R0', 0, 2, vga_setpoints, v))
    data.add_page('calc1')
    data.add('vga2_setpoint', wdgt='combo', state='readonly', label='VGA2 RMS Output, mV rms/dBV', value=vga_setpoints, src=lambda d,v: d.list_src('R0', 3, 5, vga_setpoints, v))
    data.add_page('calc3')
    data.add('vga2_input', wdgt='combo', state='readonly', label='VGA2 Input', value=vga2_input, src=lambda d,v: d.list_src('R0', 6, 6, vga2_input, v))
    data.add_page('calc4')
    data.add('vga1_gain', wdgt='combo', state='readonly', label='VGA1 Maximum Gain, dB', value=vga1_gain, src=lambda d,v: d.list_src('R0', 7, 8, vga1_gain, v))
    data.add_page('calc5')
    data.add('vga2_gain', wdgt='combo', state='readonly', label='VGA2 Maximum Gain, dB', value=vga2_gain, src=lambda d,v: d.list_src('R0', 9, 10, vga2_gain, v))

    fmt_cb = lambda val, read: strip0x_fmt_cb(val, read, ceil(data.sz/4))
    data.add_hex_data(hex_data, cmd_cb=spi_efc_cmd_cb, fmt_cb=fmt_cb)
    data.add_bin_data(bin_data)
    return data

