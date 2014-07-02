
from collections import OrderedDict as OD
from math import log
from ..regs import RegsData, get_bits, set_bits, manyregs_cb
from .callbacks import spi_efc_cmd_cb
from util.columns import *

def Format_src_cb(data, val):
    s = data.get_value('R02')
    if val == None:
        n = get_bits(s, 7, 7)
        if n:
            return 'unsigned'
        else:
            return 'signed'
    else:
        n = 0
        if val == 'unsigned':
            n = 1
        s = set_bits(s, n, 7, 7)
        data.set_value('R02', s)

def Gain_src_cb(data, val, r70, r98):
    lsb = data.get_value(r70)
    msb = data.get_value(r98)
    if val == None:
        gain70 = get_bits(lsb, 0, 7)
        gain98 = get_bits(msb, 0, 1)
        gain = gain70 | (gain98 << 8)
        #if (gain & 0x7F) == 0 or gain == 0x3FF:
        gain = '0x%.3X' % gain
        return gain
        #return '0x000'
    else:
        try:
            gain = int(val, 16)
        except:
            gain = 0
        gain70 = gain & 0xFF
        gain98 = gain >> 8
        lsb = set_bits(lsb, gain70, 0, 7)
        msb = set_bits(msb, gain98, 0, 1)
        data.set_value(r70, lsb)
        data.set_value(r98, msb)

def DIR_src_cb(data, val, reg):
    r = data.get_value(reg)
    if val == None:
        direction = get_bits(r, 6, 6)
        direction = 'source' if direction == 0 else 'sink'
        return direction
    else:
        direction = (0 if val == 'source' else 1)
        r = set_bits(r, direction, 6, 6)
        data.set_value(reg, r)

def SIGN_src_cb(data, val, reg):
    r = data.get_value(reg)
    if val == None:
        sgn = get_bits(r, 7, 7)
        sgn = '+' if sgn == 0 else '-'
        return sgn
    else:
        sgn = (0 if val == '+' else 1)
        r = set_bits(r, sgn, 7, 7)
        data.set_value(reg, r)

def PLLBand_src_cb(data, val):
    r = data.get_value('R08')
    if val == None:
        bits = get_bits(r, 2, 7)
        ret = band_list[bits]
        return ret
    else:
        bits = band_list.index(val)
        r = set_bits(r, bits, 2, 7)
        data.set_value('R08', r)

def PLLLoopDivide_src_cb(data, val):
    s = data.get_value('R09')
    if val == None:
        n = get_bits(s, 3, 4)
        n += 1
        return '%d' % (2**n)
    else:
        n = int(val)
        n = int(log(n, 2))
        n -= 1
        s = set_bits(s, n, 3, 4)
        data.set_value('R09', s)

gain_list = ['0x000','0x080','0x100','0x180','0x200','0x280','0x300','0x380','0x3FF']
band_list = ['911-951','922-966','935-981','950-996','963-1011','976-1026','991-1041','998-1049',
'1019-1072','1026-1067','1047-1103','1055-1106','1078-1135','1086-1145','1109-1166','1115-1178',
'1141-1198','1149-1210','1174-1231','1182-1242','1210-1264','1215-1277','1245-1299','1250-1313',
'1282-1336','1287-1352','1317-1375','1324-1389','1356-1412','1361-1427','1397-1451','1402-1468',
'1435-1489','1439-1505','1475-1529','1480-1553','1514-1575','1521-1600','1555-1606','1564-1639',
'1596-1658','1604-1681','1640-1702','1651-1729','1684-1748','1685-1766','1699-1780','1730-1794',
'1729-1810','1748-1825','1774-1840','1779-1853','1794-1869','1822-1885','1830-1897','1848-1915',
'1870-1931','1883-1942','1902-1961','1923-1977','1938-1992','1956-2008','1975-2026','Auto']

def cmd_cb(dev, cmd, val=None):
    if val != None:
        r = int(cmd[1:])
        return 'spi %s %02X%s' % (dev['spi'], r, val)
    else:
        return spi_efc_cmd_cb(dev, cmd, val)

hex_data = '''
R00|00|Comm
R01|00|Digital Control
R02|00|Digital Control
R03|00|Sync Control
R04|00|Sync Control
R05|00|Sync Control
R06|00|Sync Control
R07|00|Sync Control
R08|CF|PLL Control
R09|37|PLL Control
R0A|38|Misc. Control
R0B|F9|I DAC Control
R0C|01|I DAC Control
R0D|00|Aux DAC1 Control
R0E|00|Aux DAC1 Control
R0F|F9|Q DAC Control
R10|01|Q DAC Control
R11|00|Aux DAC2 Control
R12|00|Aux DAC2 Control
'''

bin_data = '''
R00|0|Unused||: True
R00|1|PLL lock indicator|1|
R00|2|Unused||: True
R00|3|Auto power-down enable||
R00|4|Power-down mode||
R00|5|Software reset||
R00|6|LSB/MSB first||
R00|7|SDIO bidirectional||
R01|0|Zero stuffing enable||
R01|1|DATACLK Delay[4]||
R01|2|Filter Modulation Mode[3:0]||
R01|6|Interpolation Factor[1:0]||
R02|0|Q first||
R02|1|TxEnable invert||
R02|2|DATACLK invert||
R02|3|Inverse sinc enable||
R02|4|DATACLK delay enable||
R02|5|Real mode||
R02|6|Single port||
R02|7|Data format||
R03|0|Reserved||: True
R03|4|Data Clock Divide Ratio<1:0>||
R03|6|Data Clock Delay Mode<1:0>||
R04|0|SYNC_O Delay[4]||
R04|1|SYNC_O Divide[2:0]||
R04|4|DATACLK Delay[3:0]||
R05|0|SYNC_I Delay[4]||
R05|1|SYNC_I Ratio[2:0]||
R05|4|SYNC_O Delay[3:0]||
R06|0|SYNC_I Timing Margin[3:0]||
R06|4|SYNC_I Delay[3:0]||
R07|0|Clock State[4:0]||
R07|5|SYNC_O triggering edge||
R07|6|SYNC_O enable||
R07|7|SYNC_I enable||
R08|0|PLL VCO Drive[1:0]||
R08|2|PLL Band Select[5:0]||
R09|0|PLL Bias[2:0]||
R09|3|PLL Loop Divide Ratio[1:0]||
R09|5|PLL VCO Divide Ratio[1:0]||
R09|7|PLL enable||
R0A|0|PLL Loop Bandwidth[4:0]||
R0A|5|VCO Control Voltage[2:0]|1|
R0B|0|I DAC Gain Adjustment[7:0]||
R0C|0|I DAC Gain Adjustment[9:8]||
R0C|2|Unused||: True
R0C|6|I DAC power-down||
R0C|7|I DAC sleep||
R0D|0|Auxiliary DAC1 Data[7:0]||
R0E|0|Auxiliary DAC1 Data[9:8]||
R0E|2|Unused||: True
R0E|5|Auxiliary DAC1 power-down||
R0E|6|Auxiliary DAC1 current direction||
R0E|7|Auxiliary DAC1 sign||
R0F|0|Q DAC Gain Adjustment[7:0]||
R10|0|Q DAC Gain Adjustment[9:8]||
R10|2|Unused||: True
R10|6|Q DAC power-down||
R10|7|Q DAC sleep||
R11|0|Auxiliary DAC2 Data[7:0]||
R12|0|Auxiliary DAC2 Data[9:8]||
R12|2|Unused||: True
R12|5|Auxiliary DAC2 power-down||
R12|6|Auxiliary DAC2 current direction||
R12|7|Auxiliary DAC2 sign||
'''

def columns():
    return get_columns([c_ip_addr, c_spi])

def get_menu(dev, cc=None):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev, cc=None):
    data = RegsData(sz=8)
    data.add_page('calc0')
    data.add('label1', label='Digital Control')
    data.add('dataformat', wdgt='combo', state='readonly', value=['signed','unsigned'], src=Format_src_cb, msg='Data format')
    data.add('interpolation', wdgt='combo', state='readonly', value=['1','2', '4', '8'], src=lambda d,v: d.log_src('R01', 6, 7, v), msg='Interpolation')
    data.add_page('calc1')
    data.add('igain', wdgt='combo', value=gain_list, src=lambda d,v: Gain_src_cb(d,v,'R0B','R0C'), msg='I DAC Gain')
    data.add('qgain', wdgt='combo', value=gain_list, src=lambda d,v: Gain_src_cb(d,v,'R0F','R10'), msg='Q DAC Gain')
    data.add_page('calc2')
    data.add('pllband', wdgt='combo', state='readonly', value=band_list, src=PLLBand_src_cb, msg='PLL Band Select')
    data.add('pllvcodivide', wdgt='combo', state='readonly', value=['1','2','4','8'], src=lambda d,v: d.log_src('R09', 5, 6, v), msg='PLL VCO divide ratio')
    data.add('pllloopdivide', wdgt='combo', state='readonly', value=['2','4','8','16'], src=PLLLoopDivide_src_cb, msg='PLL Loop divide ratio')
    data.add_page('calc3')
    data.add('dac1dir', wdgt='combo', state='readonly', value=['source','sink'], src=lambda d,v: DIR_src_cb(d,v,'R0E'), msg='AUX DAC1 Direction')
    data.add('dac1sign', wdgt='combo', state='readonly', value=['+','-'], src=lambda d,v: SIGN_src_cb(d,v,'R0E'), msg='AUX DAC1 Sign')
    data.add('dac1gain', wdgt='combo', state='readonly', value=gain_list, src=lambda d,v: Gain_src_cb(d,v,'R0D','R0E'), msg='AUX DAC1 Data')
    data.add_page('calc4')
    data.add('dac2dir', wdgt='combo', state='readonly', value=['source','sink'], src=lambda d,v: DIR_src_cb(d,v,'R12'), msg='AUX DAC1 Direction')
    data.add('dac2sign', wdgt='combo', state='readonly', value=['+','-'], src=lambda d,v: SIGN_src_cb(d,v,'R12'), msg='AUX DAC1 Sign')
    data.add('dac2gain', wdgt='combo', state='readonly', value=gain_list, src=lambda d,v: Gain_src_cb(d,v,'R11','R12'), msg='AUX DAC1 Data')

    data.add_hex_data(hex_data, cmd_cb=cmd_cb)
    data.add_bin_data(bin_data)
    data.columns = 5
    return data

