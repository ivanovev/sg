
from collections import OrderedDict as OD

from util.columns import *
from . import ADRF6820_hex, ADRF6820_bin
from ...regs import RegsData, manyregs_cb
from ..callbacks import spi_efc_cmd_cb

def adrf_fmt_cb(val, read=True):
    adrf_fmt_cb.read = read
    if val[0:2] == '0x':
        val = int(val, 16) & 0xFFFF
        val = '%.4X' % val
    return val
    
def adrf_cmd_cb(dev, cmd, val):
    val = int(val, 16)
    cmd = int(cmd[1:], 16)
    if adrf_fmt_cb.read:
        val = 0x1FFFF
    val |= cmd << 17
    val = '0x%.6X' % val
    return 'spi %s %s 0 0' % (dev['spi'], val)

refsel_list = ['x2', 'x1', '/2', '/4', '/8']
vcosel_list = ['4.6G-5.7G', '4.02G-4.6G', '3.5G-4.02G', '2.85G-3.5G']
muxout_list = ['LD', 'VPTAT', 'REFCLK', 'REFCLK/2', 'REFCLK*2', 'REFCLK/8', 'REFCLK/4', 'SCAN']

def Fpfd_src_cb(data, val):
    REFSEL = data.get_value('REFSEL')
    Fpfd = float(data.get_value('REFin'))
    if REFSEL[0] == 'x':
        Fpfd *= int(REFSEL[1])
    else:
        Fpfd /= int(REFSEL[1])
    return '%.2f' % Fpfd

def Fvco_src_cb(data, val):
    Fpfd = float(data.get_value('Fpfd'))
    INT = float(data.get_value('INT'))
    FRAC = float(data.get_value('FRAC'))
    MOD = float(data.get_value('MOD'))
    Fvco = Fpfd*2*(INT + FRAC/MOD)
    return '%.3f' % Fvco

def get_calc_data():
    data = RegsData(sz=16)
    data.add_page('calc0')
    data.add('label1', label='Fvco = 2 x Fpfd x (INT + FRAC/MOD )')
    data.add_page('calc1')
    data.add('Fvco', wdgt='entry', state='readonly', msg='Fvco', src=Fvco_src_cb)
    data.add('Fpfd1', wdgt='entry', state='readonly', msg='Fpfd', src=Fpfd_src_cb)
    data.add('INT', wdgt='spin', value={'min':21, 'max':123, 'step':1}, msg='INT', src=lambda d,v: d.bits_src('R02', 0, 10, v))
    data.add('FRAC', wdgt='spin', value={'min':0, 'max':65535, 'step':1}, msg='FRAC', src=lambda d,v: d.bits_src('R03', 0, 15, v))
    data.add('MOD', wdgt='spin', value={'min':1, 'max':65535, 'step':1}, msg='MOD', src=lambda d,v: d.bits_src('R04', 0, 15, v))
    data.add_page('calc2')
    data.add('label0', label='Fpfd = REFin x REFSEL')
    data.add_page('calc3')
    data.add('Fpfd', wdgt='entry', state='readonly', msg='Fpfd', src=Fpfd_src_cb)
    data.add('REFin', wdgt='entry', state='readonly', msg='REFin', src=lambda d,v: d.dev_src('refin'))
    data.add('REFSEL', wdgt='combo', state='readonly', value=refsel_list, msg='REFSEL', src=lambda d,v: d.list_src('R21', 0, 2, refsel_list, v))
    data.add_page('calc4')
    data.add('MUXOUT', wdgt='combo', state='readonly', value=muxout_list, label='MUXOUT', width=30, src=lambda d,v: d.list_src('R21', 4, 6, muxout_list, v))
    data.add_page('calc5')
    data.add('VCOSEL', wdgt='combo', state='readonly', value=vcosel_list, label='VCOSEL', src=lambda d,v: d.list_src('R22', 0, 2, vcosel_list, v))
    return data

def columns():
    return get_columns([c_ip_addr, c_spi, c_refin])

def get_menu(dev):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev):
    data = get_calc_data()
    data.columns = 5
    data.add_hex_data(ADRF6820_hex.data, cmd_cb=adrf_cmd_cb, fmt_cb=adrf_fmt_cb)
    data.add_bin_data(ADRF6820_bin.data)
    return data

