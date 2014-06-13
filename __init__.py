
from . import gui, srv
from util.columns import *
from util.misc import app_devtypes
from .regs import startup_cb

devdata = lambda: get_devdata('SG', get_columns([c_ip_addr, c_spi, c_gpio, c_refin]), app_devtypes(gui))

