import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

head = 'term;dep\n'
out = head
p_cyan(' Dep: From To\nfiniish may be only hvost\n\n')
choise = input(' -> ')

if ' ' in choise:
    start, finish = choise.split(' ')
    if len(start) == len(finish):
        start, finish = int(start), int(finish) + 1
    else:
        finish = int( start[: (len(start) - len(finish))] + finish ) + 1
        start = int(start)

else:
    start = int(choise)
    finish = start + 1

for x in range(start, finish):
    dep, term = str(x), str(x*10+1)
    out += term + ';' + dep + '\n'

p_green('\n' + out + '\n')
text_to_file(out, IN_DATA_PATH + 'otbor.csv')
insert_all_otbor()
