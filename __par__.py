########################## THE TOON LAND PROJECT ##########################
# Filename: __par__.py
# Created by: Cody/Fd Green Cat Fd (January 30th, 2013)
####
# Description:
#
# Used in loading all of Toon Land's code into our private namespace. Do not modify.
####

__filebase__ = 'TL_Cookies'

import os, imp
filepaths = [os.path.join(root, filename)
             for root, folders, files in os.walk('%s\\toonland' % __filebase__)
             for filename in files
             if (filename.endswith('.py')) and (root != '%s\\toonland\\security' % __filebase__)
             if not filename.startswith('_')]
modules = {}
for filepath in filepaths:
    moduleName = filepath.split('\\')[-1].split('.', 1)[0]
    exec('%s = imp.new_module(\'%s\')' % (moduleName, moduleName))
    exec('exec(\'from __main__ import *\', %s.__dict__)' % moduleName)
    exec('execfile(\'%s\', %s.__dict__)' % (filepath.replace('\\', '/'), moduleName))
    exec('modules[\'%s\'] = %s' % (moduleName, moduleName))
for module in modules:
    _modules = modules.copy()
    del _modules[module]
    exec('%s.__dict__.update(_modules)' % module)
    exec('%s.__dict__.update({\'__filebase__\':\'%s\', \'HackerCrypt\':HackerCrypt})' % (
         module, __filebase__))
execfile('%s\\toonland\\__init__.py' % __filebase__)