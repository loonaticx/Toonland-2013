########################## THE TOON LAND PROJECT ##########################
# Filename: __init__.py
# Created by: Cody/Fd Green Cat Fd (January 31st, 2013)
####
# Description:
#
# Initializes the Toon Land modification. Do not modify.
####

priv_namespace = {'__version__':'v0.1.3.3'}
exec('from __main__ import *', priv_namespace)

execfile('TL_Cookies\\toonland\\security\\HackerCrypt.py', priv_namespace)
exec('HackerCrypt = HackerCrypt()', priv_namespace)

execfile('TL_Cookies\\__par__.py', priv_namespace)

del priv_namespace