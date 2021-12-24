import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa import doc_papa

query = """SELECT department, termial, serial_number, address, datalog, kind
	FROM public.logi;"""

head = "num;department;termial;serial_number;address;datalog;kind"
fName = "logi.csv"
doc_papa(query, head, fName)