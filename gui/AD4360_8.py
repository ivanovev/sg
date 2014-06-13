
from collections import OrderedDict as OD
from copy import deepcopy
from .ADF4350 import columns
from ..regs import RegsData, regs_cb
from .callbacks import strip0x_fmt_cb, spi_efc_cmd_cb

def Fout_src_cb(data, val):
    REFin = float(data.get_value('REFin'))
    B = float(data.get_value('B'))
    R = float(data.get_value('R'))
    return '%.3f' % (REFin * B / R)

data = RegsData()
data.add_page('calc0')
data.add('label1', label='Fvco = REFin * B / R')
data.add_page('calc1')
data.add('Fout', wdgt='entry', state='readonly', src=Fout_src_cb, msg='Fout')
data.add('REFin', wdgt='entry', state='readonly', src=lambda d,v: d.dev_src('refin'), msg='REFin')
spn = RegsData.spn
data.add('B', wdgt='spin', value=spn(3, 8191), src=lambda d,v:d.bits_src('R2', 8, 20, v, minimum=3), msg='B')
data.add('R', wdgt='spin', value=spn(1, 16383), src=lambda d,v:d.bits_src('R1', 2, 15, v, minimum=1), msg='R')

hex_data = '''
R0|000020|CONTROL LATCH
R2|000802|N COUNTER LATCH
R1|000015|R COUNTER LATCH
'''
bin_data = '''
R0|0|Control bits|1:0|
R0|2|Core power level||
R0|4|Counter reset||
R0|5|Muxout control||001 - LD'
R0|8|Phase detector polarity||
R0|9|CP three-state||
R0|10|CP gain||
R0|11|Mute-til-ld||
R0|12|Output power level||
R0|14|Current setting 1||
R0|17|Current setting 2||
R0|20|POWER DOWN 1||
R0|21|POWER DOWN 2||
R0|22|Reserved|1|
R2|0|Control bits|1:2|
R2|2|Reserved|1|
R2|8|B-counter||
R2|21|CP-gain||
R2|22|Reserved|1|
R1|0|Control bits|0:1
R1|2|R-counter||
R1|16|Anti-backlash pulse width||
R1|18|Lock-detect precision||
R1|19|Test-mode bit||
R1|20|Band select clock||
R1|22|Reserved|1|
'''

def get_menu(dev):
    return OD([('Registers', regs_cb)])

def get_regs(dev):
    data.add_hex_data(hex_data, spi_efc_cmd_cb, strip0x_fmt_cb)
    data.add_bin_data(bin_data)
    return data

