
from . import ADF4350
from copy import deepcopy

bin_data = '''
R1|0|Control bits|1|
R1|3|MOD||
R1|15|PHASE VALUE||5
R1|27|PRESCALER||7
R1|28|PHASE ADJUST||8
R1|29|Reserved|1|9
R3|0|Control bits|1|
R3|3|CLOCK DIVIDER||
R3|15|CLK DIV MODE||5
R3|17|Reserved|1|7
R3|18|CSR||8
R3|19|Reserved|1|9
R3|21|CHARGE CANCEL||1
R3|22|ABP||2
R3|23|BAND SELECT CLOCK MODE||3
R3|24|Reserved|1|4
'''

columns = ADF4350.columns
get_menu = ADF4350.get_menu

def data_init(data, init):
    for i in range(0, len(init)):
        data['hex']['R%d' % i].text = init[i]

def get_regs(dev):
    data = deepcopy(ADF4350.get_regs(dev))
    init = ['07D00000', '08004E21', '78066042', '00000003', '00A0903C', '00580005']
    data_init(data, init)
    for i in ['R1', 'R3']:
        data.remove_page(i)
    data.add_bin_data(bin_data)
    return data

