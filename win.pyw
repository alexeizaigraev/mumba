from tkinter import *
from typing import Any

from modules import *
from papa_pg import *


def clear_me():
    text_box.delete(1.0, END)

def say(txt):
    text_box.delete(1.0, END)
    text_box.insert(1.0, str(txt))


def edit_show():
    key_item = str(text_box.get(1.0, END)).strip()
    clear_me()
    try:
        text_box.insert(1.0, mk_txt(key_item))
    except:
        pass

def edit_show_next_dep():
    txt = str(text_box.get(1.0, END)).strip()
    if ';' in txt:
        key_item = txt.split('\n')[0].split(';')[1]
    else:
        key_item = txt.strip()
    new_text = mk_txt(next_dep(key_item))
    clear_me()
    text_box.insert(1.0, new_text)

def edit_show_pred_dep():
    txt = str(text_box.get(1.0, END)).strip()
    if ';' in txt:
        key_item = txt.split('\n')[0].split(';')[1]
    else:
        key_item = txt.strip()
    new_text = mk_txt(pred_dep(key_item))
    clear_me()
    text_box.insert(1.0, new_text)

def edit_show_next_term():
    txt = str(text_box.get(1.0, END)).strip()
    if ';' in txt:
        key_item = txt.split('\n')[1].split(';')[1]
    else:
        key_item = txt.strip()
    new_text = mk_txt(next_term(key_item))
    clear_me()
    text_box.insert(1.0, new_text)

def edit_show_pred_term():
    txt = str(text_box.get(1.0, END)).strip()
    if ';' in txt:
        key_item = txt.split('\n')[1].split(';')[1]
    else:
        key_item = txt.strip()
    new_text = mk_txt(pred_term(key_item))
    clear_me()
    text_box.insert(1.0, new_text)
  



def edit_add_dep():
    txt = text_box.get(1.0, END).strip()
    vec = get_data_from_textbox(txt)
    try:
        refresh_one_dep(vec)
        say(f'{vec[0]}')
    except Exception as ex:
        clear_me()
        say(ex)

def edit_add_term():
    txt = text_box.get(1.0, END).strip()
    vec = get_data_from_textbox(txt)
    refresh_one_term(vec)
    try:
        refresh_one_term(vec)
        say(f'{vec[1]}')
    except Exception as ex:
        pass
        #clear_me()
        #say(vec)

def delete_del_term():
    txt = text_box.get(1.0, END).strip()
    term = get_key_from_textbox(txt)
    try:
        del_term(term)
        say(f'- {term}')
    except Exception as ex:
        say(ex)

def delete_del_dep():
    txt = text_box.get(1.0, END).strip()
    dep = get_key_from_textbox(txt)
    try:
        del_dep(dep)
        say(f'- {dep}')
    except Exception as ex:
        say(ex) 


font_size = 18
font_style = "Verdana"

root = Tk()
main_menu = Menu(root)

show_menu = Menu(main_menu, tearoff=0)
show_menu.add_command(label="show", command=edit_show, font=(font_style, font_size))



font_size = 18
#term_size = len(file_to_arr(IN_DATA_PATH + "terminals.csv")[0])
#dep_size = len(file_to_arr(IN_DATA_PATH + "departments.csv")[0])



show_menu = Menu(main_menu, tearoff=0)
show_menu.add_command(label="show", command=edit_show, font=(font_style, font_size))
show_menu.add_command(label="next_dep", command=edit_show_next_dep, font=(font_style, font_size))
show_menu.add_command(label="pred_dep", command=edit_show_pred_dep, font=(font_style, font_size))
show_menu.add_command(label="next_term", command=edit_show_next_term, font=(font_style, font_size))
show_menu.add_command(label="pred_term", command=edit_show_pred_term, font=(font_style, font_size))
show_menu.add_command(label="clear", command=clear_me, font=(font_style, font_size))

edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="show", command=edit_show, font=(font_style, font_size))
edit_menu.add_command(label="add_dep", command=edit_add_dep, font=(font_style, font_size))
edit_menu.add_command(label="add_term", command=edit_add_term, font=(font_style, font_size))
edit_menu.add_command(label="clear", command=clear_me, font=(font_style, font_size))

delete_menu = Menu(main_menu, tearoff=0)
delete_menu.add_command(label="show", command=edit_show, font=(font_style, font_size))
delete_menu.add_command(label="del_dep", command=delete_del_dep, font=(font_style, font_size))
delete_menu.add_command(label="del_term", command=delete_del_term, font=(font_style, font_size))
delete_menu.add_command(label="clear", command=clear_me, font=(font_style, font_size))


main_menu.add_cascade(label="show",
                     menu=show_menu)
main_menu.add_cascade(label="edit",
                     menu=edit_menu)
main_menu.add_cascade(label="delete",
                     menu=delete_menu)


text_box = Text(font=(font_style, font_size), foreground='black', background='cyan')
text_box.pack(side=LEFT, fill=BOTH)

root.config(menu=main_menu)

f = Frame()
f.pack(side=LEFT, padx=10)

root["bg"] = "cyan"
root.mainloop()