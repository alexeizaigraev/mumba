import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

init()
head = 'term;dep\n'
out = head

all_deps = get_departments_list()

p_cyan(' Departments list:\n\n')
choise = input(' -> ')

deps = []
if ' ' in choise:
    deps = choise.split(' ')
else:
    deps.append(choise)

for dep in deps:
    if dep not in all_deps:
        p_red(dep)
    term = dep + '1'
    out += term + ';' + dep + '\n'

p_green('\n' + out + '\n')
text_to_file(out, IN_DATA_PATH + 'otbor.csv')
insert_all_otbor()



