
from collections import OrderedDict as OD
from copy import deepcopy
from itertools import chain

from ...regs import RegsData, manyregs2_cb
from . import AD9361_bin, AD9361_hex
from util.columns import *

def columns():
    return get_columns([c_ip_addr, c_spi, c_refin])

def get_menu(dev):
    return OD([('Registers', manyregs2_cb)])

def get_regs(dev):
    data = RegsData(sz=8)
    data.add_page('calc.setup0')
    data.add('REFin', label='REFin, MHz', wdgt='entry', state='readonly', src=lambda d,v: d.dev_src('refin'))
    hex_data = data.parse_hex_data(AD9361_hex.data)
    data.add_group('setup1', hex_data, 'R000', 'R017', 0)
    data.add_group('setup2', hex_data, 'R018', 'R03A', 1)
    data.add_group('setup3', hex_data, 'R03B', 'R05F', 2)
    data.add_group('tx1', hex_data, 'R060', 'R081', 3)
    data.add_group('tx2', hex_data, 'R08E', 'R0AE', 4)
    data.add_group('tx3', hex_data, 'R0B0', 'R0D7', 5)
    data.add_group('rx1', hex_data, 'R0F0', 'R10E', 6)
    data.add_group('rx2', hex_data, 'R110', 'R12A', 7)
    data.add_group('rx3', hex_data, 'R12C', 'R15D', 8)
    data.add_group('rx4', hex_data, 'R160', 'R182', 9)
    data.add_group('rx5', hex_data, 'R185', 'R1B3', 10)
    data.add_group('rx6', hex_data, 'R1C0', 'R1FC', 11)
    data.add_group('rx7', hex_data, 'R200', 'R226', 12)
    data.add_group('analog1', hex_data, 'R230', 'R261', 13)
    data.add_group('analog2', hex_data, 'R270', 'R28F', 14)
    data.add_group('analog3', hex_data, 'R290', 'R3FE', 15)
    data.add_bin_data(AD9361_bin.data)
    data.columns=8
    return data

