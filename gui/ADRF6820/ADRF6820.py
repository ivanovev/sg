
from collections import OrderedDict as OD

from util import Data
from util.columns import *
from . import ADRF6820_hex, ADRF6820_bin
from ...regs import RegsData, manyregs_cb
from ..callbacks import spi_efc_cmd_cb

def adrf_set_freq(Fmix, Fxtal=24):
    # return [r02, r03, r04, r21, r22]
    r02 = 0
    r21 = 0x0009
    r22 = 0x2A00
    if Fmix < 356.25:
        Fmix = 356.25
    if 356.25 <= Fmix and Fmix < 712.5:
        r22 |= 0x10 # div8_en = 1
        Fvco = Fmix*8
    if 712.5 <= Fmix and Fmix < 1425:
        r22 |= 0x08 # div4_en = 1
        Fvco = Fmix*4
    if Fmix > 2850:
        Fmix = 2850
    if 1425 <= Fmix and Fmix <= 2850:
        Fvco = Fmix*2
    if 2850 <= Fvco and Fvco < 3500:
        r22 |= 0b11
    if 3500 <= Fvco and Fvco < 4020:
        r22 |= 0b10
    if 4020 <= Fvco and Fvco < 4600:
        r22 |= 0b01
    if 4060 <= Fvco and Fvco <= 5700:
        r22 |= 0b00
    INT = int(Fvco/(2*24))
    r02 = INT
    MOD = 4800
    r04 = MOD
    FRAC = round(MOD*(float(Fvco)/(2*24) - INT))
    r03 = FRAC
    return [r02, r03, r04, r21, r22]

def adrf_get_freq(reg_io, Fxtal):
    r02 = reg_io('R02')
    r03 = reg_io('R03')
    r04 = reg_io('R04')
    r21 = reg_io('R21')
    r22 = reg_io('R22')
    REFSEL = r21 & 0b11
    Fpfd = float(Fxtal)
    if REFSEL == 0b000:
        Fpfd *= 2
    elif REFSEL == 0b001:
        Fpfd *= 1
    elif REFSEL == 0b010:
        Fpfd /= 2
    elif REFSEL == 0b011:
        Fpfd /= 4
    elif REFSEL == 0b100:
        Fpfd /= 8
    INT = r02 & 0xFFF
    FRAC = float(r03)
    MOD = float(r04)
    Fvco = 2*Fpfd*(INT + FRAC/MOD)
    div = r22 & 0b11
    if div == 1:
        return Fvco/4
    if div == 2:
        return Fvco/8
    return Fvco/2

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

def Fmix_src_cb(data, val):
    Fxtal = float(data.dev_src(c_refin))
    if val != None:
        val = float(val)
        if val < 356.25:
            return
        if val > 2850:
            return
        r02, r03, r04, r21, r22 = adrf_set_freq(float(val), Fxtal)
        data.set_value('R02', '%.4X' % r02, skip_trace_cb=True)
        data.set_value('R03', '%.4X' % r03, skip_trace_cb=True)
        data.set_value('R04', '%.4X' % r04, skip_trace_cb=True)
        data.set_value('R21', '%.4X' % r21, skip_trace_cb=True)
        data.set_value('R22', '%.4X' % r22)
    else:
        Fvco = float(Fvco_src_cb(data, None))
        r22 = int(data.get_value('R22'), 16)
        if r22 & 0x08:
            return '%.2f' % (Fvco/4)
        if r22 & 0x10:
            return '%.2f' % (Fvco/8)
        return '%.2f' % (Fvco/2)

def get_calc_data():
    data = RegsData(sz=16)
    data.add_page('calc0')
    data.add('label0', label='Fmix = Fvco / DIV')
    data.add_page('calc1')
    data.add('Fmix', wdgt='spin', value=Data.spn(356.25, 2850, 0.01), text='1440', msg='Fmix', src=Fmix_src_cb)
    data.add('Fvco1', wdgt='entry', state='readonly', msg='Fvco', src=Fvco_src_cb)
    data.add('DIV', wdgt='combo', state='readonly', text='2', value=['2', '4', '8'], msg='DIV', src=lambda d,v: d.list_src('R22', 3, 4, ['2', '4', '8'], v))
    data.add_page('calc2')
    data.add('label1', label='Fvco = 2 x Fpfd x (INT + FRAC/MOD )')
    data.add_page('calc3')
    data.add('Fvco', wdgt='entry', state='readonly', msg='Fvco', src=Fvco_src_cb)
    data.add('Fpfd1', wdgt='entry', state='readonly', msg='Fpfd', src=Fpfd_src_cb)
    data.add('INT', wdgt='spin', value=Data.spn(21, 123), msg='INT', src=lambda d,v: d.bits_src('R02', 0, 10, v))
    data.add('FRAC', wdgt='spin', value=Data.spn(0, 63535), msg='FRAC', src=lambda d,v: d.bits_src('R03', 0, 15, v))
    data.add('MOD', wdgt='spin', value=Data.spn(1, 63535), msg='MOD', src=lambda d,v: d.bits_src('R04', 0, 15, v))
    data.add_page('calc4')
    data.add('label0', label='Fpfd = REFin x REFSEL')
    data.add_page('calc5')
    data.add('Fpfd', wdgt='entry', state='readonly', msg='Fpfd', src=Fpfd_src_cb)
    data.add('REFin', wdgt='entry', state='readonly', msg='REFin', src=lambda d,v: d.dev_src('refin'))
    data.add('REFSEL', wdgt='combo', state='readonly', value=refsel_list, msg='REFSEL', src=lambda d,v: d.list_src('R21', 0, 2, refsel_list, v))
    data.add_page('calc6')
    data.add('MUXOUT', wdgt='combo', state='readonly', value=muxout_list, label='MUXOUT', width=30, src=lambda d,v: d.list_src('R21', 4, 6, muxout_list, v))
    data.add_page('calc7')
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

