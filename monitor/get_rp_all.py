# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
#from papa_pg import get_otbor_deps

def ag_folders():
    outlist = []
    for folder in comon_data_dict(3).values():
        if folder != 'nodata':
            outlist.append(folder)
    return outlist

def col_key_pg(vec):
    os.system(COM_CLEAR)
    listkey = vec
    for i in range(len(listkey)):
        if not listkey[i]:
            continue
        p_cyan(f'\t{i} {listkey[i]}')
    
    #print('')
    print('\n\n\n -> ', end = '')
    choise = int(input())
    os.system(COM_CLEAR)
    
    return listkey[choise]

def get_all_fnames():
    out = []
    folders = os.listdir(GDRIVE_PATH + ag_folder)
    for folder in folders:
        try:
            work_dir = GDRIVE_PATH + ag_folder + '/' + folder
            fnames = os.listdir(work_dir)
            for fname in fnames:
                if 'RP' not in fname:
                    continue
                
                fname_full = work_dir + '/' + fname
                out.append(fname_full)
        except:
            pass
        
    return out


def short_name(name):
    return name.split('/')[-1]


init()
sum = 0
out_path = KABINET_DIR
old = os.listdir(out_path)
for fname in old:
    try:
        if '.pdf' in fname:
            os.remove(out_path + fname)
    except:
        print('err remove', fname)


ag_folder = col_key_pg(ag_folders())
print(f'\n{ag_folder}\n')

a = get_all_fnames()
for aa in a:
    old_name = aa
    new_name = out_path + short_name(aa)
    sum += 1
    coper(old_name, new_name)


print(f'\n\t{sum=}\n')
