from modules import *
import psycopg2
from datetime import datetime

def dbexec(execstr):
    info = ''
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr)
        con.commit()
    except (Exception) as error:
        alarm(error)
    finally:
        if con:
            cur.close()
            con.close()
        
def db_exec_vec(execstr, vec):
    info = ''
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr, vec)
        con.commit()
    except Exception as error:
        info += str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()
    return info
 
            
def clear_table(table):
    execstr =  f'DELETE FROM {table}'
    dbexec(execstr)


def del_dep_new(dep):
    q=f"""DELETE FROM public.departmentsnew
	WHERE department = '{dep}';
    """
    dbexec(q)

def del_dep(dep):
    q=f"""DELETE FROM public.departments
	WHERE department = '{dep}';
    """
    dbexec(q)

def del_term(term):
    q=f"""DELETE FROM public.terminals
	WHERE termial = '{term}';
    """
    dbexec(q)

  



def table_from_file_to_arr(fname):
    return file_to_arr(IN_DATA_PATH + fname)[1:]


def refresh_table_otbor_term():
    q_err = 0
    sum = 0
    clear_table('otbor')
    arr = file_to_vec(IN_DATA_PATH + 'otbor_term.csv')
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for line in arr:
        query = f''' INSERT INTO otbor (term, dep)
VALUES ('{line}', '{line[:-1]}')'''
        try:
            sum += 1
            cur.execute(query)
        except Exception as ex:
            q_err += 1
    con.commit()
    if con:
        cur.close()
        con.close()
    ssay(f'refresh otbor\n{q_err=} {sum=}\n')

def clear_part_table(table_name, arr):
    for line in arr:
        if table_name == 'departments':
            del_dep(line[0])
        elif table_name == 'terminals':
            del_term(line[1])

def refresh_table_from_file_full(table_name, fname, start=0):
    q_err = 0
    sum = 0
    #clear_table(table_name)
    arr = file_to_arr(fname)[start:]
    #clear_part_table(table_name, arr)
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec0 in arr:
        vec = good_vec(vec0)
        if table_name == 'departments':
            query_del = f"""DELETE FROM public.departments
	WHERE department = '{vec[0]}';"""
            query = f'''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}');'''
        elif table_name == 'terminals':
            query_del = f"""DELETE FROM public.terminals
	WHERE termial = '{vec[1]}';"""
            query = f'''INSERT INTO public.terminals(
	department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish)
	VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}', '{vec[19]}', '{vec[20]}', '{vec[21]}');'''
        elif table_name == 'otbor':
            query = f''' INSERT INTO otbor (term, dep)
VALUES ('{vec[0]}', '{vec[1]}')'''
        try:
            cur.execute(query_del)
        except:
            pass
        try:
            sum += 1
            cur.execute(query)
        except Exception as ex:
            q_err += 1
    con.commit()
    if con:
        cur.close()
        con.close()
    ssay(f'refresh {table_name}\n{q_err=} {sum=}\n')

def term_from_file_full():
    refresh_table_from_file_full('terminals', IN_DATA_PATH + 'terminals.csv', start=1)

def dep_from_file_full():
    refresh_table_from_file_full('departments', IN_DATA_PATH + 'departments.csv', start=1)

def otbor_from_file_full():
    refresh_table_from_file_full('otbor', IN_DATA_PATH + 'otbor.csv', start=1)



def refresh_table(table_name, fname):
    q_err = 0
    sum = 0
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
            sum += 1
            cur.execute(query)
        except Exception as ex:
            q_err += 1
    con.commit()
    if con:
        cur.close()
        con.close()
    ssay(f'refresh {table_name}\n{q_err=} {sum=}\n')
 


def title_string(s):
    return s.title()


"""
def insert_all_deps():
    return refresh_table('departments', 'departments.csv')
"""

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

"""
def insert_all_terms():
    return refresh_table('terminals', 'terminals.csv')
"""

def insert_all_otbor():
    return refresh_table('otbor', 'otbor.csv')

def insert_all_otbor_term():
    return refresh_table_otbor_term()  

def table_to_file(tname):
    info = ''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
    except (Exception) as error:
        q_err += 1
        info == str(error) + '\n'
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
    fname = OUT_DATA_PATH + f'pg_{tname}.csv'
    text_to_file(text, fname)
    info += fname + '\n'
    return info


def select_terms_to_file():
    return table_to_file('terminals')
 
def select_deps_to_file():
    return table_to_file('departments')


def select_table(tname):
    q_err = 0
    sum = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
        sum += 1
    except (Exception) as error:
        q_err += 1
        alarm(error)
    finally:
        if con:
            cur.close()
            con.close()
        ssay(f'select_table {q_err=}')
    return rows

def select_deps():
    return select_table('departments')
        
def select_terms():
    return select_table('terminals')


def get_data(query):
    info = ''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except (Exception) as error:
        q_err += 1
        info += str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()
    
    return rows


    



def get_deps_data():
    query = '''SELECT department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2
	FROM public.departments;'''
    return get_data(query)


def get_list_one(query):
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except (Exception) as err:
        q_err += 1
        p_red(err)
    finally:
        if con:
            cur.close()
            con.close()
    
    for line in rows:
        if line[0]:
            arr.append(line[0])
    return arr


def get_partners():
    u = ''
    query = f'''SELECT DISTINCT partner
FROM departments
WHERE department != {u}
ORDER BY partner;'''
    return get_list_one(query)
    
    
def get_terminals_list():
    query = f'''SELECT termial FROM terminals
ORDER BY termial'''
    return get_list_one(query)
    

def get_serial_list():
    query = f'''SELECT DISTINCT serial_number FROM terminals
ORDER BY serial_number'''
    return get_list_one(query)
    
def get_terminals_list_partner(partner):
    query = f'''SELECT termial FROM terminals, departments
    WHERE departments.department = terminals.department
    AND departments.partner = '{partner}'
ORDER BY termial;'''
    return get_list_one(query)
    

def get_departments_list():
    query = f'''SELECT department FROM departments
ORDER BY department'''
    return get_list_one(query)
    

def get_departments_new_list():
    query = f'''SELECT department FROM departmentsnew
ORDER BY department'''
    return get_list_one(query)
    
def get_otbor_deps():
    query = f'''SELECT dep FROM otbor
ORDER BY dep'''
    return get_list_one(query)
    
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


def get_kabinet_pereezd_old_data():
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


def get_history_data():
    query = '''SELECT terminals.termial, terminals.department,
terminals.serial_number, departments.address
FROM terminals, departments, otbor
WHERE terminals.department = departments.department
AND terminals.termial = otbor.term
ORDER BY terminals.termial;'''
    return get_data(query)

def get_activ_term_data():
    query = '''SELECT terminals.termial, terminals.department,
departments.address, departments.partner
FROM terminals, departments
WHERE terminals.department = departments.department
ORDER BY terminals.termial;'''
    return get_data(query)

def get_one_term_data(term):
    query = f'''SELECT * 
FROM terminals
WHERE terminals.termial = '{term}';'''
    return get_data(query)

def get_one_dep_data(dep):
    query = f'''SELECT * 
FROM departments
WHERE departments.department = '{dep}';'''
    return get_data(query)

def get_term_by_serial(serial):
    query = f'''SELECT DISTINCT terminals.termial
    FROM terminals
WHERE serial_number = '{serial}';'''
    return get_list_one(query)[0]


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
            pass               
    con.commit()
    
    if con:
        cur.close()
        con.close()

    now = str(datetime.strftime(datetime.now(), "%Y-%m-%d_%H_%M_%S"))
    out_path = 'R:/DRM/BackupAccess/db2_be_' + now + '_' + kind + '.accdb'
    in_path = IN_DATA_PATH + 'drm.db'
    try:
        shutil.copy(in_path, out_path)
    except:
        pass


#_actual___________________________



  
def get_all_dep_data():
    q = 'SELECT * FROM departments'
    return get_data(q)

def get_all_dep_new_data():
    q = 'SELECT * FROM departmentsnew'
    return get_data(q)

def get_one_dep_data(dep):
    q = f"""SELECT * FROM departments WHERE department = '{dep}';"""
    return get_data(q)

def get_one_dep_new_data(dep):
    q = f"""SELECT * FROM departments WHERE departmentnew = '{dep}';"""
    return get_data(q)


def refresh_table_actual():
    sum = 0
    qerr = 0
    clear_table('departmentsnew')
    arr = get_all_dep_data()
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec in arr:
        query = f"""INSERT INTO departmentsnew (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2)
    VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}' , '{vec[19]}');"""
        try:
            cur.execute(query)
            sum += 1
        except Exception as ex:
            qerr += 1
            alarm(ex)
    con.commit()
    if con:
        cur.close()
        con.close()
    ssay(f'refresh dep new\n{qerr=} {sum=}')
    


def title_string(s):
    return s.title()


def refresh_one_term(vec):
    vec = good_vec(vec)
    info = ''
    try:
        del_term(vec[1])
    except:
        pass
    try:
        query = f'''INSERT INTO public.terminals(
	department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish)
	VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}', '{vec[19]}', '{vec[20]}', '{vec[11]}');'''
        dbexec(query)
    except Exception as ex:
        print(ex)


   
def refresh_one_dep(vec):
    vec = good_vec(vec)
    info = ''
    vec.append('')
    try:
        del_dep(vec[0])
    except Exception as ex:
        info += str(ex)
    try:
        query = f"""INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2)
    VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}' , '{vec[19]}');"""
        dbexec(query)
    except:
        pass

def act_refresh_one_dep(dep):
    dep = str(dep)
    vec = []
    try:
        vec = get_one_dep_data(dep)[0]
    except Exception as ex:
        pass
    try:
        del_dep_new(dep)
    except:
        pass
    try:
        query = f"""INSERT INTO departmentsnew (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2)
    VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}' , '{vec[19]}');"""
        dbexec(query)
    except:
        pass


#edit___________________________

def mk_txt(key_field):
    if len(key_field) < 8:
        txt = ""
        heads = file_to_arr(IN_DATA_PATH + "departments.csv")[0]
        heads.append('koatu2')
        txt_arr = []
        for i in range(len(heads)):
            heads[i] = f'{heads[i]};'
        try:
            data = get_one_dep_data(key_field)[0]
            for i in range(len(data)):
                try:
                    heads[i] += data[i]
                except:
                    pass
        except:
            pass
        return '\n'.join(heads)
    else:
        txt = ""
        heads = file_to_arr(IN_DATA_PATH + "terminals.csv")[0]
        txt_arr = []
        for i in range(len(heads)):
            heads[i] = f'{heads[i]};'
        try:
            data = get_one_term_data(key_field)[0]
            for i in range(len(data)):
                try:
                    heads[i] += data[i]
                except:
                    pass
        except:
            pass
        return '\n'.join(heads)


def get_key_from_textbox(txt):
    arr = txt.split('\n')
    try:
        dep = arr[0].split(';')[1]
        term = arr[1].split(';')[1]
        if dep and term and dep in term:
            return arr[1].split(';')[1]
    except:
        pass
    return arr[0].split(';')[1]

def get_data_from_textbox(txt):
    vec = []
    for line in txt.split('\n'):
        try:
            vec.append(line.split(';')[1])
        except:
            vec.append(line)
    return vec
  
def next_dep(dep):
    vec = get_departments_list()
    if dep in vec:
        if vec.index(dep) < len(vec) - 1:
            return vec[vec.index(dep) + 1]
        else:
            return vec[0]
    else:
        return(str(vec))

def pred_dep(dep):
    vec = get_departments_list()
    if dep in vec:
        if vec.index(dep) > 0:
            return vec[vec.index(dep) - 1]
        else:
            return vec[len(vec) -1]

def next_term(term):
    vec = get_terminals_list()
    if term in vec:
        if vec.index(term) < len(vec) - 1:
            return vec[vec.index(term) + 1]
        else:
            return vec[0] 

def pred_term(term):
    vec = get_terminals_list()
    if term in vec:
        if vec.index(term) > 0:
            return vec[vec.index(term) - 1]
        else:
            return vec[len(vec) -1]

def get_address(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0][14]

def get_koatu(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0][17]

def get_tax_id(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0][18]
    
def get_koatu2(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    city = arr[0][5].strip()
    distrCity = arr[0][3].strip()
    koatu = arr[0][17].strip()
    if not city:
        city = ''
    if not distrCity:
        distrCity = ''
    if not koatu:
        koatu = ''
    rez = ""
    try:
        rez = mk_koatu2(city, distrCity, koatu)
    except:
        pass
    return rez



verb = False



