
import os
import sys
from modules import *
#from tech import *
import datetime
import platform

#from colorama import Fore, Style, init


def mk_menu(kv, numm_color):
    #os.system(COM_CLEAR)
    print()
    init()
    my_keys = list(kv.keys())
    num = 0
    print()
    for point in kv:
        num += 1
        if num != numm_color:
            p_blue(f'\t{num} {point}')
        else:
            p_green(f'\t{num} {point}')

    choice = '99'
    while choice != '0':
        print(f'{Fore.GREEN}\n\n -> ', end='')
        choice = input()
        if '' == choice:
            menu_main()
        elif 0 < int(choice) < len(my_keys) + 1:
            comand = PYTHON_NAME + ' ' + kv[my_keys[int(choice)-1]] + '.py'
            os.system(COM_CLEAR)
            os.system(comand)
            mk_menu(kv, numm_color)
        elif '0' == choice:
            sys.exit()
        else:
            print(f'{Fore.RED} >> wrong choice!')

def mk_menu_win(kv, numm_color):
    #os.system(COM_CLEAR)
    print()
    init()
    my_keys = list(kv.keys())
    num = 0
    print()
    for point in kv:
        num += 1
        if num != numm_color:
            p_blue(f'\t{num} {point}')
        else:
            p_green(f'\t{num} {point}')

    choice = '99'
    while choice != '0':
        print(f'{Fore.GREEN}\n\n -> ', end='')
        choice = input()
        if '' == choice:
            menu_main()
        elif 0 < int(choice) < len(my_keys) + 1:
            comand = PYTHON_NAME + ' ' + kv[my_keys[int(choice)-1]] + '.pyw'
            os.system(COM_CLEAR)
            os.system(comand)
            mk_menu_win(kv, numm_color)
        elif '0' == choice:
            sys.exit()
        else:
            print(f'{Fore.RED} >> wrong choice!')


def menu_main():
    os.system(COM_CLEAR)
    print('\n\n')
    menu = ['1 People',
            '2 Some',
            '3 Monitors',
            '4 Kabinet',
            '5 Otbor',
            '6 Doc',
            '7 Edit',
            '8 Windows',
            '9 PgBase',]
    for point in menu:
        #print(f'{Fore.YELLOW} {point}', end = '  ')
        if point == menu[-1]:
            p_yellow(f'\t{point}')
        else:
            p_blue(f'\t{point}')
        
    choise = -1
    while choise != 0:
        print('\n\n -> ', end='')
        choise = input()
        
        if "1"  == choise:
            os.system(COM_CLEAR)
            menu_people()

        if "2"  == choise:
            os.system(COM_CLEAR)
            menu_some()

        if "3"  == choise:
            os.system(COM_CLEAR)
            menu_monitor()

        if "4"  == choise:
            os.system(COM_CLEAR)
            menu_kabinet()
       
        if "5"  == choise:
            os.system(COM_CLEAR)
            menu_otbor()

        if "6"  == choise:
            os.system(COM_CLEAR)
            menu_doc()

        if "7"  == choise:
            os.system(COM_CLEAR)
            menu_edit()
        
        if "8"  == choise:
            os.system(COM_CLEAR)
            menu_win()
        
        if "9"  == choise:
            os.system(COM_CLEAR)
            menu_db()

        elif not choise:
            menu_main()
        
        elif '0' == choise:
            sys.exit()
        else:
            p_red('\n\twrong choise!')

def menu_win():
    h = {'dep': 'win_dep',
        'term': 'win_term',
        'comon': 'win',}
    mk_menu_win(h, 1)

def menu_people():
    h = {'Priem': 'people/priem',
        'Otpusk': 'people/otpusk',
        'Perevod': 'people/perevod',
        'PostAll': 'people/postall',}
    mk_menu(h, 4)
    
def menu_some():
    h = {'Term': 'some/pg_term',
        'Site': 'some/pg_site',
        'SummuryOtbor': 'some/pg_summury_otbor',
        #'Summury': 'some/pg_summury',
        'Summury_ab': 'some/pg_summury_ab',
        'Natasha': 'some/natasha',
        'Active_term': 'some/active_term',
        'ulya_adresa': 'some/ulya',}
    mk_menu(h, len(h)-1)
    os.system(COM_CLEAR)

def menu_monitor():
    h = {'Walker': 'monitor/walker',
        'Monitor': 'monitor/monitor',
        'Accback': 'monitor/accback',
        'Get_RP_Fast': 'monitor/get_rp_fast',
        'Get_rp_all': 'monitor/get_rp_all',
        'gnetz': 'monitor/gnetz',
        'gdrive_copy': 'monitor/gdrive_copy',
        'gdrive_comon': 'monitor/gdrive_comon',}
    mk_menu(h, len(h))

def menu_kabinet():
    h = {'Rro': 'kabinet/rro',
        'Pereezd': 'kabinet/pereezd',
        'Otmena': 'kabinet/otmena',
        'Prro': 'kabinet/prro',
        'Knigi': 'kabinet/knigi',}
    os.system(COM_CLEAR)
    mk_menu(h, len(h)-1)

def menu_doc():
    h = {'Activaciya': 'doc/activaciya',
        'Act_Peredachi': 'doc/act_peredachi',
        'Dep_To_File': 'doc/dep_to_file',
        'Term_To_File': 'doc/term_to_file',
        'VsyoZapros': 'kabinet/knigi',}
    os.system(COM_CLEAR)
    mk_menu(h, len(h)-1)



def menu_other():
    h = {'Kvadratiki': 'other/kvadratiki',}
    os.system(COM_CLEAR)
    mk_menu(h, 2)

def menu_otbor():
    h = {'Otbor_From_To_Dep': 'otbor/otbor',
        'Otbor_List_Dep': 'otbor/otbor_hard_dep',
        'Otbor_Hard_Term': 'otbor/otbor_hard',
        'Otbor_Serial': 'otbor/otbor_serial',
        'Otbor_From_File_Term': 'otbor/otbor_from_file_term',
        #'Otbor_From_File': 'otbor/otbor_from_file',
        'show_otbor': 'otbor/show_otbor',
        }
    os.system(COM_CLEAR)
    mk_menu(h, 5)


def menu_db():
    h = {'all_to_actual': 'db/actual_refresh_all',
        'otbor_to_actual': 'db/actual_refresh_otbor',
        'del_otbor_actual': 'db/del_actual_otbor',
        'del_all_actual': 'db/del_actual_all',
        'del_otbor_dep': 'db/del_otbor_dep',
        'del_otbor_term': 'db/del_otbor_term',
        'show': 'db/show',
        'analis_dep': 'db/analis_dep',
        'analis_term': 'db/analis_term',
        }
    os.system(COM_CLEAR)
    mk_menu(h, 5)

def menu_edit():
    h = {'dep_from_file': 'edit/dep_from_file',
        'term_from_file': 'edit/term_from_file',}
    os.system(COM_CLEAR)
    mk_menu(h, 0)


init()
menu_main()
