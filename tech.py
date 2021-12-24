import os
import getpass
from colorama import Fore, Style, init

def tech():
    say = 'q'
    init()
    print(Fore.BLACK)
    while True:
        say = getpass.getpass()
        os.system('cls')
        if say.lower() != 'az' or say.lower() != 'фя':
            break
        #print('namaste')

tech()
