
from .regsdata import *
from .regs import Regs
from .manyregs import Manyregs
from .manyregs2 import Manyregs2
import util

def regs_cb(dev):
    util.process_cb(mode='regs', dev=dev)

def manyregs_cb(dev):
    util.process_cb(mode='manyregs', dev=dev)

def manyregs2_cb(dev):
    util.process_cb(mode='manyregs2', dev=dev)

def startup_cb(apps, mode, dev):
    if mode in ['regs', 'manyregs', 'manyregs2']:
        getter = util.app_gui(apps, dev[util.c_type], 'get_regs')
        data = getter(dev)
        if mode == 'regs':
            return Regs(dev=dev, data=data)
        if mode == 'manyregs':
            return Manyregs(dev=dev, data=data)
        if mode == 'manyregs2':
            return Manyregs2(dev=dev, data=data)

