import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *

from papa_pg import get_data

def doc_papa_back(query, head, ofName):
    now = now_date_log()
    out_path = f'{GDRIVE_PATH}PG_BACKUP/{now}_{ofName}'
    info = ''
    if head:
        info = head + '\n'
    data = get_data(query)
    count = 0;
    for line in data:
        count += 1
        info += f'{count};{";".join(line)}\n'

    info = info.replace(" 0:00:00", "").replace("null", "")
    print()
    text_to_file(info, out_path)
    

query = """SELECT department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2 FROM public.departments;"""
head = "num;department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner name;id_terminal;koatu;tax_id;koatu2"
fName = "departments.csv"
doc_papa_back(query, head, fName)

query = "SELECT * FROM public.terminals;"
head = "num;department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner name;id_terminal;koatu;tax_id;koatu2"
fName = "terminals.csv"
doc_papa_back(query, head, fName)
   
 