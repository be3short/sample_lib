import inspect
import sys

class ModuleClass:
    class ModuleSubClass:
        def __init__(self):
            self.name = ModuleClass.__name__

    def __init__(self):
        self.name = ModuleClass.__name__




def module_func():
    print("module func: {}".format(module_func.__module__))