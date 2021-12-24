import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os


def dir_out_post():
    return file_to_arr(CONFIG_PATH + 'ConfigPostPath.txt')[0]

def post_all(ag, fout):
    out_text = "login;status;fio;terminal;agent\n"
    a = [f'{line[0]};{line[1]};{line[2]};{line[-2]};{line[-1].strip()}' 
        for line in all_kass
        if (len(line) > 3 \
            and ag in line[-1] \
            and ('true' in line[1]))]
    out_text += '\n'.join(a).rstrip()
    text_to_file(out_text, fout)
    #ssay(fout)



def mk_fierd():
    all_otpuska = file_to_arr(IN_DATA_PATH + 'all_otpuska.csv')
    a = [line[0] for line in all_otpuska
        if line and 'nul' not in line[3]]
    return a



def kass(ag):
    rez = [line[0] for line in all_kass
        if len(line) > 3 \
            and ag in line[-1] \
            and 'true' in line[1]]
    return rez

def post_otpuska(ag, fout):
    logins = kass(ag)
    out_text = "login;otpusk_start;otpusk_finish;data_uvolneniya\n"
    
    a = file_to_arr(IN_DATA_PATH + 'all_otpuska.csv')
    rez = [';'.join(line[:4]).replace('null', '')
        for line in a
        if line[0] in logins]
    out_text += '\n'.join(rez)
    text_to_file(out_text, fout)
    #say(fout)

post_path = GDRIVE_PATH
#all_kass = file_to_arr(IN_DATA_PATH + 'kass_all.csv')
fierd = mk_fierd()
all_kass = [line.split(';') for line in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8") 
    if len(line.split(';')) > 4 
    and 'true' in line.split(';')[1]
    and line.split(';')[0] not in fierd]





#all_otpuska = file_to_arr(IN_DATA_PATH + 'all_otpuska.csv')
#all_otpuska[:] = [line for line in all_otpuska if line[0] in aktiv_logins]
all_otpuska = [line for line in open(IN_DATA_PATH + 'all_otpuska.csv', 'r', encoding="UTF-8") 
    if line.split(';')[0] not in fierd]


post_all('justin', post_path + 'justin/OutPostAll.csv')
post_otpuska('justin', post_path + 'justin/OutPostOtpuskaJust.csv')

post_all('allo', post_path + 'allo/OutPostAllAllo.csv')

post_all('satua', post_path + 'sat/OutPostAllSat.csv')
post_otpuska('satua', post_path + 'sat/OutPostOtpuskaSat.csv')

post_path = OUT_DATA_PATH + 'DOC/'
post_all('justin', post_path + 'justin/OutPostAll.csv')
post_otpuska('justin', post_path + 'justin/OutPostOtpuskaJust.csv')
