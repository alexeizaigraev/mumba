import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

refresh_table_actual()
p_yellow('\nrefresh_all_deps_new\n')
