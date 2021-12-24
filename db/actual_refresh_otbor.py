import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *



otbor = select_table('otbor')

"""
refresh dep
"""
for line in otbor:
    dep = line[1]
    try:
        act_refresh_one_dep(dep)
        say(f'+ actual {dep}')
    except Exception as ex:
        alarm(f'+ {ex}\n')

