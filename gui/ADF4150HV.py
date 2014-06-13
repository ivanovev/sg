
from . import ADF4150
from . import ADF4351
from copy import deepcopy

bin_data = '''
R2|0|Control bits|1|
R2|3|COUNTER RESET||
R2|4|CP THREE-STATE||
R2|5|POWER DOWN||: 0 - POWER UP, 1 - POWER DOWN
R2|6|Reserved|1|
R2|7|LDP||
R2|8|LDF||
R2|9|CHARGE PUMP CURRENT SETTING||
R2|12|Reserved|1|2
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
R3|18|BOOST EN||8
R3|19|Reserved|1|9
R4|0|Control bits|1|
R4|3|OUTPUT POWER||
R4|5|RF OUTPUT ENABLE||
R4|6|Reserved|1|
R4|10|MTLD||0
R4|11|Reserved|1|1
R4|20|DIVIDER SELECT||0
R4|23|FEEDBACK SELECT||3
R4|24|Reserved|1|4
R5|0|Control bits|1|
R5|3|Reserved|1|
R5|22|LD PIN MODE||2
R5|24|Reserved|1|4
R5|29|CC ENABLE||9
R5|30|ABP WIDTH||0
'''

columns = ADF4150.columns
get_menu = ADF4150.get_menu

def get_regs(dev):
    data = deepcopy(ADF4150.get_regs(dev))
    init = ['00320000', '00005141', '78006042', '00000003', '0080002C', '10000005']
    ADF4351.data_init(data, init)
    for i in range(2, 6):
        data.remove_page('R%d' % i)
    data.add_bin_data(bin_data)
    return data

