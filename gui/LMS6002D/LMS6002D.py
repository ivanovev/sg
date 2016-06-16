
from collections import OrderedDict as OD
from copy import deepcopy
from itertools import chain
from math import floor
from threading import Thread
from time import sleep
from numpy import arange, linspace

from . import LMS6002D_hex, LMS6002D_bin
from ..callbacks import strip0x_fmt_cb
from ...regs import RegsData, bits_src, get_bits, set_bits, manyregs2_cb

from util.columns import *
from util import proxy, find_key, find_from_table, telnet_io_cb

def reg_io_func(r, v=None, dev=None, data=None):
    ret = None
    if dev != None:
        ret = lms_spi_fmt_cb(proxy.call_telnet(dev, lms_spi_cmd_cb(dev, r, v)))
    if data != None and v != None:
        data.set_value(r, v)
    return ret

def mk_lms_reg_io(dev=None, data=None):
    return lambda r, v=None: reg_io_func(r, v, dev, data)

def reg_upd(reg_io, r, *args, v=None):
    if v == None:
        v = reg_io(r)
    if v == None:
        return
    for i in args:
        n, n1, n2 = i
        v = set_bits(v, n, n1, n2)
    reg_io(r, v)
    return v

def Fvco_src_cb(reg_io, val, n, REFin=None):
    if REFin == None:
        REFin = float(reg_io('REFin'))
    NINT = float(NINT_src_cb(reg_io, None, 'R%s0'%n, 'R%s1'%n))
    NFRAC = float(NFRAC_src_cb(reg_io, None, 'R%s1'%n, 'R%s2'%n, 'R%s3'%n))
    Fvco = REFin*(NINT + NFRAC)
    #print(REFin, NINT, NFRAC, Fvco)
    return '%.3f' % Fvco

def NINT_src_cb(reg_io, val, r0, r1):
    r0 = reg_io(r0)
    nint81 = int(r0, 16) & 0xFF
    r1 = reg_io(r1)
    nint0 = (int(r1, 16) >> 7) & 1
    nint = (nint81 << 1) | nint0
    return '%d' % nint
    
def NFRAC_src_cb(reg_io, val, r1, r2, r3):
    r1 = reg_io(r1)
    nfrac2216 = int(r1, 16) & 0x7F
    r2 = reg_io(r2)
    nfrac158 = int(r2, 16) & 0xFF
    r3 = reg_io(r3)
    nfrac70 = int(r3, 16) & 0xFF
    nfrac = (nfrac2216 << 16) | (nfrac158 << 8) | nfrac70
    return '%.4f' % (nfrac / (1 << 23))

def freqsel_src_cb(reg_io, val, n='1'):
    r = 'R%s5' % n
    s = reg_io(r)
    if val == None:
        n = get_bits(s, 2, 7)
        v = '{0:05b}'.format(n)
        k = find_key(freqsel_list, v)
        return k
    else:
        n = int(freqsel_list[val], 2)
        s = set_bits(s, n, 2, 7)
        reg_io(r, s)

def trxpll_freq(reg_io, freq, n, refin):
    if not freq:
        k = freqsel_src_cb(reg_io, None, n)
        if k == None:
            return
        y = int(freqsel_list[k], 2)
        x = 2**((y & 7) - 3)
        Fvcox = Fvco_src_cb(reg_io, None, n, REFin=refin)
        return '%.2f' % (float(Fvcox)/x)
    f = float(freq)
    rr = ['R%s%d' % (n, i) for i in list(range(0, 4)) + [5]]
    def select_freqsel(f):
        kk = list(freqsel_list.keys())
        k1 = kk[0]
        for k in kk:
            f0, f1 = [1000*float(i) for i in k.split('-')]
            if f0 <= f and f <= f1:
                k1 = k
                break
        if f > f1:
            k1 = kk[-1]
        y = int(freqsel_list[k1], 2)
        return y
    y = select_freqsel(f)
    x = 2**((y & 7) - 3)
    nint = floor(x*f/refin)
    nfrac = floor(2**23*(x*f/refin - nint))
    selout = 0
    if n == '2':
        selout = 3
    vv = deepcopy(rr)
    vv[0] = '%.2X' % ((nint >> 1) & 0xFF)
    vv[1] = '%.2X' % ((((nint & 1) << 7) | (nfrac >> 16)) & 0xFF)
    vv[2] = '%.2X' % ((nfrac >> 8) & 0xFF)
    vv[3] = '%.2X' % (nfrac & 0xFF)
    vv[4] = '%.2X' % ((y << 2) | selout)
    ret = OD(zip(rr, vv))
    if reg_io != None:
        for k in reversed(rr):
            v = ret[k]
            if reg_io(k,v) == None:
                break
    return freq

def freq_src_cb(d, val, n='1'):
    refin = float(d.get_value('REFin'))
    #reg_io = mk_lms_reg_io(d)
    if val == None:
        return trxpll_freq(d.io, None, n, refin)
    rr = trxpll_freq(d.io, val, n, refin)

def select_vcocap(reg_io, n, force_select=True):
    rx9 = 'R%s9' % n
    vx9 = reg_io(rx9)
    vcocap = VCOCAP_src_cb(reg_io, None, rx9)
    def write_vcocap(vcocap):
        v = set_bits(vx9, vcocap, 0, 5)
        reg_io(rx9, v)
        return v
    rxA = 'R%sA' % n
    def vtune():
        v = int(reg_io(rxA), 16)
        cl = 1 if v & 0x40 else 0
        ch = 1 if v & 0x80 else 0
        return cl, ch
    def case_end(il, ih):
        if type(il) == int and type(ih) == int:
            i = int(round((il+ih)/2))
        else:
            i = 31
        #print(il, ih, '=>', i)
        write_vcocap(i)
        return '%d' % i
    def case_1():
        #print('case_1')
        il,ih = None, None
        for i in range(30, -1, -1):
            write_vcocap(i)
            cl, ch = vtune()
            if cl == 0 and ch == 1:
                il = i
                break
        write_vcocap(31)
        for i in range(32, 64):
            write_vcocap(i)
            cl, ch = vtune()
            if cl == 1 and ch == 0:
                ih = i
                break
        return case_end(il, ih)
    def case_2():
        #print('case_2')
        il,ih = None, None
        for i in range(30, -1, -1):
            write_vcocap(i)
            cl, ch = vtune()
            if cl == 0 and ch == 0 and il == None:
                il = i
                continue
            elif cl == 0 and ch == 1:
                ih = i
                break
        return case_end(il, ih)
    def case_3():
        #print('case_3')
        il,ih = None, None
        for i in range(32, 64):
            write_vcocap(i)
            cl, ch = vtune()
            if cl == 0 and ch == 0 and il == None:
                il = i
                continue
            elif cl == 1 and ch == 0:
                ih = i
                break
        return case_end(il, ih)
    write_vcocap(31)
    cl, ch = vtune()
    if cl == 0 and ch == 0 and force_select:
        vcocap = case_1()
    elif cl == 1 and ch == 0:
        vcocap = case_2()
    elif cl == 0 and ch == 1:
        vcocap = case_3()
    print('vcocap:', vcocap)
    return vcocap

def select_vcocap_thread(d, n):
    reg_io = mk_lms_reg_io(d.dev, data)
    rx9 = 'R%s9' % n
    v = select_vcocap(reg_io, n)
    v = '%.2X' % (int(v))
    data.set_value(rx9, v, skip_trace_cb=False)

def select_vcocap_cb(data, n):
    t = Thread(target=select_vcocap_thread, args=(data,n))
    t.start()

def TXVGA1GAIN_src_cb(reg_io, val):
    if val:
        v41 = '%.2X' % (int(val) + 35)
        reg_io('R41', v41)
        return val
    else:
        v41 = reg_io('R41')
        g = int(v41, 16) & 0x1F
        return '%d' % (g - 35)

def TXVGA2GAIN_src_cb(reg_io, val):
    return bits_src(reg_io, 'R45', 3, 7, val, minimum=0, maximum=25)

vga2vcm_bits = list(range(0b1000, 0b1111)) + list(range(0b111, 0b0-1, -1))
vga2vcm_list=['%g' % i for i in linspace(0.62, 1.18, 15)]
vga2vcm_table = OD([(vga2vcm_list[i],vga2vcm_bits[i]) for i in range(0, len(vga2vcm_list))])
def RXVGA2VCM_src_cb(d, val):
    hv = d.get_value('R64')
    if val:
        b = find_from_table(vga2vcm_table, val)
        hv = set_bits(hv, b, 2, 5)
        d.set_value('R64', hv)
    else:
        b = get_bits(hv, 2, 5)
        if b == 0xF:
            return
        v = find_from_table(vga2vcm_table, b, False)
        return v

def VCOCAP_src_cb(reg_io, val, r):
    v = reg_io(r)
    if val == None:
        v = int(v, 16) & 0x3F
        return '%d' % v
    else:
        if val == '': val = '0'
        v = set_bits(v, int(val), 0, 5)
        reg_io(r, v)

def Icp_src_cb(d, val, r, k):
    hv = d.get_value(r)
    if val == None:
        val = int(hv, 16) & 0x1F
        return '%d' % (val*k)
    else:
        hv = set_bits(hv, int(int(val)/k), 0, 4)
        d.set_value(r, hv)

def VCO_output_src_cb(d, val, rx8, rx9):
    v8 = d.get_value(rx8)
    v9 = d.get_value(rx9)
    if val == None:
        v0 = int(v9, 16) >> 7
        v31 = int(v8, 16) >> 5
        v30 = v0 | (v31 << 1)
        v = 1.4 + 0.1*v30
        return '%.1f' % v
    else:
        v30 = int((float(val) - 1.4)/0.1)
        v0 = v30 & 1
        v31 = v30 >> 1
        v8 = set_bits(v8, v31, 5, 7)
        v9 = set_bits(v9, v0, 7, 7)
        d.set_value(rx8, v8)
        d.set_value(rx9, v9)

def RXVGA2GAINAB_src_cb(d, val, n):
    v68 = d.get_value('R68')
    if val == None:
        if n == 'a':
            v = get_bits(v68, 0, 3)
        else:
            v = get_bits(v68, 4, 7)
        return '%d' % (v*3)
    else:
        v = int(int(val)/3)
        if n == 'a':
            v68 = set_bits(v68, v, 0, 3)
        else:
            v68 = set_bits(v68, v, 4, 7)
        d.set_value('R68', v68)
        return val

lnagain_list = ['Bypass', 'mid gain', 'max gain']
def LNAGAIN_src_cb(d, val):
    v75 = d.get_value('R75')
    if val == None:
        v = get_bits(v75, 6, 7)
        if v == 0:
            return
        v -= 1
        return lnagain_list[v]
    else:
        v = lnagain_list.index(val)
        v += 1
        v75 = set_bits(v75, v, 6, 7)
        d.set_value('R75', v75)

rxvga1tia_table = {0:0, 0b111:1, 0b1111:2.1}
def RXVGA1TIA_src_cb(d, val):
    v7b = d.get_value('R7B')
    if val == None:
        v = get_bits(v7b, 4, 7)
        v = find_from_table(rxvga1tia_table, v)
        return '%.1f' % v
    else:
        v = find_from_table(rxvga1tia_table, float(val), False)
        v = round(float(v))
        v7b = set_bits(v7b, int(v), 4, 7)
        d.set_value('R7B', v7b)

def TXRFLBEN_src_cb(val, calc_val_cb, send):
    v46 = calc_val_cb('R46')
    if send == None:
        v = get_bits(v46, 2, 3)
        return '1' if v == 3 else 0
    else:
        v = int(send)
        if v:
            v46 = set_bits(v46, 3, 2, 3)
        else:
            v46 = set_bits(v46, 0, 2, 3)
        calc_val_cb('R46', v46)

txrfpa_list = ['OFF', 'PA1', 'PA2']
trxlpfbw_list = ['14', '10', '7', '6', '5', '4.375', '3.5', '3', '2.75', '2.5', '1.92', '1.5', '1.375', '1.25', '0.875', '0.75']
lnasel_list = ['Disabled', 'LNA1', 'LNA2', 'LNA3']
lna3gain_list = ['+0', '+1', '+2', '+3']
lbpath_list = ['disabled', 'LNA1', 'LNA2', 'LNA3']
rxpllselout_list = ['all pd', 'first', 'second', 'third']

freqsel_list = OD([('0.2325-0.285625','100111'), ('0.285625-0.336875','101111'),
('0.336875-0.405','110111'),('0.405-0.465','111111'),('0.465-0.57125','100110'),
('0.57125-0.67375','101110'),('0.67375-0.81','110110'),('0.81-0.93','111110'),
('0.93-1.1425','100101'),('1.1425-1.3475','101101'),('1.3475-1.62','110101'),
('1.62-1.86','111101'),('1.86-2.285','100100'),('2.285-2.695','101100'),
('2.695-3.24','110100'),('3.24-3.72','111100')])

def lms_spi_cmd_cb(dev, cmd, val=None):
    r = cmd[1:]
    if val == None: val = '00'
    else: r = '%.2X' % (0x80 | int(r, 16))
    return 'spi %s %s%s 1 0' % (dev['spi'], r, val)

def lms_spi_fmt_cb(val, read=True):
    if not read:
        return val
    if not val:
        return
    if type(val) == str:
        val = strip0x_fmt_cb(val, read)
        if len(val) == 4:
            return val[2:]
        return '%.2X' % (int(val, 16) & 0xFF)

def get_calc_data():
    data = RegsData(sz=8)

    data.add_page('calc.toplevel0')
    data.add('REFin', label='REFin, MHz', wdgt='entry', state='readonly', src=lambda d,v: d.dev_src('refin'))
    data.add_page('calc.toplevel1')
    ac = lambda k, name, r, b, msg=None: data.add(k, name=name, wdgt='check', src=lambda d,v: d.bits_src(r, b, b, v), msg=msg)
    ac('toplevelen', 'Toplevel enable', 'R05', 4)
    ac('topleveltxen', 'TX enable', 'R05', 3)
    ac('toplevelrxen', 'RX enable', 'R05', 2)
    ac('toplevelresetn', 'Soft reset', 'R05', 5, '0 - reset state')
    data.add_page('calc.toplevel2')
    ac('pllclkout', 'PLLCLKOUT', 'R09', 6)
    ac('txspiclk', 'TX SPI clk', 'R09', 0)
    ac('rxspiclk', 'RX SPI clk', 'R09', 2)
    ac('rxoutsw', 'RXOUTSW', 'R09', 7, '1 - switch closed, RXVGA2 should be powered off first')

    spn = lambda v1,v2,v3=1: {'min':v1, 'max':v2, 'step':v3}
    data.add_page('calc.txpll0')
    ac('txpllen', 'TXPLL enable', 'R14', 3)
    data.add_page('calc.txpll1')
    data.add('txfreq', label='TX frequency, MHz', wdgt='spin', width=8, value=spn(232.5,3720,0.01), src=lambda d,v: freq_src_cb(d,v,'1'))
    data.add_page('calc.txpll2')
    data.add('freqsel1', label='TX frequency range, GHz', wdgt='entry', state='readonly', value=freqsel_list, src=lambda d,v: freqsel_src_cb(d.io,v,'1'))
    data.add_page('calc.txpll3')
    data.add('Fvco', label='TX Fvco [MHz] = REFin [MHz] x [NINT + NFRAC]')
    data.add_page('calc.txpll4')
    data.add('Fvco1', wdgt='entry', state='readonly', src=lambda d,v: Fvco_src_cb(d.io,v,'1'), msg='Ftxvco')
    data.add('REFin1', wdgt='entry', state='readonly', src=lambda d,v: d.dev_src('refin'), msg='REFin')
    data.add('NINT1', wdgt='entry', state='readonly', src=lambda d,v: NINT_src_cb(d.io,v, 'R10', 'R11'), msg='NINT TX')
    data.add('NFRAC1', wdgt='entry', state='readonly', src=lambda d,v: NFRAC_src_cb(d.io,v, 'R11', 'R12', 'R13'), msg='NFRAC TX')
    data.add_page('calc.txpll5')
    data.add('vcocap1', label='TX VCOCAP', wdgt='spin', width=3, value=spn(0,63), src=lambda d,v: VCOCAP_src_cb(d.io,v,'R19'))
    data.add('vcocap1_btn', wdgt='button', text='Select', click_cb=lambda d=data: select_vcocap_cb(d,'1'), msg='Select VCOCAP')
    data.add_page('calc.txpll6')
    data.add('txvcoout',label='VCO output, V',wdgt='spin',width=5,value=spn(1.4,2.6,0.1),src=lambda d,v: VCO_output_src_cb(d,v,'R18','R19'))
    data.add('txicp',label='CP current, uA',wdgt='spin',width=5,value=spn(0,2400,100),src=lambda d,v: Icp_src_cb(d,v,'R16',100))
    data.add_page('calc.txpll7')
    data.add('txicpup', label='CP up offset, uA', wdgt='spin', width=5, value=spn(0,240,10), src=lambda d,v:Icp_src_cb(d,v,'R17', 10))
    data.add('txicpdn', label='CP down offset, uA', wdgt='spin', width=5, value=spn(0, 240, 10), src=lambda d,v: Icp_src_cb(d,v,'R18', 10))

    data.add_page('calc.rxpll0')
    ac('rxpllen', 'RXPLL enable', 'R24', 3)
    data.add_page('calc.rxpll1')
    data.add('rxfreq', label='RX frequency, MHz', wdgt='spin', width=8, value=spn(232.5,3720,0.01), src=lambda d,v: freq_src_cb(d,v,'2'))
    data.add_page('calc.rxpll2')
    data.add('freqsel2', label='RX frequency range, GHz', wdgt='entry', state='readonly', value=freqsel_list, src=lambda d,v: freqsel_src_cb(d.io,v,'2'))
    data.add_page('calc.rxpll3')
    data.add('rxselout', label='RXPLL SELOUT', wdgt='combo', state='readonly', value=rxpllselout_list, src=lambda d,v: d.list_src('R25',0,1,rxpllselout_list,v), msg='(!) set to third')
    data.add_page('calc.rxpll4')
    data.add('Fvco', label='RX Fvco [MHz] = REFin [MHz] x [NINT + NFRAC]')
    data.add_page('calc.rxpll5')
    data.add('Fvco2', wdgt='entry', state='readonly', src=lambda d,v: Fvco_src_cb(d.io,v,'2'), msg='Frxvco')
    data.add('REFin', wdgt='entry', state='readonly', src=lambda d,v: d.dev_src('refin'), msg='REFin')
    data.add('NINT2', wdgt='entry', state='readonly', src=lambda d,v: NINT_src_cb(d.io,v, 'R20', 'R21'), msg='NINT RX')
    data.add('NFRAC2', wdgt='entry', state='readonly', src=lambda d,v: NFRAC_src_cb(d.io,v, 'R21', 'R22', 'R23'), msg='NFRAC RX')
    data.add_page('calc.rxpll6')
    data.add('vcocap2', label='RX VCOCAP', wdgt='spin', width=3, value=spn(0,63), src=lambda d,v: VCOCAP_src_cb(d.io,v,'R29'))
    data.add('vcocap2_btn', wdgt='button', text='Select', click_cb=lambda d=data: select_vcocap_cb(d,'2'), msg='Select VCOCAP')
    data.add_page('calc.rxpll7')
    data.add('rxvcoout', label='VCO output, V', wdgt='spin', width=5, value=spn(1.4,2.6,0.1), src=lambda d,v: VCO_output_src_cb(d,v,'R28','R29'))
    data.add('rxicp', label='CP current, uA', wdgt='spin', width=5, value=spn(0,2400,100), src=lambda d,v: Icp_src_cb(d,v,'R26',100))
    data.add_page('calc.rxpll8')
    data.add('rxicpup', label='CP up offset, uA', wdgt='spin', width=5, value=spn(0,240,10), src=lambda d,v: Icp_src_cb(d,v,'R27',10))
    data.add('rxicpdn', label='CP down offset, uA', wdgt='spin', width=5, value=spn(0,240,10), src=lambda d,v: Icp_src_cb(d,v,'R28',10))

    data.add_page('calc.txlpf0')
    ac('txlpfen', 'TXLPF enable', 'R34', 1)
    ac('txlpfbyp', 'Bypass', 'R35', 6)
    data.add_page('calc.txlpf1')
    data.add('txlpfbw',label='TXLPF BW, MHz',wdgt='combo',state='readonly',value=trxlpfbw_list,src=lambda d,v: d.list_src('R34',2,5,trxlpfbw_list,v),msg='R34: BWC_LPF')

    data.add_page('calc.txrf0')
    ac('txrfen', 'TXRF enable', 'R40', 1)
    data.add('txrfpa', label='PA', wdgt='combo', state='readonly', value=txrfpa_list, src=lambda d,v: d.list_src('R44',3,4,txrfpa_list,v))
    data.add_page('calc.txrf1')
    data.add('txvga1gain', label='TXVGA1 gain', wdgt='spin', width=3, value=spn(-35, -4), src=lambda d,v: TXVGA1GAIN_src_cb(d.io,v))
    data.add('txvga2gain', label='TXVGA2 gain', wdgt='spin', width=3, value=spn(0, 25), src=lambda d,v: TXVGA2GAIN_src_cb(d.io,v))

    data.add_page('calc.rxlpfdacadc0')
    ac('dacadcen', 'DAC ADC enable', 'R57',7)
    data.add_page('calc.rxlpfdacadc1')
    ac('rxlpfen', 'RXLPF enable', 'R54', 1)
    ac('rxlpfbyp', 'Bypass', 'R55', 6)
    data.add('rxlpfbw',label='RXLPF BW, MHz',wdgt='combo',state='readonly',value=trxlpfbw_list,src=lambda d,v: d.list_src('R54',2,5,trxlpfbw_list,v),msg='R54: BWC_LPF')
    data.add_page('calc.rxlpfdacadc2')
    iq_list=['I,Q','Q,I']
    data.add('txinterleave',label='TX interleave mode',wdgt='combo',state='readonly',value=iq_list,src=lambda d,v: d.list_src('R5A',3,3,iq_list,v),msg='R5A: MISC_CTRL[5]')
    data.add('rxinterleave',label='RX interleave mode',wdgt='combo',state='readonly',value=iq_list,src=lambda d,v: d.list_src('R5A',6,6,iq_list,v),msg='R5A: MISC_CTRL[8]')
    data.add_page('calc.rxlpfdacadc3')
    ac('rxadcbuf', 'ADC buffer disable', 'R59', 0, '1 - disable;0 - enable')
    cmadj_list=['875mV','960mV','700mV','790mV']
    data.add('rxcmadj',label='Common mode adjust',wdgt='combo',state='readonly',value=cmadj_list,src=lambda d,v: d.list_src('R59',3,4,cmadj_list,v),msg='R59: RX_CTRL2[5:4]')
    gainadj_list=['1.50V','1.75V','1.00V','1.25V']
    data.add('rxgainadj',label='Reference gain adjust',wdgt='combo',state='readonly',value=gainadj_list,src=lambda d,v: d.list_src('R59',5,6,gainadj_list,v),msg='R59: RX_CTRL2[7:6]')
    data.add_page('calc.rxlpfdacadc4')
    adc_phase_list=['rising','falling']
    data.add('rxadcphase',label='ADC sampling phase',wdgt='combo',state='readonly',value=adc_phase_list,src=lambda d,v: d.list_src('R5A',2,2,adc_phase_list,v),msg='R5A: RX_CTRL3[7]')
    adc_clkadj_list=['nominal','+450ps','+150ps','+300ps']
    data.add('rxadcclkadj',label='ADC clock adjust',wdgt='combo',state='readonly',value=adc_clkadj_list,src=lambda d,v: d.list_src('R5A',0,1,adc_clkadj_list,v),msg='R5A: RX_CTRL3[1:0]')

    data.add_page('calc.rxvga20')
    ac('rxvga2en', 'Enable RXVGA2', 'R64',1)
    data.add_page('calc.rxvga21')
    data.add('rxvga2gain', label='RXVGA2 gain', wdgt='spin', width=3, value=spn(0, 30, 3), src=lambda d,v: d.bits_src('R65',0,4,v,coef=3,maximum=30), msg='R65: RXVGA2GAIN')
    data.add_page('calc.rxvga22')
    data.add('rxvga2vcm',label='RXVGA2 output common mode voltage',wdgt='combo',state='readonly',text='0.9',value=vga2vcm_list,src=RXVGA2VCM_src_cb,msg='R64: VCM[3:0]')

    data.add_page('calc.rxfe0')
    data.add('lnasel',label='Active LNA (must be LNA3)',wdgt='combo',state='readonly',value=lnasel_list,src=lambda d,v: d.list_src('R75',4,5,lnasel_list,v),msg='R75: LNASEL_RXFE')
    data.add('biaslna', label='LNA', wdgt='spin', value=spn(0,15),width=3,src=lambda d,v: d.bits_src('R7A', 0, 3, v), msg='R7A: ICT_LNA_RXFE')
    data.add('lna3gain',label='LNA3 gain', wdgt='combo', state='readonly', value=lna3gain_list, src=lambda d,v: d.list_src('R7C', 0, 1, lna3gain_list, v),msg='R7C: G_FINE_LNA3_RXFE')
    data.add_page('calc.rxfe1')
    data.add('lnagain',label='LNA gain mode',wdgt='combo',state='readonly',value=lnagain_list,src=LNAGAIN_src_cb, msg='R75: G_LNA_RXFE')
    in1sel_list=['PADS', 'LNA']
    data.add('in1sel',label='Input to the mixer',wdgt='combo',state='readonly',value=in1sel_list,src=lambda d,v: d.list_src('R71',7,7,in1sel_list,v), msg='R71: IN1SEL_MIX_RXFE')
    data.add_page('calc.rxfe2')
    data.add('biasmix', label='Bias current: mixer', wdgt='spin', width=3, value=spn(0,15), src=lambda d,v: d.bits_src('R7A', 4, 7, v), msg='R7A: ICT_MIX_RXFE')
    #data.add_page('calc.rxfe3')
    #data.add('lnaloadext', label='LNA load resistor: external', wdgt='spin', width=3, value=spn(0, 63), src=lambda d,v: d.bits_src('R78', 0, 5, v), msg='R78: RDLEXT_LNA_RXFE')
    #data.add('lnaloadint', label='internal', wdgt='spin', width=3, value=spn(0, 63), src=lambda d,v: d.bits_src('R79', 0, 5, v), msg='R79: RDLINT_LNA_RXFE')
    data.add_page('calc.rxfe4')
    data.add('vga1gain',label='VGA1: gain',wdgt='spin',width=4, value=spn(0, 127), src=lambda d,v: d.bits_src('R76', 0, 6, v), msg='R76: RFB_TIA_RXFE')
    data.add('vga1bw',label='bw',wdgt='spin',width=3,value=spn(0, 127),text='0',src=lambda d,v: d.bits_src('R77', 0, 6, v), msg='R77: CFB_TIA_RXFE')
    data.add('vga1tia',label='tia',wdgt='combo',width=3,state='readonly',value=['%.1f'%find_from_table(rxvga1tia_table,i) for i in range(0,0x10)], src=RXVGA1TIA_src_cb, msg='R7B: ICT_TIA_RXFE')
    return data

def reset_fpga_cb(regs):
    regs.cmdio(telnet_io_cb(regs.data.dev, 'de0_reset'))

def reset_rf_cb(regs):
    regs.cmdio(telnet_io_cb(regs.data.dev, 'lms_reset'))

def rf_mode(reg_io, mode):
    if mode == 'off':
        reg_upd(reg_io, 'R05', (0, 2, 3))
        reg_upd(reg_io, 'R09', (0, 0, 0), (0, 2, 2))
    elif mode == 'tx':
        reg_upd(reg_io, 'R05', (0, 2, 2), (1, 3, 3))
        reg_upd(reg_io, 'R09', (0, 2, 2), (1, 0, 0))
        reg_upd(reg_io, 'R5A', (1, 4, 4))
    elif mode == 'rx':
        reg_upd(reg_io, 'R05', (0, 3, 3), (1, 2, 2))
        reg_upd(reg_io, 'R09', (0, 0, 0), (1, 2, 2))
        reg_upd(reg_io, 'R75', (3, 4, 5))
        reg_upd(reg_io, 'R64', (0b1010, 2, 5)) # RXVGA2 common mode
        reg_upd(reg_io, 'R59', (0b10, 3, 4)) # ADC common mode
    elif mode == None:
        v05 = reg_io('R05')
        v09 = reg_io('R09')
        txrx = get_bits(v05, 2, 3)
        tx = txrx & 2
        rx = txrx & 1
        spi = get_bits(v09, 0, 2)
        txspi = spi & 1
        rxspi = spi & 4
        if tx and txspi:
            return 'tx'
        elif rx and rxspi:
            return 'rx'
        elif tx == rx and txspi == rxspi:
            if tx == 0 and txspi == 0:
                return 'off'
    return mode

def mode_cb(regs, mode):
    reg_io = mk_lms_reg_io(regs.data.dev, data)
    rf_mode(reg_io, mode)
    regs.upd_cb()

def dc_calibrate(reg_io, n, addr, acceptable=3):
    rx1 = 'R%s1' % n
    rx3 = 'R%s3' % n
    vx3 = reg_upd(reg_io, rx3, (addr, 0, 2))
    try_cnt = 0
    reg_upd(reg_io, rx3, (1, 5, 5), v=vx3)
    reg_upd(reg_io, rx3, (0, 5, 5), v=vx3)
    ret = False
    for i in range(0, acceptable):
        sleep(.001)
        vx1 = reg_io(rx1)
        dc_clbr_done = get_bits(vx1, 1, 1)
        if dc_clbr_done == 1:
            continue
        dc_lock = get_bits(vx1, 1, 1)
        if dc_lock in [0, 7]:
            ret = True
            break
    return ret
    
def init_tuningmod(reg_io):
    #reg_io = lambda r, v=None: fmt_cb(proxy.call_telnet(dev, lms_spi_cmd_cb(dev, r, v)))
    #print('LPF tuning/DC offset cancellation of the tuning module')
    def clken5(c=None):
        v09 = reg_io('R09')
        if c == None:
            c = get_bits(v09, 5, 5)
            return c
        else:
            v09 = set_bits(v09, c, 5, 5)
            reg_io('R09', v09)
    r09b5 = clken5()
    clken5(1)
    ret = dc_calibrate(reg_io, '0', 0)
    if ret:
        v = reg_io('R00')
        dccal = get_bits(v, 0, 5)
        #print('algorithm converged, dccal =', dccal)
        for r in ['R35', 'R55']:
            v = reg_io(r)
            v = set_bits(v, dccal, 0, 5)
            reg_io(r, v)
    else:
        print('PANIC: Algorithm does Not Converge!')
    clken5(r09b5)
    return str(ret)

def init_lpfbw(reg_io, refin):
    #reg_io = lambda r, v=None: fmt_cb(proxy.call_telnet(dev, lms_spi_cmd_cb(dev, r, v)))
    #print('LPF tuning/Execute LPF bandwidth tuning procedure')
    mode = rf_mode(reg_io, None)
    txfreq = trxpll_freq(reg_io, None, '1', refin)
    vcocap = VCOCAP_src_cb(reg_io, None, 'R19')
    #print(mode, txfreq)
    # Power Down TxVGA2
    v44 = reg_io('R44')
    reg_upd(reg_io, 'R44', (0, 3, 4), v=v44)
    # Enable TxPLL and set to Produce 320MHz
    rf_mode(reg_io, 'tx')
    trxpll_freq(reg_io, 320, '1', refin)
    select_vcocap(reg_io, '1')
    # Use 40MHz generated From TxPLL
    v06 = reg_upd(reg_io, 'R06', (0, 2, 2))
    # Power Up LPF tuning clock generation block
    v06 = reg_upd(reg_io, 'R06', (0, 3, 3), v=v06)
    # TopSPI::BWC_LPFCAL := RXLPF BWC
    v54 = reg_io('R54')
    bwc_lpf = get_bits(v54, 2, 5)
    v07 = reg_upd(reg_io, 'R07', (bwc_lpf, 0, 3))
    # TopSPI::EN_CAL_LPFCAL := 1 (Enable)
    reg_upd(reg_io, 'R07', (1, 7, 7), v=v07)
    # TopSPI::RST_CAL_LPFCAL := 1 (Rst Active)
    reg_upd(reg_io, 'R06', (1, 0, 0))
    # TopSPI::RST_CAL_LPFCAL := 0 (Rst Inactive)
    reg_upd(reg_io, 'R06', (0, 0, 0))
    # RCCAL := TopSPI::RCCAL_LPFCAL
    r01 = reg_io('R01')
    rccal = get_bits(r01, 5, 7)
    # RxLPFSPI::RCCAL_LPF := RCCAL
    reg_upd(reg_io, 'R56', (rccal, 4, 6))
    # TxLPFSPI::RCCAL_LPF := RCCAL
    reg_upd(reg_io, 'R36', (rccal, 4, 6))
    #print(rccal)
    if mode != None:
        reg_upd(reg_io, 'R06', (1, 2, 2), (1, 3, 3))
        trxpll_freq(reg_io, txfreq, '1', refin)
        VCOCAP_src_cb(reg_io, vcocap, 'R19')
        reg_io('R44', v44)
        rf_mode(reg_io, mode)
    return '%d' % rccal

def trxlpf_dc_offset(reg_io, n):
    #reg_io = lambda r, v=None: fmt_cb(proxy.call_telnet(dev, lms_spi_cmd_cb(dev, r, v)))
    clk_en = reg_io('R09')
    if n == '1':
        r09 = reg_upd(reg_io, 'R09', (1, 1, 1))
        trx = '3'
    elif n == '2':
        r09 = reg_upd(reg_io, 'R09', (1, 3, 3))
        trx = '5'
    vi = dc_calibrate(reg_io, trx, 0)
    vq = dc_calibrate(reg_io, trx, 1)
    reg_io('R09', clk_en)
    return vi, vq

def init_txlpf(reg_io):
    #print('TXLPF/DC offset cancellation of I&Q filters')
    val = trxlpf_dc_offset(reg_io, '1')
    #print(val)
    return str(val)

def init_rxlpf(reg_io):
    #print('RXLPF/DC offset cancellation of I&Q filters')
    val = trxlpf_dc_offset(reg_io, '2')
    #print(val)
    return str(val)

def init_rxvga2(reg_io):
    #print('RXVGA2 init')
    #reg_io = lambda r, v=None: fmt_cb(proxy.call_telnet(dev, lms_spi_cmd_cb(dev, r, v)))
    v = True
    for i in range(0, 5):
        v = dc_calibrate(reg_io, '6', i)
        if not v:
            print('PANIC: Algorithm does Not Converge!')
            break
    return str(v)

def rf_init(reg_io, c, **kwargs):
    if c == '1':
        return init_tuningmod(reg_io)
    if c == '2':
        return init_lpfbw(reg_io, **kwargs)
    if c == '3':
        return init_txlpf(reg_io)
    if c == '4':
        return init_rxlpf(reg_io)
    if c == '5':
        return init_rxvga2(reg_io)

def init_cb(regs, c):
    reg_io = mk_lms_reg_io(regs.data.dev, regs.data)
    refin = regs.data.dev['refin']
    print(refin)
    #reg_io = lambda r, v=None: lms_spi_fmt_cb(proxy.call_telnet(regs.dev, lms_spi_cmd_cb(regs.dev, r, v)))
    rf_init(reg_io, c, refin=float(refin))

def columns():
    return get_columns([c_ip_addr, c_spi, c_refin])

def get_menu(dev):
    return OD([('Registers', manyregs2_cb)])

def get_menu2():
    menu = OD()
    menu_reset = OD()
    menu_reset['FPGA'] = reset_fpga_cb
    menu_reset['RF'] = reset_rf_cb
    menu['Reset'] = menu_reset
    menu_mode = OD()
    menu_mode[('off', 'tx', 'rx')] = lambda regs, mode: Thread(target=mode_cb, args=(regs, mode)).start()
    menu['Mode'] = menu_mode
    menu_vcocap = OD()
    menu_vcocap['TXPLL'] = lambda regs: Thread(target=select_vcocap_thread, args=(regs,'1')).start()
    menu_vcocap['RXPLL'] = lambda regs: Thread(target=select_vcocap_thread, args=(regs,'2')).start()
    menu['VCOCAP'] = menu_vcocap
    menu_init = OD()
    init_menus = ['DC offset cancellation', 'LPF bandwidth', 'TXLPF', 'RXLPF', 'RXVGA2']
    for i in range(0, len(init_menus)):
        menu_init['%d. %s' % (i+1, init_menus[i])] = lambda regs, i=i: Thread(target=init_cb, args=(regs,'%d' % (i+1,))).start()
    #menu_init['separator4'] = None
    #menu_init['TX LO leakage cancellation'] = lambda regs: Thread(target=init_txlo, args=(regs.dev,)).start()
    menu['Init'] = menu_init
    return menu

def get_regs(dev):
    data = get_calc_data()
    hex_data = data.parse_hex_data(LMS6002D_hex.data)
    ag = lambda n,i,j: data.add_group(n, hex_data, 'R%d0' % i, 'R%dF' % i, j, lms_spi_cmd_cb, lms_spi_fmt_cb)
    ag('toplevel', 0, 0)
    ag('txpll', 1, 1)
    ag('rxpll', 2, 2)
    ag('txlpf', 3, 3)
    ag('rxlpfdacadc', 5, 4)
    ag('txrf', 4, 5)
    ag('rxvga2', 6, 6)
    ag('rxfe', 7, 7)
    data.add_bin_data(LMS6002D_bin.data)
    data.columns=5
    data.menu = get_menu2()
    return data

