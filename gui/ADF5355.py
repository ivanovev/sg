
from collections import OrderedDict as OD
from util.columns import *
from .ADF4355_2 import Fout_src_cb, Fvco_src_cb, Fpfd_src_cb
from .callbacks import spi_efc_cmd_cb
from ..regs import RegsData, manyregs_cb

hex_data = '''
R00|00003E80|
R01|00000001|
R02|00000022|
R03|00000003|
R04|000D0004|
R05|00000005|
R06|00000006|
R07|00000007|
R08|000002C8|
R09|FFFFFFF9|
R10|8400001A|
R11|0070022B|
R12|0000000C|
'''

bin_data = '''
R00|0|Control bits|1:0|
R00|4|INT|
R00|20|PRESCALER|
R00|21|AUTOCAL|
R00|22|RESERVED|1|
R01|0|Control bits|1:1|
R01|4|FRAC1|
R01|28|RESERVED|1|
R02|0|Control bits|1:2|
R02|4|MOD2|
R02|18|FRAC2|
R03|0|Control bits|1:3|
R03|4|PHASE|
R03|28|PHASE ADJUST|
R03|29|PHASE RESYNC|
R03|30|SD LOAD RESET|
R03|31|RESERVED|1|
R04|0|Control bits|1:4|
R04|4|COUNTER RESET|
R04|5|CP THREE-STATE|
R04|6|PD|
R04|7|PD POLARITY|
R04|8|MUX LOGIC|
R04|9|REF MODE|
R04|10|CURRENT SETTING|
R04|14|DOUBLE BUFF|
R04|15|R COUNTER|
R04|25|RDIV2|
R04|26|REFERENCE DOUBLER|
R04|27|MUXOUT|
R04|30|RESERVED|1|
R05|0|Control bits|1:5|
R05|4|CLKDIV|
R05|16|CLKDIV MODE|
R05|18|RESERVED|1|
R05|19|CSR|
R05|20|RESERVED|
R05|23|ABP|
R05|24|RESERVED|
R06|0|Control bits|1:6|
R06|4|OUTPUT POWER|
R06|6|RF OUTPUT ENABLE|
R06|7|RESERVED|1|
R06|10|RFOUTB|
R06|11|MTLD|
R06|12|VCO POWER-DOWN|
R06|13|CP BLEED CURRENT|
R06|21|DIVIDER SELECT|
R06|24|FEEDBACK SELECT|
R06|25|RESERVED|1|
R06|28|VCO LDO|
R06|29|NEGATIVE BLEED|
R06|30|RESERVED|1|
R07|0|Control bits|1:7|
R07|4|LD MODE|
R07|5|FRAC-N LD PRECISION|
R07|7|LOL MODE|
R07|8|LD CYCLE COUNT|
R07|10|RESERVED|1|
R07|25|LE SYNC|
R07|26|RESERVED|1|
R08|0|Control bits|1:8|
R08|4|RESERVED|1:0x2C|
R09|0|Control bits|1:9|
R09|4|RESERVED|1:0xFFFFFFF|
R10|0|Control bits|1:10|
R10|4|RESERVED|1:0x8400001|
R11|0|Control bits|1:11|
R11|4|RESERVED|1:0x0070022|
R12|0|Control bits|1:12|
R12|4|RESERVED|1:0xC|
'''

def columns():
    return get_columns([c_ip_addr, c_spi, c_refin])

def get_menu(dev):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev):
    data = RegsData(columns=4)
    data.add_page('calc0')
    data.add('label1', label='Fout = Fvco / RF Divider')
    data.add_page('calc1')
    data.add('Fout', wdgt='entry', src=Fout_src_cb, state='readonly', msg='Fout')
    data.add('Fvco1', wdgt='entry', src=Fvco_src_cb, state='readonly', msg='Fvco')
    data.add('RFDIV', wdgt='combo', state='readonly', value=['1','2','4','8','16','32','64'], src=lambda d,v: d.log_src('R06', 21, 23, v), msg='RF DIVIDER')
    data.add_page('calc2')
    data.add('label2', label='Fvco = Fpfd × [INT + (FRAC1 +(FRAC2/MOD2)/MOD1)]')
    data.add_page('calc3')
    data.add('Fvco', wdgt='entry', src=Fvco_src_cb, state='readonly', msg='Fvco')
    data.add('Fpfd1', wdgt='entry', src=Fpfd_src_cb, state='readonly', msg='Fpfd')
    data.add('INT', wdgt='spin', value={'min':23, 'max':65535, 'step':1}, src=lambda d,v: d.bits_src('R00', 4, 19, v), msg='INT')
    data.add('FRAC1', wdgt='spin', value={'min':1, 'max':16777215, 'step':1}, src=lambda d,v: d.bits_src('R01', 4, 27, v), msg='FRAC1')
    data.add('FRAC2', wdgt='spin', value={'min':0, 'max':16383, 'step':1}, src=lambda d,v: d.bits_src('R02', 18, 31, v), msg='FRAC2')
    data.add('MOD2', wdgt='spin', value={'min':2, 'max':16383, 'step':1}, src=lambda d,v: d.bits_src('R02', 4, 17, v), msg='MOD2')
    data.add('MOD1', wdgt='entry', state='readonly', text='16777216', msg='MOD1')
    data.add_page('calc4')
    data.add('label2', label='Fpfd = REFin × [(1 + D)/(R × (1 + T))]')
    data.add_page('calc5')
    data.add('Fpfd', wdgt='entry', src=Fpfd_src_cb, state='readonly', msg='Fpfd')
    data.add('REFin', wdgt='entry', src=lambda d,v: d.dev_src('refin'), state='readonly', msg='REFin')
    data.add('D', wdgt='spin', value={'min':0, 'max':1, 'step':1}, src=lambda d,v: d.bits_src('R02', 26, 26, v), msg='D')
    data.add('R', wdgt='spin', value={'min':1, 'max':1023, 'step':1}, src=lambda d,v: d.bits_src('R04', 15, 24, v), msg='R')
    data.add('T', wdgt='spin', value={'min':0, 'max':1, 'step':1}, src=lambda d,v: d.bits_src('R04', 25, 25, v), msg='T')
    cmd_cb = lambda dev, cmd, val: spi_efc_cmd_cb(dev, cmd, val, ncpha='1', cpol='0')
    data.add_hex_data(hex_data, cmd_cb=cmd_cb)
    data.add_bin_data(bin_data)
    return data

