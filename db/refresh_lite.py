import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from papa_sq import *
import os

try:
    os.system('python runsharp_lite.py')
except Exception as ex:
    p_red(ex)

verb = True

insert_all_terms()
insert_all_deps()
insert_all_otbor()
