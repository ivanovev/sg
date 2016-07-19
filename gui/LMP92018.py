
from collections import OrderedDict as OD
from ..regs import RegsData, manyregs_cb
from util import util_io_cb
from util.columns import *

def lmp_fmt_cb(val, read=True):
    lmp_fmt_cb.read = read
    if val[0:2] == '0x':
        val = int(val, 16)
        val &= ~0x800000
        val = '%.6X' % val
    return val

def lmp_cmd_cb(dev, cmd, val):
    if lmp_fmt_cb.read:
        val = int(val, 16)
        val |= 0x800000
        val = '0x%.6X' % val
    else:
        val = int(val, 16)
        val &= ~0x800000
        val = '0x%.6X' % val
    cmd1 = 'spi %s %s 1 0' % (dev['spi'], val)
    cmd2 = 'spi %s %s 1 0' % (dev['spi'], '0x000000')
    return 'telnet %s; %s' % (cmd1, cmd2)

hex_data = '''
R0|000000|NOOP
R1|100000|Temperature sensor configure
R2|110000|Reference configure
R3|180000|DAC configure
R4|190000|Update all DACs
R5|1E0000|General configuration
R6|1F0000|GPIO configure
R7|200000|Status
R8|300000|GPI state
R9|310000|GPO data
R10|400000|Vendor ID
R11|410000|Version/stepping
R12|500000|DAC0
R13|510000|DAC1
R14|520000|DAC2
R15|540000|DAC3
R16|600000|ADC0
R17|610000|ADC1
R18|620000|ADC2
R19|630000|ADC3
R20|640000|ADC4
R21|650000|ADC5
R22|660000|ADC6
R23|670000|ADC7
'''

bin_data = '''
R0|0|DATA||
R0|16|Command|1:0x00|
R0|23|R/W|1|
R1|0|TSS||
R1|1|Don't care||
R1|16|Command|1:0x10|
R1|23|R/W|1|
R2|0|CREF||
R2|3|Don't care||
R2|16|Command|1:0x11|
R2|23|R/W|1|
R3|0|CDAC||
R3|4|Don't care||
R3|16|Command|1:0x18|
R3|23|R/W|1|
R4|0|00|1|
R4|2|DDATA||
R4|12|0000|1|
R4|16|Command|1:0x19|
R4|23|R/W|1|
R5|0|DRDY||
R5|1|Don't care||
R5|16|Command|1:0x1E|
R5|23|R/W|1|
R6|0|CGPIO||
R6|12|Don't care||
R6|16|Command|1:0x1F|
R6|23|R/W|1|
R7|0|RDY||
R7|1|Don't care||
R7|16|Command|1:0x20|
R7|23|R/W|1|
R8|0|SGPI||
R8|12|Don't care||
R8|16|Command|1:0x30|
R8|23|R/W|1|
R9|0|CGPO||
R9|12|Don't care||
R9|16|Command|1:0x31|
R9|23|R/W|1|
R10|0|ID|1|
R10|16|Command|1:0x40|
R10|23|R/W|1|
R11|0|STEP||
R11|4|VER||
R11|16|Command|1:0x41|
R11|23|R/W|1|
R12|0|00|1|
R12|2|DDATA||
R12|12|Don't care|1|
R12|16|Command|1:0x50|
R12|23|R/W|1|
R13|0|00|1|
R13|2|DDATA||
R13|12|Don't care|1|
R13|16|Command|1:0x51|
R13|23|R/W|1|
R14|0|00|1|
R14|2|DDATA||
R14|12|Don't care|1|
R14|16|Command|1:0x52|
R14|23|R/W|1|
R15|0|00|1|
R15|2|DDATA||
R15|12|Don't care|1|
R15|16|Command|1:0x53|
R15|23|R/W|1|
R16|0|00|1|
R16|2|ADATA||
R16|12|Don't care|1|
R16|16|Command|1:0x60|
R16|23|R/W|1|
R17|0|00|1|
R17|2|ADATA||
R17|12|Don't care|1|
R17|16|Command|1:0x61|
R17|23|R/W|1|
R18|0|00|1|
R18|2|ADATA||
R18|12|Don't care|1|
R18|16|Command|1:0x62|
R18|23|R/W|1|
R19|0|00|1|
R19|2|ADATA||
R19|12|Don't care|1|
R19|16|Command|1:0x63|
R19|23|R/W|1|
R20|0|00|1|
R20|2|ADATA||
R20|12|Don't care|1|
R20|16|Command|1:0x64|
R20|23|R/W|1|
R21|0|00|1|
R21|2|ADATA||
R21|12|Don't care|1|
R21|16|Command|1:0x65|
R21|23|R/W|1|
R22|0|00|1|
R22|2|ADATA||
R22|12|Don't care|1|
R22|16|Command|1:0x66|
R22|23|R/W|1|
R23|0|00|1|
R23|2|ADATA||
R23|12|Don't care|1|
R23|16|Command|1:0x67|
R23|23|R/W|1|
'''

def columns():
    return get_columns([c_ip_addr, c_spi])

def get_menu(dev):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev):
    data = RegsData(sz=24, io_cb=util_io_cb)
    data.add_hex_data(hex_data, cmd_cb=lmp_cmd_cb, fmt_cb=lmp_fmt_cb)
    data.add_bin_data(bin_data)
    data.columns = 4
    return data

