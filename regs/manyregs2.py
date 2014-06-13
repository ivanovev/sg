
import tkinter as tk
import tkinter.ttk as ttk
from collections import OrderedDict as OD
import pdb

from .manyregs import Manyregs

class Manyregs2(Manyregs):
    def __init__(self, dev, data, parent=None):
        Manyregs.__init__(self, dev=dev, data=data, parent=parent)

    def init_custom_layout(self):
        self.data.select(0)
        self.init_groups()
        self.init_bottom_frame()

    def init_groups(self):
        gg = self.data.groups
        self.tabs = ttk.Notebook(self.fcalc)
        self.tabs.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        for g in gg:
            f1 = self.init_calc_frame(g)
            self.tabs.add(f1, text=g)
            self.data[g].tabid = self.tabs.tabs()[-1]
        self.data.bind_tab_cb(self.tabs, self.update_bottom_frame)

    def init_calc_frame(self, g):
        f1 = tk.Frame(self.tabs)
        self.init_calc(f1, 'calc', g)
        return f1

    def update_bottom_frame(self, *args):
        p = self.data.cmds
        if hasattr(self, 'fa'):
            self.fa.pack_forget()
            delattr(self, 'fa')
        self.fa = self.data.get_attribute(p.name, 'f', lambda: self.init_bottom_hex(p.name))
        self.fa.pack(fill=tk.BOTH, expand=1, side=tk.BOTTOM)

