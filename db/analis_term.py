import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data

def base_data():
    q = """SELECT terminals.termial, 
departmentsnew.department, departmentsnew.street, 
departmentsnew.hous, departmentsnew.address
FROM public.terminals, public.departmentsnew
WHERE terminals.department = departmentsnew.department
AND departmentsnew.partner != 'intime'
AND terminals.model != 'УЕ РККС'
AND terminals.model != 'УЕРККС'"""
    return get_data(q)


info = ''
count = 0
termData = file_to_arr(IN_DATA_PATH + "terminals_sverka.csv")
data = base_data()
for item in data:
    termBase = item[0]
    depBase = item[1]
    streetBase = item[2]
    housBase = item[3]
    #addBase = item[4]

    for termLine in termData:
        if termLine[0] == termBase and 'tru' in termLine[1]:
            if strInBoth(termLine[2], streetBase) and strInBoth(termLine[2], housBase):
                continue
            else:
                info += f'{ termLine[0]}\nтерминал: \t{termLine[2]}\n_____база: \t{streetBase} {housBase}\n\n'
                count += 1
                
info += f'\n\tошибок {count}\n\n{info}'
save_and_show(info, 'info.txt')