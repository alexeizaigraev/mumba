import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

init()
head = 'term;dep\n'
out = head

#all_term = get_terminals_list()

p_cyan(' Terminals:\nnext for first may be only hvost\n')
choise = input(' -> ')

terms = []
serials = []
if ' ' in choise:
    serials = choise.split(' ')
else:
    serials.append(choise)

for serial in serials:
    try:
        term = get_term_by_serial(serial)
        p_yellow(term)
        dep = term[:7]
        out += term + ';' + dep + '\n'
    except Exception as ex:
        p_red(ex)

p_green('\n' + out + '\n')
text_to_file(out, IN_DATA_PATH + 'otbor.csv')
insert_all_otbor()



