import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

def serials_by_hvost(hvost):
    rez = []
    hvost_len = len(hvost)
    for serial in all_serials:
        if hvost in serial[len(serial) - hvost_len - 1 : ]:
            rez.append(serial)
    return rez

init()
head = 'term;dep\n'
out = head

all_serials = get_serial_list()

p_cyan(' Terminals:\nnext for first may be only hvost\n')
choise = input(' -> ')

terms = []
hvosts = []
if ' ' in choise:
    hvosts = choise.split(' ')
else:
    hvosts.append(choise)

for hvost in hvosts:
    try:
        serials = serials_by_hvost(hvost)
        if serials:
            for serial in serials:
                term = get_term_by_serial(serial)
                p_cyan(term)
                dep = term[:7]
                out += term + ';' + dep + '\n'
    except Exception as ex:
        p_red(ex)

p_green('\n' + out + '\n')
text_to_file(out, IN_DATA_PATH + 'otbor.csv')
insert_all_otbor()



