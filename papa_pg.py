from modules import *
import psycopg2
from datetime import datetime

def dbexec(execstr):
    #print('# dbexec')
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr)
        con.commit()
        if verb:
            p_blue(execstr)
    except (Exception) as error:
        print ('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

def db_exec_vec(execstr, vec):
    #print('# db_exec_vec')
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr, vec)
        con.commit()
        if verb:
            print(vec[0])
    except Exception as error:
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
 
            
def clear_table(table):
    execstr =  f'DELETE FROM {table}'
    dbexec(execstr)

def table_from_file_to_arr(fname):
    return file_to_arr(IN_DATA_PATH + fname)[1:]

def refresh_table(table_name, fname):
    clear_table(table_name)
    arr = table_from_file_to_arr(fname)
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec in arr:
        if table_name == 'departments':
            query = f'''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}');'''
        elif table_name == 'terminals':
            query = f'''INSERT INTO terminals (department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}', '{vec[19]}')
'''
        elif table_name == 'otbor':
            query = f''' INSERT INTO otbor (term, dep)
VALUES ('{vec[0]}', '{vec[1]}')'''
        try:
            cur.execute(query)
        except Exception as ex:
            p_red(str(ex))
    con.commit()
    if con:
        cur.close()
        con.close()
    p_blue(f'refresh {table_name}')


def title_string(s):
    return s.title()



def insert_all_deps():
    refresh_table('departments', 'departments.csv')


def mk_finish0(reg_date, mod):
    
    didi = {
        'Екселліо FP-280': 7,
        'Екселліо FP-700': 7,
        'Екселліо FPP-350': 0,
        'Екселліо FPU-550ES': 7,
        'Екселліо FPU-550ES': 7,
        'Екселліо FP-280': 5,
        'ПРРО': 10,
        'УЕ РККС': 0,
        }
    dd, mm, yy = reg_date.split('.')
    #yy = yy[:4]
    new_year = int(yy) + didi[mod]
    return f'{dd}.{mm}.{new_year}'


def good_date(vec):
    positions = [4, 15, 20, 21,]
    for pos in positions:
        vec[pos] = vec[pos][:10]
    return vec

def make_finish(vec):
    model = vec[2]
    register = vec[20]
    finish = vec[21]
    if not finish and register and model:
        try:
            vec[21] = mk_finish0(register, model)
        except:
            pass
            return vec


def insert_all_terms():
    refresh_table('terminals', 'terminals.csv')




def insert_all_otbor():
    refresh_table('otbor', 'otbor.csv')



def send_to_gdrive(tname):
    #print(f'# send {tname} to Gdrive')
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        #p_blue('db open ok')
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
        
    except (Exception) as error:
        q_err += 1
        print('>>', error)
    
    finally:
        if con:
            cur.close()
            con.close()
    
    text = ''
    for vec in rows:
        text += ';'.join(vec) + ';' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\n'
    
    text_add_file(text, GDRIVE_PATH + f'arhiv/{tname}.csv')



def select_deps_to_gdrive():
    send_to_gdrive('departments')

def select_terms_to_gdrive():
    send_to_gdrive('terminals')
    
    
  

def table_to_file(tname):
    print(f'# {tname} to file')
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        #p_blue('db open ok')
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
        #arr_to_file(rows, IN_DATA_PATH + 'pg_departments.csv')      

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

    if tname == 'departments':
        text = 'department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner_name;id_terminal;koatu;tax_id;koatu2\n'
    else:
        text = 'department;termial;model;serial_number;date_manufacture;soft;producer;rne_rro;sealing;fiscal_number;oro_serial;oro_number;ticket_serial;ticket_1sheet;ticket_number;sending;books_arhiv;tickets_arhiv;to_rro;owner_rro;register;finish\n'

    for vec in rows:
        text += ';'.join(vec) + '\n'
    
    text_to_file(text, OUT_DATA_PATH + f'pg_{tname}.csv')


def select_terms_to_file():
    table_to_file('terminals')
 
def select_deps_to_file():
    table_to_file('departments')


def select_table(tname):
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
        
    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    return rows

def select_deps():
    return select_table('departments')
        
def select_terms():
    return select_table('terminals')


def get_data(query):
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    return rows


    

def get_terms_data():
    query = '''SELECT otbor.term, departments.id_terminal, departments.city,departments.region, 
departments.street_type, departments.street, departments.hous, 
terminals.serial_number, terminals.fiscal_number
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)

def get_deps_data():
    query = '''SELECT department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2
	FROM public.departments;'''
    return get_data(query)


def get_partners():
    u = "'1700999'"
    q_err = 0
    query = f'''SELECT DISTINCT partner
FROM departments
WHERE department != {u}
ORDER BY partner;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    for line in rows:
        if line[0]:
            arr.append(line[0])
    return arr



def get_summury_data():
    u = "'1700999'"
    query = f'''SELECT department, address, partner
FROM departments
WHERE department != {u}
ORDER BY department;'''
    return get_data(query)

def get_summury_partner_data(partner):
    u = "'1700999'"
    query = f'''SELECT department, region, district_region, post_index, city_type, city, district_city, street_type, street, hous, address, koatu, koatu2
FROM departments
WHERE department != {u} 
AND partner ='{partner}'
ORDER BY department;'''
    return get_data(query)


def get_site_data():
    query = f'''SELECT department, edrpou, address, register  FROM departments ORDER BY department'''
    return get_data(query)

def get_natasha_data():
    query = f'''SELECT department, edrpou, partner FROM departments
ORDER BY partner'''
    return get_data(query)

def get_terminals_list():
    q_err = 0
    print('# get_terminals_list')
    query = f'''SELECT termial FROM terminals
ORDER BY termial'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    return out_list


def get_otbor_deps():
    query = f'''SELECT dep FROM otbor
ORDER BY dep'''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    return out_list



def col_key_pg(hh, key_col_num = -1):
    os.system('cls')
    print('\n\n')
    s = set()
    for line in hh:
        try:
            key = line[key_col_num]
            s.add(key)
        except:
            #('>> no key', key)
            pass
    
    listkey = list(s)
    for i in range(len(listkey)):
        if not listkey[i]:
            continue
        p_cyan(f'\t{i} {listkey[i]}')
    
    #print('')
    print('\n\n\n -> ', end = '')
    choise = int(input())
    os.system('cls')
    
    return listkey[choise]


def get_kabinet_prro_data():
    query = '''SELECT departments.tax_id, departments.koatu, departments.department,
departments.address
FROM otbor, departments
WHERE otbor.dep = departments.department
ORDER BY departments.department;'''
    return get_data(query)


def get_kabinet_knigi_data():
    query = '''SELECT terminals.fiscal_number, terminals.model, terminals.serial_number,
terminals.soft, terminals.rne_rro, terminals.department,
departments.address, departments.koatu, departments.tax_id,
terminals.oro_number, terminals.oro_serial,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)


def get_kabinet_rro_data():
    query = '''SELECT terminals.department,
departments.post_index, departments.region, departments.district_region,
departments.city, departments.street, departments.hous,
departments.koatu, departments.tax_id,
terminals.model, terminals.serial_number, terminals.soft,
terminals.producer, terminals.date_manufacture,
terminals.rne_rro, terminals.oro_serial, terminals.ticket_serial,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)


def get_kabinet_pereezd_data():
    query = '''SELECT terminals.department,
departments.post_index, departments.region,
departments.city, departments.street, departments.hous,
departments.koatu, departments.tax_id,
terminals.model, terminals.serial_number, terminals.soft,
terminals.producer, terminals.date_manufacture,
terminals.rne_rro, terminals.fiscal_number, terminals.oro_serial, terminals.ticket_serial,
terminals.to_rro,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)

def get_kabinet_otmena_data():
    query = '''SELECT terminals.ticket_number, terminals.serial_number,
terminals.model, terminals.soft, terminals.rne_rro, 
departments.address, departments.koatu, departments.tax_id,
terminals.fiscal_number, departments.department
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)


def insert_all_depsarhiv():
    now = str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"))
    data = select_deps()
    #print(data)
    q_err = 0
    query = '''INSERT INTO public.departmentsarhiv(
department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2, datetime)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        q_err = 0
        
        for vec in data:
            if not vec:
                continue
            vec = list(vec)
            try:
                vec.append(now)
                #print(vec)
                cur.execute(query, vec)
                
            except (Exception) as error:
                q_err += 1
                print('>>', error)

            if verb:
                pass
                #print(vec[0])                
        con.commit()
    except:
        pass
    finally:
        if con:
            cur.close()
            con.close()

    if q_err == 0:
        p_blue('insert_all_depsarhiv\n')
    else:
        print('insert_all_depsarhiv', 'errors:', q_err, '\n')



def insert_all_termsarhiv():
    now = str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"))
    data = select_terms()
    #print(data)
    q_err = 0
    query = '''INSERT INTO public.terminalsarhiv(
	department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish, datetime)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        q_err = 0
        
        for vec in data:
            if not vec:
                continue
            vec = list(vec)
            try:
                vec.append(now)
                cur.execute(query, vec)
                
            except (Exception) as error:
                q_err += 1
                print('>>', error)

            if verb:
                pass
                #print(vec[0])                
        con.commit()
    except:
        pass
    finally:
        if con:
            cur.close()
            con.close()

    if q_err == 0:
        p_blue('insert_all_termsarhiv\n')
    else:
        print('insert_all_termsarhiv', 'errors:', q_err, '\n')


def get_history_data():
    query = '''SELECT terminals.termial, terminals.department,
terminals.serial_number, departments.address
FROM terminals, departments, otbor
WHERE terminals.department = departments.department
AND terminals.termial = otbor.term
ORDER BY terminals.termial;'''
    return get_data(query)




def date_log():
    ddd = datetime.now().date()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{y}.{m}.{d}'

def loger_pg(kind):
    data = get_history_data()
    nau = date_log()
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    #p_blue('db open ok')
    
    for vec in data:
        query = f""" INSERT INTO logi (department, termial, serial_number, address, datalog, kind)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{nau}', '{kind}');"""
        try:
            cur.execute(query)
        except Exception as ex:
            print(ex)
        if verb:
            print(vec[1])                
    con.commit()
    
    if con:
        cur.close()
        con.close()

    now = str(datetime.strftime(datetime.now(), "%Y-%m-%d_%H_%M_%S"))
    out_path = 'R:/DRM/BackupAccess/db2_be_' + now + '_' + kind + '.accdb'
    in_path = IN_DATA_PATH + 'drm.db'
    try:
        shutil.copy(in_path, out_path)
        print(f'\n{out_path}')
    except:
        print('\n\tno accback')








verb = False
