
from collections import OrderedDict as OD
from .ADF4350 import columns
from ..regs import RegsData, regs_cb
from .callbacks import strip0x_fmt_cb, spi_efc_cmd_cb

def Fvco_src_cb(data, val):
    REFin = float(data.get_value('REFin'))
    INT = float(data.get_value('INT'))
    FRAC = float(data.get_value('FRAC'))
    MOD = float(data.get_value('MOD'))
    Fvco = float(REFin)*(INT + float(FRAC)/MOD)
    return '%.3f' % Fvco

data = RegsData(sz=24)
data.add_page('calc0')
data.add('label1', label='Fvco = REFin x (INT + FRAC/MOD) / 2')
data.add_page('calc1')
data.add('Fvco', wdgt='entry', state='readonly', src=Fvco_src_cb)
data.add('REFin', wdgt='entry', state='readonly', src=lambda d,v: d.dev_src('refin'))
data.add('INT', wdgt='spin', value={'min':23, 'max':65535, 'step':1}, src=lambda d,v: d.bits_src('R0', 3, 9, v))
data.add('FRAC', wdgt='spin', value={'min':0, 'max':4094, 'step':1}, src=lambda d,v: d.bits_src('R2', 3, 13, v))
data.add('MOD', wdgt='spin', value={'min':2, 'max':4095, 'step':1}, src=lambda d,v: d.bits_src('R1', 3, 13, v))

hex_data = '''
R0|000020|
R1|000031|
R2|00004A|
R3|000043|
R4|000104|
R5|000205|
R6|000106|
R7|000087|
'''

bin_data = '''
R0|0|Control bits|1:0|
R0|3|INT||
R0|10|DIVIDE MODE||
R0|11|Reserved|1|
R1|0|Control bits|1:1|
R1|3|MOD||
R1|14|Reserved|1|
R2|0|Control bits|1:2|
R2|3|FRAC||
R2|14|Reserved|1|
R3|0|Control bits|1:3|
R3|3|DITHER RESTART||
R3|20|DITHER ENABLE||
R3|21|DITHER MAGNITUDE||
R3|23|Reserved|1|
R4|0|Control bits|1:4|
R4|3|PFD ANTIBACKLASH||
R4|5|PFD EDGE||
R4|7|CP CONTROL||
R4|9|CP SRC||
R4|10|CP CURRENT||
R4|12|PFD PHASE OFFSET MUL||
R4|17|PFD POL||
R4|18|CP CURRENT REF||
R4|19|INPUT REF PATH||
R4|21|REF OUTPUT MUX||
R5|0|Control bits|1:5|
R5|3|LO DRV||
R5|4|LO EXT||
R5|5|LO DIV1||
R5|6|PLL EN||
R5|7|LO DIV2||
R5|8|CAP DAC||
R5|12|Reserved|1|
R6|0|Control bits|1:6|
R6|3|VCO BAND SELECT||
R6|9|VCO BW SW CTRL||
R6|10|VCO AMPLITUDE||
R6|16|VCO SWITCH||
R6|17|VCO ENABLE||
R6|18|VCO LDO ENABLE||
R6|19|3.3V LDO ENABLE||
R6|20|CHARGE PUMP ENABLE||
R6|21|Reserved|1|
R7|0|Control bits|1:7|
R7|3|Reserved|1|
R7|21|MIXER B_EN||
R7|22|XVCO||
R7|23|Reserved|1|
'''

def get_menu(dev):
    return OD([('Registers', regs_cb)])

def get_regs(dev):
    data.add_hex_data(hex_data, cmd_cb=spi_efc_cmd_cb, fmt_cb=strip0x_fmt_cb)
    data.add_bin_data(bin_data)
    return data

