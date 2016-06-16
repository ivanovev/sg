
from copy import deepcopy
from . import ADF4350, ADF4351

bin_data = '''
R0|0|Control bits|1|
R0|3|FRAC||
R0|15|INT||5
R0|31|Reserved|1|1
R1|0|Control bits|1|
R1|3|MOD||
R1|15|PHASE VALUE||5
R1|27|PRESCALER||7
R1|28|Reserved|1|8
R2|0|Control bits|1|
R2|3|COUNTER RESET||
R2|4|CP THREE-STATE||
R2|5|POWER DOWN||: 0 - POWER UP, 1 - POWER DOWN
R2|6|PD POLARITY||
R2|7|LDP||
R2|8|LDF||
R2|9|CHARGE PUMP CURRENT SETTING||
R2|13|DOUBLE BUFF||3
R2|14|R COUNTER||4
R2|24|RDIV2||4
R2|25|REFERENCE DOUBLER||5
R2|26|MUXOUT||6: 0 1 1 - DIGITAL LOCK DETECT
R2|29|LOW NOISE LOW SPUR||9
R2|31|Reserved|1|1
R3|0|Control bits|1|
R3|3|CLOCK DIVIDER||
R3|15|CLK DIV MODE||5
R3|17|Reserved|1|7
R3|18|CSR||8
R3|19|Reserved|1|9
R3|21|CHARGE CANCEL||1
R3|22|ABP||2
R3|23|Reserved|1|3
R4|0|Control bits|1|
R4|3|OUTPUT POWER||
R4|5|RF OUTPUT ENABLE||
R4|6|Reserved|1|
R4|10|MTLD||0
R4|11|Reserved|1|1
R4|20|DIVIDER SELECT||0
R4|23|FEEDBACK SELECT||3
R4|24|Reserved|1|4
'''

columns = ADF4350.columns
get_menu = ADF4350.get_menu

def get_regs(dev):
    data = deepcopy(ADF4350.get_regs(dev))
    init = ['00320000', '00005141', '78006042', '00000003', '0080002C', '00580005']
    ADF4351.data_init(data, init)
    for i in range(0, 5):
        data.remove_page('R%d' % i)
    data.add_bin_data(bin_data)
    return data

