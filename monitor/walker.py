# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil

def dir_in_walk():
    return file_to_arr(CONFIG_PATH + 'ConfigRaskladPath.txt')[0]

def dir_out_walk():
        return file_to_arr(CONFIG_PATH + 'ConfigGdrivePath.txt')[0]
    
def show():
    a = os.listdir(dir_in_walk())
    for aa in a:
        p_blue(aa)
    if not a:
        p_cyan('\nnothing show\n')


def mk_agents():
    return file_to_dict_one(COMON_DATA_PATH, 3)

def mover():
    agents = mk_agents()
    a = os.listdir(dir_in_walk())
    if len(a) < 1:
            p_magenta('\n\tno files found\n')
    old_dir = dir_in_walk()
    for aa in a:
        fname = os.path.abspath(aa).split(os.sep)[-1]
        old_fname = os.path.join(old_dir, fname)
        folder = fname[:7]
        key = fname[:3]
        new_root = os.path.join(dir_out_walk(), agents[key])
        new_dir = os.path.join(new_root, folder)
        new_fname = os.path.join(new_dir, fname)
        backup_fname = 'R:/DRM/ЗАИГРАЕВ ОБМЕН АРХИВ/Архив/' + fname
        if not os.path.exists(new_dir):
            try:
                os.mkdir(new_dir)
                p_blue('\tnew folder')
            except:
                p_red(new_dir)
        try:
            shutil.copy(old_fname, backup_fname)
        except:
            pass
        
        try:
            shutil.move(old_fname, new_fname)
            p_cyan(new_fname)
        except:
            p_red(new_fname)
        
        
        
mover()

p_green('\n\n\nОстаток в rasklad:\n')
show()

