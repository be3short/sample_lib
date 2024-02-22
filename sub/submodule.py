
#from __lib__.module import ModuleClass


import __lib__
from __lib__.sub.subsub import subsubmodule
from ..module import ModuleClass

class SubModuleClass:
    def __init__(self):
        self.name = SubModuleClass.__name__