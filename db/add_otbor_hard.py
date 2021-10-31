import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

init()
head = 'term;dep\n'
out = head

all_term = get_terminals_list()

p_cyan(' Terminals:\n')
choise = input(' -> ')

terms = []
if ' ' in choise:
    terms = choise.split(' ')
else:
    terms.append(choise)

for term in terms:
    if term not in all_term:
        p_red(term)
    dep = term[:7]
    out += term + ';' + dep + '\n'

p_green('\n' + out + '\n')
text_to_file(out, IN_DATA_PATH + 'otbor.csv')
insert_all_otbor()



