import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa import doc_papa

query = """SELECT terminals.department, departments.address,
terminals.serial_number, terminals.fiscal_number
FROM terminals, departments, otbor
WHERE terminals.termial = otbor.term
AND departments.department = otbor.dep;"""

head = "№ п/п;№ відділення ТОВ«ЕПС»;Адреса відділення; ЗН;ФН;Дата активації"
fName = "Activaciya.csv"
doc_papa(query, head, fName)