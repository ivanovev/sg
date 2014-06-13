
from . import ADRF6601
from copy import deepcopy

bin_data = '''
R5|0|Control bits|1:5|
R5|3|LO DRV||
R5|4|LO IN/OUT CNTRL||
R5|5|LO DIV 2/3||
R5|6|PLL EN||
R5|7|MIXER BIAS EN||
R5|8|CDAC||
R5|12|Reserved|1|
R6|0|Control bits|1:6|
R6|3|VCO BAND SELECT||
R6|9|VCO BS SRC|
R6|10|VCO AMPLITUDE||
R6|16|VCO SWITCH||
R6|17|VCO ENABLE||
R6|18|VCO LDO ENABLE||
R6|19|3.3V LDO ENABLE||
R6|20|CP ENABLE||
R6|21|Reserved|1|
R7|0|Control bits|1:7|
R7|3|Reserved|1|
R7|22|XVCO||
R7|23|Reserved|1|
'''

columns = ADRF6601.columns
get_menu = ADRF6601.get_menu

def get_regs(dev):
    data = ADRF6601.get_regs(dev)
    for i in ['R5', 'R6', 'R7']:
        data.remove_page(i)
    data.add_bin_data(bin_data)
    return data
