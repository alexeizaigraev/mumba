import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa import doc_papa

query = """SELECT terminals.department, terminals.termial, terminals.model, terminals.serial_number, 
terminals.date_manufacture, terminals.soft, terminals.producer, terminals.rne_rro, 
terminals.sealing, terminals.fiscal_number, terminals.oro_serial, terminals.oro_number, 
terminals.ticket_serial, terminals.ticket_1sheet, terminals.ticket_number, 
terminals.sending, terminals.books_arhiv, terminals.tickets_arhiv, terminals.to_rro, 
terminals.owner_rro, terminals.register, terminals.finish,

departments.department, departments.region, departments.district_region, 
departments.district_city, departments.city_type, departments.city, 
departments.street, departments.street_type, departments.hous, departments.post_index, 
departments.partner, departments.status, departments.register, departments.edrpou, 
departments.address, departments.partner_name, departments.id_terminal, 
departments.koatu, departments.tax_id, departments.koatu2
	
FROM public.departments, public.terminals, public.otbor
WHERE terminals.termial = otbor.term
AND terminals.department = departments.department;"""

head = "num;terminals.department;terminals.termial;terminals.model;terminals.serial_number;terminals.date_manufacture;terminals.soft;terminals.producer;terminals.rne_rro;terminals.sealing;terminals.fiscal_number;terminals.oro_serial;terminals.oro_number;terminals.ticket_serial;terminals.ticket_1sheet;terminals.ticket_number;terminals.sending;terminals.books_arhiv;terminals.tickets_arhiv;terminals.to_rro;terminals.owner_rro;terminals.register;terminals.finish;departments.department;departments.region;departments.district_region;departments.district_city;departments.city_type;departments.city;departments.street;departments.street_type;departments.hous;departments.post_index;departments.partner;departments.status;departments.register;departments.edrpou;departments.address;departments.partner_name;departments.id_terminal;departments.koatu;departments.tax_id;departments.koatu2"
fName = "Vsyo_Otbor.csv"
doc_papa(query, head, fName)