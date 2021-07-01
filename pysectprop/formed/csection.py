from py2md.classes import MDTable
from ..general.generalsection import GeneralSection
from .. import config

class CSection(GeneralSection):
    r"""
    C-Channel section property calculation class.
    
    3 section elements - Upper Flange, Lower Flange and Web.
    8 nodal points can be manually defined.     
    
    Attributes
    ----------
    hw : Real
        Height of Web.
    wuf : Real
        Upper/Top Flange Width.
    wlf : Real
        Lower/Bot. Flange Width.
    ts : Real-Single Val or List [Lower Flange Thickness, Web Thickness, Upper Flange Thickness]
        Specifies section thickness, applied to all 3 section elements.
    rm : Real
        Specifies section fillet radius to all nodal points. Zero[0] if larger than half section thickness.
        ! Use only if single/constant ts value is specfied.
        
    Section Properties: Real
        Stores Additional Engineering Section Property Data:
            - Total Area-A | Ay | Az | Ayy
            - cy | cz 
            - Iyy | Izz | Iyz
            - Rotation Angle-thetap | Iyp | Izp

    Methods
    -------
    plot():
        Plots section geometry.
    
    """
       
    hw = None
    wuf = None
    wlf = None
    ts = None
    rm = None
    def __init__(self, hw: float, wuf: float, wlf: float, ts,
                 rm: float, label: str=None):
        self.hw = hw
        self.wuf = wuf
        self.wlf = wlf
        try:
            ts
        except TypeError:
            ts = [ts]
        if isinstance(ts, list):
            self.ts1 = ts[0] # Lower Flange Thickness
            self.ts2 = ts[1] # Web Thickness
            self.ts3 = ts[2] # Upper Flange Thickness
        else:
            self.ts1 = ts # Lower Flange Thickness
            self.ts2 = ts # Web Thickness
            self.ts3 = ts # Upper Flange Thickness
        self.rm = rm
        y = [0.0, self.wlf, self.wlf, self.ts2, self.ts2, self.wuf, self.wuf, 0.0]
        z = [0.0, 0.0, self.ts1, self.ts1, self.hw-self.ts3, self.hw-self.ts3, self.hw, self.hw]
        if self.rm < self.ts1/2:
            r = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        else:
            ri = self.rm-self.ts1/2
            ro = self.rm+self.ts1/2
            r = [ro, 0.0, 0.0, ri, ri, 0.0, 0.0, ro]
        super().__init__(y, z, r, label=label)
    def __repr__(self):
        if self.label is None:
            outstr = '<C-Section>'
        else:
            outstr = f'<C-Section {self.label:s}>'
        return outstr
    def __str__(self):
        mdstr = self.section_heading('C-Section')
        table = MDTable()
        table.add_column(f'h<sub>w</sub> ({config.lunit:s})', config.l1frm, data=[self.hw])
        table.add_column(f'w<sub>uf</sub> ({config.lunit:s})', config.l1frm, data=[self.wuf])
        table.add_column(f'w<sub>lf</sub> ({config.lunit:s})', config.l1frm, data=[self.wlf])
        table.add_column(f't<sub>s</sub> ({config.lunit:s})', config.l1frm, data=[self.ts1])
        table.add_column(f'r<sub>m</sub> ({config.lunit:s})', config.l1frm, data=[self.rm])
        mdstr += str(table)
        mdstr += self.section_properties()
        return mdstr
    def _repr_markdown_(self):
        return self.__str__()   
