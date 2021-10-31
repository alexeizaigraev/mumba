# -*- coding: utf-8 -*-
""" Набор модулей """
import os
import shutil
from pathlib import Path
import datetime
from sys import platform


from colorama import Fore, Style, init

def my_clear():
    if platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def sos(err, fact):
    """Сообщение об ошибке - запрос ввода - меню"""
    print('>> Err ', err, fact)
    input('## Press Any Key')
    input()
    os.system(PYTHON_NAME + ' main.py')

def alarm(err, fact):
    """Сообщение об ошибке - без прерывания программы"""
    print('>> Err ', err, fact)

def file_to_arr(path):
    """ Читает файл в массив. имя файла: path """
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            if ";" in line:
                b.append(line.strip().split(";"))
            else:
                b.append(line.strip())
    return b

def file_to_gen(path):
    """ Читает файл в массив. имя файла: path """
    for line in open(path, 'r', encoding="UTF-8"):
        if ";" in line:
            b = line.strip().split(";")
        else:
            b = line.strip()
        yield b

def file_to_vec(path):
    """ Читает файл в массив. имя файла: path """
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            b.append(line.strip())
    return b

def file_to_dict_one(fname, num_col):
    h = dict()
    with open(fname, 'r', encoding="UTF-8") as file:
        for line in file:
            split_line = line.strip().split(";")
            h[split_line[0]] = split_line[num_col]
    return h


def arr_to_text(arr):
    text = ''
    for v in arr:
        text += ';'.join(v) + "\n"
    return text

def file_to_text(fname):
    text = None
    with open(fname, 'r', encoding="UTF-8") as file:
        text = file.read()
    return text

def text_to_file(b, fname):
    """Записывает текст b в файл с именем fname"""
    with open(fname, 'w', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        p_magenta('emptty ' + fname)
    else:
        p_blue(f'\n {fname}\n')

def text_add_file(b, fname):
    """Записывает текст b в файл с именем fname"""
    with open(fname, 'a', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        p_magenta('clear ' + fname)
    else:
        p_blue(f'\n\t add to: {fname}\n')


def save_and_show(text, fname):
    text_to_file(text, fname)
    open_name = 'notepad.exe ' + fname
    os.system(open_name)


def arr_to_file(b, fname):
    """Записывает массив b в файл с именем fname"""
    with open(fname, 'w', encoding="UTF-8") as file:
        for bb in b:
            file.write(";".join(bb) + "\n")
    p_blue(f'\n\t{fname}\n')
    
    
def text_to_file_cp1251(b, fname):
    """Записывает text b в файл с именем fname"""
    with open(fname, 'w', encoding="cp1251") as file:
        file.write(b)
    p_green(fname)

def now_date_kabinet():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{d}{m}{y}'

def now_date_log():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{d}.{m}.{y}'

def mk_natasha():
    sign = 'Відділення № '
    b = ['1',]
    with open(IN_DATA_PATH + 'natasha.csv', 'r', encoding="UTF-8") as file:
        for line_str in file:
            line = line_str.strip().split(';')
            for unit in line:
                if sign in unit:
                    el = unit.replace(sign, '').strip()
                    b.append(el)
    return set(b)

def comon_data_dict(col_key_num):
    h = dict()
    with open(COMON_DATA_PATH, 'r', encoding="UTF-8") as file:
        for line in file:
            vec = line.split(';')
            key = vec[0]
            h[key] = vec[col_key_num]
    return h

def dir_kabinet(self):
        return file_to_arr(CONFIG_PATH + 'ConfigKabinetPath.txt')[0]


def mover(old_name, new_name):
    try:
        shutil.move(old_name, new_name)
        p_blue(new_name)
    except:
        p_red('>> err', old_name)

def coper(old_name, new_name):
    try:
        shutil.copy(old_name, new_name)
        p_blue(new_name)
    except:
        p_red('>> err', old_name)




def p_red(text):
    init()
    print(Fore.RED + text)
def p_green(text):
    init()
    print(Fore.GREEN + text)
def p_yellow(text):
    init()
    print(Fore.YELLOW + text)
def p_cyan(text):
    init()
    print(Fore.CYAN + text)
def p_magenta(text):
    init()
    print(Fore.MAGENTA + text)
def p_blue(text):
    init()
    print(Fore.LIGHTBLUE_EX + text)
    

def ask(vec):
    os.system(COM_CLEAR)
    print('\n\n')
    for i in range(len(vec)):
        p_green(f'\t{i} {vec[i]}')

    print('\n\n\t-> ', end = '')
    choise = input()
    return vec[int(choise)]
  


DATA_PATH = file_to_arr('Config/ConfigDataPath.txt')[0]
IN_DATA_PATH = DATA_PATH + 'InData/'
OUT_DATA_PATH = DATA_PATH + 'OutData/'
CONFIG_PATH = DATA_PATH + 'Config/'
COMON_DATA_PATH = CONFIG_PATH + 'comon_data.csv'
CONFIG_DIR_PATH = DATA_PATH + 'ConfigDir/'
KABINET_DIR = file_to_arr(CONFIG_PATH + 'ConfigKabinetPath.txt')[0]

GDRIVE_PATH = file_to_arr(CONFIG_PATH + 'ConfigGdrivePath.txt')[0]

if platform == 'linux':
    py_prefix = 'python3'
    com_clear = 'clear'
else:
    py_prefix = 'python'
    com_clear = 'cls'

COM_CLEAR = com_clear
PYTHON_NAME = py_prefix
