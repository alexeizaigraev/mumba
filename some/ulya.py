# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 


from modules import *
#from papa import *
from papa_pg import *
from datetime import datetime, date

def get_ula_data():
    query = f'''SELECT department, address FROM departmentsnew
ORDER BY partner'''
    return get_data(query)

def find_adr(dep):
    for line in spr:
        if line[0] == dep:
            return line[1]
    return ''


out = '№ з/п;Працівник;Дата прийняття;Підрозділ організації;Підрозділ організації.Адреса;Cтавка;;;;;;;;\n'
spr = get_ula_data()
data = file_to_arr(IN_DATA_PATH + 'ulya.csv')
for line in data:
    if 'Відділення' in line[3]:
        dep = line[3].rstrip()[-7:]
        adr = find_adr(dep)
        if adr:
            line[4] = adr
        out += ';'.join(line) + '\n'

fname = OUT_DATA_PATH + 'UlyaOut.csv'
#text_to_file(out, fname)
save_and_show(out, fname)

