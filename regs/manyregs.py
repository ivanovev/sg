
import tkinter as tk

from collections import OrderedDict as OD
from math import ceil

from .regs import Regs

class Manyregs(Regs):
    def __init__(self, dev, data, parent=None):
        Regs.__init__(self, dev=dev, data=data, parent=parent, standalone=True)

    def init_custom_layout(self):
        self.init_calc(self.fcalc)
        self.init_bottom_frame()
        f1 = self.init_bottom_hex()
        f1.pack(fill=tk.BOTH)

    def init_bottom_frame(self):
        self.fbl = tk.Frame(self.fb)
        self.fbl.pack(side='left', fill=tk.BOTH, expand=1)

        self.fbr = tk.Frame(self.fb)
        self.fbr.pack(side='right', fill=tk.BOTH)
        registers = tk.Button(self.fbr, text='Registers', command=self.regs_cb)
        registers.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

    def init_bottom_hex(self, name='hex'):
        f1 = tk.Frame(self.fbl)
        i = 0
        columns = 8
        if hasattr(self.data, 'columns'):
            columns = self.data.columns
        cmds = self.data[name]
        rows = ceil(float(len(cmds))/columns)
        width = int(self.data.sz/4) + 1
        for k,v in cmds.items():
            col = int(i % columns)
            row = int(i / columns)
            v.state = 'readonly'
            v.trace_cb = self.hex_cb
            l, w = self.make_cmdw(f1, k, cmds)
            v.l.set('0')
            l.grid(column=2*col, row=row, sticky=tk.E+tk.W)
            if 'init' in self.data:
                v.t.set(self.data['init'][i])
            w.configure(width=width)
            w.grid(column=2*col+1, row=row, sticky=tk.E+tk.W)
            i = i + 1

        if len(cmds) % columns:
            tk.Label(f1, text=' ').grid(column=2*columns-2, row=rows-1, sticky=tk.E+tk.W)
            tk.Label(f1, text=' ').grid(column=2*columns-1, row=rows-1, sticky=tk.E+tk.W)

        for i in range(0, rows):
            f1.rowconfigure(i, weight=1)
        for i in range(0, 2*columns):
            f1.columnconfigure(i, weight=1)

        self.init_hex()
        return f1

    def regs_cb(self):
        if hasattr(self.data, 'menu'):
            delattr(self.data, 'menu')
        dlg = Regs(parent=self.root, data=self.data, dev=self.data.dev, standalone=False)
        dlg.do_modal()

