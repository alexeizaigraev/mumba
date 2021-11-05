import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


def niseStr(str):
    return str.replace("’", '').replace("'", '').replace(' ', '').replace('-', '').replace('`', '').lower() 


def strInBoth(str1, str2):
    str1 = niseStr(str1)
    str2 = niseStr(str2)
    if ( str1 in str2 ) or ( str2 in str1 ):
        return True
    return False


def mk_koatu2(koatuSpr, sity, distrSity, koatu, adrFull):
    if not koatu:
        return ''
    for line in koatuSpr:
        sprKoatu = line[1]
        sprPlace = line[2]
        if (koatu in sprKoatu or sprKoatu in koatu) \
        and ( strInBoth(sprPlace, sity) or ( strInBoth(sprPlace, distrSity) ) ):
            return line[0]
    return ''


koatuSpr = file_to_arr(IN_DATA_PATH + 'koatuall.csv')

head = '№ п/п;"№ Відділення ТОВ ""ЕПС""";Область;Район в обл.;Індекс;Тип населеного пункту;Населений пункт;Район в місті;Тип вулиці;Адреса;Номер будинку;Дата признчення керівника;модель РРО;Заводський № РРО;2;koatu1;koatu2\n'
out_text = head


h = get_partners()
partner = ask(h)
print(f'\n\n\t{partner}\n\n')

data = get_summury_partner_data(partner)


my_deps = []
count = 0
for line in data:
    line = list(line)
    sity = line[5]
    distrSity = line[6]
    koatu = line[11]
    adrFull = line[12]

    ins_data = ''
    try:
        ins_data = mk_koatu2(koatuSpr, sity, distrSity, koatu, adrFull)
    except Exception as ex:
        p_red(ex)
    line[-1] = ins_data
    
    line = list(line)
    
    dep = line[0]
    if not dep:
        continue
    count += 1
    out_line = (str(count) + ';' 
            + line[0]  + ';'
            + line[1] + ';'
            + line[2] + ';'
            + line[3] + ';'
            + line[4] + ';'
            + line[5] + ';'
            + line[6] + ';'
            + line[7] + ';'
            + line[8] + ';'
            + line[9] + ';'
            + '' + ';'
            + '' + ';'
            + '' + ';'
            + line[10] + ';'
            + line[11] + ';'
            + line[12] )
    out_text += out_line + '\n'
    

text_to_file(out_text, OUT_DATA_PATH + 'hr_new_deps.csv')

