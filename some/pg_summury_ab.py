import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


head = '№ п/п;"№ Відділення ТОВ ""ЕПС""";Адреса;Партнер\n'
out_text = head

data = get_summury_data()

natasha = mk_natasha()
my_deps = []
count = 0
for line in data:
    if line[0] not in natasha:
        continue
    count += 1
    out_line = f'{count};{line[0]};{line[1]};{line[2]}'
    out_text += out_line + '\n'
    
text_to_file(out_text, OUT_DATA_PATH + 'summury_ab.csv')

