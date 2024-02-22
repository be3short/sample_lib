import importlib
import sys

import module
print(module.ModuleClass)

sys.path.append("/Users/beshort/Documents/GitHub")
import sample_lib




'''
spec = importlib.util.spec_from_file_location('submodule', '/Users/beshort/Documents/GitHub/sample_lib/sub/submodule.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(module)
'''

