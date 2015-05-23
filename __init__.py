
from . import gui, srv
from util.columns import *
from util.misc import app_devtypes, app_devdata
from .regs import startup_cb

devdata = lambda: app_devdata('SG', get_columns([c_ip_addr, c_spi, c_gpio, c_refin]), app_devtypes(gui))

