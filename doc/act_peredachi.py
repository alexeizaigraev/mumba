import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa import doc_papa

query = """SELECT terminals.model, terminals.serial_number, 
terminals.department, departments.address
FROM terminals, departments, otbor
WHERE terminals.termial = otbor.term
AND departments.department = otbor.dep;"""

head = "№ п/п;Найменування устаткування, Реєстратор контрольно-касовий електронний чорний;Серійний Номер;Відділення ТОВ \"ЕПС\";Місце розташування підприємства торгівлі-послуг;Кількість оди-ниць;Вартість з ПДВ (грн.)"
fName = "Act_Peredachi.csv"
doc_papa(query, head, fName)