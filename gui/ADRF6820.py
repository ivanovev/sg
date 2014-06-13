
from collections import OrderedDict as OD

from ..regs import RegsData, manyregs_cb
from .callbacks import strip0x_fmt_cb, spi_efc_cmd_cb
from . import ADRF6820_hex, ADRF6820_bin
from util.columns import *

def columns():
    return get_columns([c_ip_addr, c_spi, c_refin])

def get_menu(dev):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev):
    data = RegsData(sz=16)
    data.columns = 5
    data.add_hex_data(ADRF6820_hex.data, cmd_cb=spi_efc_cmd_cb, fmt_cb=strip0x_fmt_cb)
    data.add_bin_data(ADRF6820_bin.data)
    return data
