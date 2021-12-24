import os
import sys
import shutil

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
#from papa_pg import get_departments_list



def priznak_in_name(name):
    for priznak in priznaks:
        if priznak in name.lower():
            return True
    return False

def get_files():
    send = []
    for ag_folder in ag_folders:
        path = os.path.join(GDRIVE_PATH, ag_folder)
        for top, dirs, files in os.walk(path):
            for nm in files:
                name_full = os.path.join(top, nm)
                sname = name_full.split(os.sep)
                fname_short = sname[-1]
                dep = sname[-2]
                
                if priznak_in_name(name_full):
                    new_name = '_'.join([dep, fname_short])
                    new_name_full = os.path.join(outpath, new_name)
                    try:
                        if choise == 'move':
                            shutil.move(name_full, new_name_full)
                        else:
                            shutil.copy(name_full, new_name_full)
                        if dep not in send:
                            send.append(dep)
                        print(choise, new_name_full)
                    except Exception as ex:
                        print(ex)
    return send

def mk_rezdict():
    sum = 0
    h = dict() 
    a = os.listdir(outpath)
    for fname in a:
        try:
            sum += 1
            dep = fname[:7]
            if dep in h:
                h[dep] += 1
            else:
                h[dep] = 1
        except:
            pass
    return h, sum
        

def mk_aq_fold():
    return file_to_dict_one(COMON_DATA_PATH, 3)

def mk_rezdictpartner():
    f_fold = mk_aq_fold()
    h = dict() 
    a = os.listdir(outpath)
    for fname in a:
        try:
            dep = fname[:7]
            ag_key = dep[:3]
            fold = f_fold[ag_key]
            if fold in h:
                h[fold] += 1
            else:
                h[fold] = 1
        except:
            pass
    return h
        

quest = ['copy', 'move']

choise = ask(quest)

print(f'{choise=}')

priznaks = ('foto', 'photo', 'фото',)
outpath = DATA_PATH + 'gnetz/'
ag_folders = comon_data_list(3)

get_files()

rez_dict, sum = mk_rezdict()

info = ''
rezdictpartner  = mk_rezdictpartner()
for key in rezdictpartner:
    str = f'{key} {rezdictpartner[key]}'
    print(str)
    info += str + '\n'


info += (f'\ndepatrtments: {len(rez_dict)}\nfiles: {sum}\n\n')


"""
for key in rez_dict:
    info += f'{key} {rez_dict[key]}\n'



info += '\n\nno send:\n'

all_deps = get_departments_list()

bed = [dep for dep in all_deps if dep not in rez_dict]
bed_text = '\n'.join(bed)
info += f'\nno send {len(bed)}:\n\n{bed_text}'

"""

info += f'saved in {outpath}\n\n'
print(f'saved in {outpath}\n\n')

save_and_show(info, 'info.txt')