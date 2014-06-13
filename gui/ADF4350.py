
from collections import OrderedDict as OD
from ..regs import RegsData, regs_cb
from .callbacks import spi_efc_cmd_cb, strip0x_fmt_cb
from util.columns import *

def Fout_src_cb(data, val):
    Fvco = float(data.get_value('Fvco1'))
    DIV = float(data.get_value('DIV'))
    return '%.3f' % (Fvco/DIV)

def Fvco_src_cb(data, val):
    Fpfd = float(data.get_value('Fpfd1'))
    INT = float(data.get_value('INT'))
    FRAC = float(data.get_value('FRAC'))
    MOD = float(data.get_value('MOD'))
    Fvco = float(Fpfd)*(INT + float(FRAC)/MOD)
    return '%.3f' % Fvco

def Fpfd_src_cb(data, val):
    REFin = float(data.get_value('REFin'))
    D = float(data.get_value('D'))
    R = float(data.get_value('R'))
    T = float(data.get_value('T'))
    Fpfd = REFin*((1.+D)/(R*(1.+T)))
    return '%.3f' % Fpfd

data = RegsData()
data.add_page('calc0')
data.add('label1', label='Fout = Fvco/DIV')
data.add_page('calc1')
data.add('Fout', wdgt='entry', src=Fout_src_cb, state='readonly', msg='Fout')
data.add('Fvco1', wdgt='entry', src=Fvco_src_cb, state='readonly', msg='Fvco')
data.add('DIV', wdgt='combo', state='readonly', value=['1','2','4','8','16'], src=lambda d,v: d.log_src('R4', 20, 22, v), msg='DIV')
data.add_page('calc2')
data.add('label2', label='Fvco = Fpfd x (INT + FRAC/MOD)')
data.add_page('calc3')
data.add('Fvco', wdgt='entry', src=Fvco_src_cb, state='readonly', msg='Fvco')
data.add('Fpfd1', wdgt='entry', src=Fpfd_src_cb, state='readonly', msg='Fpfd')
data.add('INT', wdgt='spin', value={'min':23, 'max':65535, 'step':1}, src=lambda d,v: d.bits_src('R0', 15, 30, v), msg='INT')
data.add('FRAC', wdgt='spin', value={'min':0, 'max':4094, 'step':1}, src=lambda d,v: d.bits_src('R0', 3, 14, v), msg='FRAC')
data.add('MOD', wdgt='spin', value={'min':2, 'max':4095, 'step':1}, src=lambda d,v: d.bits_src('R1', 3, 14, v), msg='MOD')
data.add_page('calc4')
data.add('label3', label='Fpfd = REFin x [(1 + D)/(R x (1 + T))]')
data.add_page('calc5')
data.add('Fpfd', wdgt='entry', src=Fpfd_src_cb, state='readonly', msg='Fpfd')
data.add('REFin', wdgt='entry', src=lambda d,v: d.dev_src('refin'), state='readonly', msg='REFin')
data.add('D', wdgt='spin', value={'min':0, 'max':1, 'step':1}, src=lambda d,v: d.bits_src('R2', 25, 25, v), msg='D')
data.add('R', wdgt='spin', value={'min':1, 'max':1023, 'step':1}, src=lambda d,v: d.bits_src('R2', 14, 23, v), msg='R')
data.add('T', wdgt='spin', value={'min':0, 'max':1, 'step':1}, src=lambda d,v: d.bits_src('R2', 24, 24, v), msg='T')
data.add_page('calc6')
muxout_list = ['THREE-STATE OUTPUT','DVdd','DGnd','R DIVIDER OUTPUT','N DIVIDER OUTPUT','ANALOG LOCK DETECT','DIGITAL LOCK DETECT','RESERVED']
data.add('muxout', wdgt='combo', label='MUXOUT', state='readonly', msg='MUXOUT', value=muxout_list, src=lambda d,v: d.list_src('R2',26,28,muxout_list,v))
ld_list = ['LOW','DIGITAL LOCK DETECT','LOW2','HIGH']
data.add('ld', wdgt='combo', label='LD PIN MODE', state='readonly', msg='LD PIN MODE', value=ld_list, src=lambda d,v: d.list_src('R5',22,23,ld_list,v))

hex_data = '''
R0|00480000|
R1|00008FA1|
R2|78004802|
R3|00057FFB|
R4|00AC903C|
R5|00580005|
'''

bin_data = '''
R0|0|Control bits|1:0|
R0|3|FRAC||
R0|15|INT||
R0|31|Reserved|1|
R1|0|Control bits|1:1|
R1|3|MOD||
R1|15|PHASE VALUE||
R1|27|PRESCALER||
R1|28|Reserved|1|
R2|0|Control bits|1:2|
R2|3|COUNTER RESET||
R2|4|CP THREE-STATE||
R2|5|POWER DOWN||0 - POWER UP, 1 - POWER DOWN
R2|6|PD POLARITY||
R2|7|LDP||
R2|8|LDF||
R2|9|CHARGE PUMP CURRENT SETTING||
R2|13|DOUBLE BUFF||
R2|14|R COUNTER||
R2|24|RDIV2||
R2|25|REFERENCE DOUBLER||
R2|26|MUXOUT||0 1 1 - DIGITAL LOCK DETECT
R2|29|LOW NOISE LOW SPUR||
R2|31|Reserved|1|
R3|0|Control bits|1:3|
R3|3|CLOCK DIVIDER||
R3|15|CLK DIV MODE||
R3|17|Reserved|1|
R3|18|CSR||
R3|19|Reserved|1|
R4|0|Control bits|1:4|
R4|3|OUTPUT POWER||
R4|5|RF OUTPUT ENABLE||
R4|6|AUX OUTPUT POWER||
R4|8|AUX OUTPUT ENABLE||
R4|9|AUX OUTPUT SELECT||
R4|10|MTLD||
R4|11|VCO POWER-DOWN||
R4|12|BAND SELECT CLKDIV||
R4|20|DIVIDER SELECT||
R4|23|FEEDBACK SELECT||
R4|24|Reserved|1|
R5|0|Control bits|1:5|
R5|3|Reserved|1|
R5|22|LD PIN MODE||
R5|24|Reserved|1|
'''

cmd_cb = lambda dev, cmd, val: spi_efc_cmd_cb(dev, cmd, val, ncpha='1', cpol='0')

def columns():
    return get_columns([c_ip_addr, c_spi, c_refin])

def get_menu(dev):
    return OD([('Registers', regs_cb)])

def get_regs(dev):
    data.add_hex_data(hex_data, cmd_cb=cmd_cb, fmt_cb=strip0x_fmt_cb)
    data.add_bin_data(bin_data)
    return data

