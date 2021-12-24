from tkinter import *
import tkinter as tk
import tkinter
import tkinter.font as font
from typing import Any
from modules import *
import os
import sys
import subprocess
from papa_pg import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def clear_me():
    text_department.set('')
    text_region.set('')
    text_district_region.set('')
    text_district_city.set('')
    text_city_type.set('')
    text_city.set('')
    text_street.set('')
    text_street_type.set('')
    text_hous.set('')
    text_post_index.set('')
    text_partner.set('')
    text_status.set('')
    text_register.set('')
    text_edrpou.set('')
    text_address.set('')
    text_partner_name.set('')
    text_id_terminal.set('')
    text_koatu.set('')
    text_tax_id.set('')
    text_koatu2.set('')



def get_windata():
    vec = [
        text_department.get(),
        text_region.get(),
        text_district_region.get(),
        text_district_city.get(),
        text_city_type.get(),
        text_city.get(),
        text_street.get(),
        text_street_type.get(),
        text_hous.get(),
        text_post_index.get(),
        text_partner.get(),
        text_status.get(),
        text_register.get(),
        text_edrpou.get(),
        text_address.get(),
        text_partner_name.get(),
        text_id_terminal.get(),
        text_koatu.get(),
        text_tax_id.get(),
        text_koatu2.get(),
    ]
    return vec

def edit_show():
    key = str(text_department.get()).strip()
    if not key:
        return
    clear_me()
    data = get_one_dep_data(key)[0]
    try:
        text_department.set(data[0])
        text_region.set(data[1])
        text_district_region.set(data[2]),
        text_district_city.set(data[3]),
        text_city_type.set(data[4]),
        text_city.set(data[5]),
        text_street.set(data[6]),
        text_street_type.set(data[7]),
        text_hous.set(data[8]),
        text_post_index.set(data[9]),
        text_partner.set(data[10]),
        text_status.set(data[11]),
        text_register.set(data[12]),
        text_edrpou.set(data[13]),
        text_address.set(data[14]),
        text_partner_name.set(data[15]),
        text_id_terminal.set(data[16]),
        text_koatu.set(data[17]),
        text_tax_id.set(data[18]),
        text_koatu2.set(data[19]),

        text_info.set(f'show {data[0]}')
    except:
        pass

def navi_forward():
    key = str(text_department.get()).strip()
    if not key:
        return
    clear_me()
    data = get_one_dep_data(next_dep(key))[0]
    try:
        text_department.set(data[0])
        text_region.set(data[1])
        text_district_region.set(data[2]),
        text_district_city.set(data[3]),
        text_city_type.set(data[4]),
        text_city.set(data[5]),
        text_street.set(data[6]),
        text_street_type.set(data[7]),
        text_hous.set(data[8]),
        text_post_index.set(data[9]),
        text_partner.set(data[10]),
        text_status.set(data[11]),
        text_register.set(data[12]),
        text_edrpou.set(data[13]),
        text_address.set(data[14]),
        text_partner_name.set(data[15]),
        text_id_terminal.set(data[16]),
        text_koatu.set(data[17]),
        text_tax_id.set(data[18]),
        text_koatu2.set(data[19]),

        text_info.set(f'show {data[0]}')
    except:
        pass

def navi_backward():
    key = str(text_department.get()).strip()
    if not key:
        return
    clear_me()
    data = get_one_dep_data(pred_dep(key))[0]
    try:
        text_department.set(data[0])
        text_region.set(data[1])
        text_district_region.set(data[2]),
        text_district_city.set(data[3]),
        text_city_type.set(data[4]),
        text_city.set(data[5]),
        text_street.set(data[6]),
        text_street_type.set(data[7]),
        text_hous.set(data[8]),
        text_post_index.set(data[9]),
        text_partner.set(data[10]),
        text_status.set(data[11]),
        text_register.set(data[12]),
        text_edrpou.set(data[13]),
        text_address.set(data[14]),
        text_partner_name.set(data[15]),
        text_id_terminal.set(data[16]),
        text_koatu.set(data[17]),
        text_tax_id.set(data[18]),
        text_koatu2.set(data[19]),

        text_info.set(f'show {data[0]}')
    except:
        pass

def edit_add():
    data = get_windata()
    try:
        refresh_one_dep(data)
        text_info.set(f'+ {data[0]}')
    except Exception as ex:
        #clear_me()
        text_info.set(str(ex))

def edit_delete():
    key = str(text_department.get()).strip()
    if not key:
        return
    try:
        del_dep(key)
        text_info.set(f'- {key}')
    except Exception as ex:
        text_info.set(str(ex) )
    

root = Tk()

data = []


font_size = 18
font_style = "Verdana"

main_menu = Menu(root)

edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="show", command=edit_show, font=(font_style, font_size))
edit_menu.add_command(label="add", command=edit_add, font=(font_style, font_size))
edit_menu.add_command(label="delete", command=edit_delete, font=(font_style, font_size))

navi_menu = Menu(main_menu, tearoff=0)
navi_menu.add_command(label=" -->> ", command=navi_forward, font=(font_style, font_size))
navi_menu.add_command(label=" <<-- ", command=navi_backward, font=(font_style, font_size))

main_menu.add_cascade(label="edit",
                     menu=edit_menu)
main_menu.add_cascade(label="navi",
                     menu=navi_menu)

buttonFont = font.Font(size=18)


button_find = tk.Button(text="найди", command=edit_show)
button_find.grid(row=1, column=0)
button_find['font'] = buttonFont

button_back = tk.Button(text="  <<  ", command=navi_backward)
button_back.grid(row=1, column=1)
button_back['font'] = buttonFont

button_forward = tk.Button(text="  >>  ", command=navi_forward)
button_forward.grid(row=1, column=2)
button_forward['font'] = buttonFont

button_add = tk.Button(text="добавь", command=edit_add, bg='lightcyan')
button_add.grid(row=1, column=3)
button_add['font'] = buttonFont

button_clear = tk.Button(text="очисти", command=clear_me, bg='lightgreen', )
button_clear.grid(row=1, column=4)
button_clear['font'] = buttonFont

button_delete = tk.Button(text="удали", command=edit_delete, bg='magenta')
button_delete.grid(row=12, column=3)
button_delete['font'] = buttonFont

tk.Button(text="bottom", bg='cyan').grid(row=22, column=4)
tk.Button(text="fringle_1", bg='cyan').grid(row=18, column=4)
tk.Button(text="fringle_2", bg='cyan').grid(row=16, column=4)


STEP = 1
PEREHOD = 15
WIGHT_ENTRY = 35


text_department = tk.StringVar()
label_department = tk.Label(text='department', font='Verdana 18', bg='cyan' )\
    .grid(row=3, column=0, sticky=E)
entry_department = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_department, foreground='blue')\
    .grid(row=3, column=1, columnspan=1, sticky=E+W)


text_region = tk.StringVar()
label_region = tk.Label(text='region', font='Verdana 18', bg='cyan')\
    .grid(row=4, column=0, sticky=E)
entry_region = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_region)\
    .grid(row=4, column=1, columnspan=1, sticky=E+W)
    
text_district_region = tk.StringVar()
label_district_region = tk.Label(text='district_region', font='Verdana 18', bg='cyan')\
    .grid(row=5, column=0, sticky=E)
entry_district_region = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_district_region)\
    .grid(row=5, column=1, columnspan=1, sticky=E+W)

text_district_city = tk.StringVar()
label_district_city = tk.Label(text='district_city', font='Verdana 18', bg='cyan')\
    .grid(row=6, column=0, sticky=E)
entry_district_city = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_district_city)\
    .grid(row=6, column=1, columnspan=1, sticky=E+W) 

text_city_type = tk.StringVar()
label_city_type = tk.Label(text='city_type', font='Verdana 18', bg='cyan')\
    .grid(row=7, column=0, sticky=E)
entry_city_type = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_city_type)\
    .grid(row=7, column=1, columnspan=1, sticky=E+W) 

text_city = tk.StringVar()
label_city = tk.Label(text='city', font='Verdana 18', bg='cyan')\
    .grid(row=8, column=0, sticky=E)
entry_city_type = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_city)\
    .grid(row=8, column=1, columnspan=1, sticky=E+W) 

text_street = tk.StringVar()
label_street = tk.Label(text='street', font='Verdana 18', bg='cyan')\
    .grid(row=9, column=0, sticky=E)
entry_street = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_street)\
    .grid(row=9, column=1, columnspan=1, sticky=E+W) 

text_street_type = tk.StringVar()
label_street_type = tk.Label(text='street_type', font='Verdana 18', bg='cyan')\
    .grid(row=10, column=0, sticky=E)
entry_street_type = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_street_type)\
    .grid(row=10, column=1, columnspan=1, sticky=E+W) 

text_hous = tk.StringVar()
label_hous = tk.Label(text='hous', font='Verdana 18', bg='cyan')\
    .grid(row=11, column=0, sticky=E)
entry_hous = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_hous)\
    .grid(row=11, column=1, columnspan=1, sticky=E+W) 

text_post_index = tk.StringVar()
label_post_index = tk.Label(text='post_index', font='Verdana 18', bg='cyan')\
    .grid(row=12, column=0, sticky=E)
entry_post_index = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_post_index)\
    .grid(row=12, column=1, columnspan=1, sticky=E+W) 

text_partner = tk.StringVar()
label_partner = tk.Label(text='partner', font='Verdana 18', bg='cyan')\
    .grid(row=13, column=0, sticky=E)
entry_partner = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_partner)\
    .grid(row=13, column=1, columnspan=1, sticky=E+W) 

text_status = tk.StringVar()
label_status = tk.Label(text='status', font='Verdana 18', bg='cyan')\
    .grid(row=14, column=0, sticky=E)
entry_status = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_status)\
    .grid(row=14, column=1, columnspan=1, sticky=E+W) 

text_register = tk.StringVar()
label_register = tk.Label(text='register', font='Verdana 18', bg='cyan')\
    .grid(row=15, column=0, sticky=E)
entry_register = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_register)\
    .grid(row=15, column=1, columnspan=1, sticky=E+W) 

text_edrpou = tk.StringVar()
label_edrpou = tk.Label(text='edrpou', font='Verdana 18', bg='cyan')\
    .grid(row=16, column=0, sticky=E)
entry_edrpou = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_edrpou)\
    .grid(row=16, column=1, columnspan=1, sticky=E+W) 

text_address = tk.StringVar()
label_address = tk.Label(text='address', font='Verdana 18', bg='cyan')\
    .grid(row=17, column=0, sticky=E)
entry_address = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_address)\
    .grid(row=17, column=1, columnspan=4, sticky=E+W) 

#______________________________________

text_partner_name = tk.StringVar()
label_partner_name = tk.Label(text='partner_name', font='Verdana 18', bg='cyan')\
    .grid(row=3, column=2, sticky=E)
entry_partner_name = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_partner_name)\
    .grid(row=3, column=3, columnspan=1, sticky=E+W) 

text_id_terminal = tk.StringVar()
label_id_terminal = tk.Label(text='id_terminal', font='Verdana 18', bg='cyan')\
    .grid(row=4, column=2, sticky=E)
entry_id_terminal = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_id_terminal)\
    .grid(row=4, column=3, columnspan=1, sticky=E+W) 

text_koatu = tk.StringVar()
label_koatu = tk.Label(text='koatu', font='Verdana 18', bg='cyan')\
    .grid(row=5, column=2, sticky=E)
entry_koatu = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_koatu)\
    .grid(row=5, column=3, columnspan=1, sticky=E+W) 

text_tax_id = tk.StringVar()
label_tax_id = tk.Label(text='tax_id', font='Verdana 18', bg='cyan')\
    .grid(row=6, column=2, sticky=E)
entry_tax_id = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_tax_id)\
    .grid(row=6, column=3, columnspan=1, sticky=E+W) 

text_koatu2 = tk.StringVar()
label_koatu2 = tk.Label(text='koatu2', font='Verdana 18', bg='cyan')\
    .grid(row=7, column=2, sticky=E)
entry_koatu2 = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_koatu2)\
    .grid(row=7, column=3, columnspan=1, sticky=E+W) 

#___________________________________________________

#text_box = Text(font=(font_style, font_size), foreground='black', background='cyan')
#text_box.grid(row=19, column=1, columnspan=3, rowspan=1)

text_info = tk.StringVar()
entry_info = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), foreground='blue', textvariable=text_info)\
    .grid(row=19, column=1, columnspan=3, sticky=E+W) 

root.config(menu=main_menu) 
root["bg"] = "cyan"
root.mainloop()