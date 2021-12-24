import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

def verify(fufu, act):
    t = ''
    col_num = 14
    if fufu[col_num] != act[col_num]:
            s = f'verify {fufu[0]}\ndep {fufu[col_num]}\ndepNew {act[col_num]}\n\n'
            t += s
            #print(s)
    return(t)


info = ''
futur_all = get_all_dep_data()
actual_all = get_all_dep_new_data()

futur = set(get_departments_list())
actual = set(get_departments_new_list())


print(f'{futur - actual = }')
info += f'{futur - actual = }\n\n'
print(f'{actual - futur = }')
info += f'{actual - futur = }\n\n'
info += '\n\n'



info += '\n\nverify:\n'

for fufu in futur_all:
    for act in actual_all:
        if fufu[0] == act[0]:
            rez = verify(fufu, act)
            if rez:
                info += rez

save_and_show(info, 'info.txt')
