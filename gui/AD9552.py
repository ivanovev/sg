
from collections import OrderedDict as OD
from .ADF4350 import columns
from .callbacks import spi_efc_cmd_cb
from ..regs import RegsData, manyregs_cb

def cmd_cb(dev, cmd, val=None):
    if val != None:
        r = int(cmd[1:])
        return 'spi %s %02X%s' % (dev['spi'], r, val)
    else:
        return spi_efc_cmd_cb(dev, cmd, val)

hex_data = '''
R00|18|Serial port control
R04|00|Readback control
R05|00|I/O update
R0A|80|PLL charge pump and PFD control
R0B|30|PLL charge pump and PFD control
R0C|00|PLL charge pump and PFD control
R0D|00|PLL charge pump and PFD control
R0E|70|VCO control
R0F|80|VCO control
R10|80|VCO control
R11|00|PLL control
R12|80|PLL control
R13|00|PLL control
R14|00|PLL control
R15|20|PLL control
R16|00|PLL control
R17|01|PLL control
R18|00|PLL control
R19|20|PLL control
R1A|00|Input receiver and band gap
R1B|80|XTAL tuning control
R1C|00|XTAL control
R1D|00|XTAL control
R32|A8|OUT1 driver control
R33|00|Select OUT2 source
R34|A8|OUT2 driver control
'''

bin_data = '''
R00|0|Unused|1|
R00|1|LSB first||
R00|2|Register map reset||
R00|3|Unused|1|
R00|5|Register map reset (aclr)||
R00|6|LSB first||
R00|7|Unused|1|
R04|0|Readback control||
R04|1|Unused|1|
R05|0|I/O update (aclr)||
R05|1|Unused|1|
R0A|0|Charge pump current control[7:0]||
R0B|0|Force VCO to midpoint frequency||
R0B|1|PFD reference input edge control||
R0B|2|PFD feedback input edge control||
R0B|3|Enable CP mode control||
R0B|4|CP mode[1:0]||
R0B|6|Enable SPI control of antiback-lash period||
R0B|7|Enable SPI control of charge pump current||
R0C|0|Unused|1|
R0C|3|Enable CP offset current control||
R0C|4|CP offset current[1:0]||
R0C|6|CP offset current polarity||
R0C|7|Unused|1|
R0D|0|PLL lock detector power-down||
R0D|6|Antibacklash control[1:0]||
R0E|0|Enable SPI control of VCO band setting||
R0E|1|Boost VCO supply||
R0E|2|Enable SPI control of VCO calibration||
R0E|3|ALC threshold[2:0]||
R0E|6|Enable ALC||
R0E|7|Calibrate VCO (aclr)||
R0F|0|Unused|1|
R0F|2|VCO level control[5:0]||
R10|0|Unused|1|
R10|1|VCO band control[6:0]||
R11|0|N[7:0] (SDM integer part)||
R12|0|MOD[19:12] (SDM modulus)||
R13|0|MOD[11:4] (SDM modulus)||
R14|0|Reset PLL||
R14|1|Disable SDM||
R14|2|Bypass SDM||
R14|3|Enable SPI control of output frequency||
R14|4|MOD[3:0] (SDM modulus)||
R15|0|FRAC[19:12] (SDM fractional part)||
R16|0|FRAC[11:4] (SDM fractional part)||
R17|0|P1 divider[5]||
R17|1|Unused|1|
R17|4|FRAC[3:0] (SDM fractional part)||
R18|0|P0 divider[2:0]||
R18|3|P1 divider[4:0]||
R19|0|Unused|1|
R19|7|Enable SPI control of OUT1 dividers||
R1A|0|Enable SPI control of band gap voltage||
R1A|1|Unused|1|
R1A|2|Band gap voltage adjust[4:0]||
R1A|7|Receiver reset (aclr)||
R1B|0|XTAL tuning capacitor control[5:0]||
R1B|6|Unused|1|
R1B|7|Disable SPI control of XTAL tuning||
R1C|0|Unused|1|
R1D|0|Use crystal resonator||
R1D|1|Unused|1|
R1D|2|Select 2× Unused frequency multiplier||
R1D|3|Unused|1|
R32|0|Enable SPI control of OUT1 driver control||
R32|1|OUT1 CMOS polarity[1:0]||
R32|3|OUT1 mode control[2:0]||
R32|6|OUT1 power-down||
R32|7|OUT1 drive strength||
R33|0|Unused|1|
R33|3|OUT2 source||
R33|4|Unused|1|
R34|0|Enable SPI control of OUT2 driver control||
R34|1|OUT2 CMOS polarity[1:0]||
R34|3|OUT2 mode control[2:0]||
R34|6|OUT2 power-down||
R34|7|OUT2 drive strength||
'''

def get_menu(dev):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev):
    data = RegsData(sz=8)
    data.add_page('calc0')
    data.add('label1', label='AD9552')
    data.add_hex_data(hex_data)
    data.add_bin_data(bin_data)
    data.columns = 3
    return data

