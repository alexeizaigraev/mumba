import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *

from papa_pg import get_data

def doc_papa(query, head, ofName):
    docPath = OUT_DATA_PATH + 'DOC/'
    info = ''
    if head:
        info = head + '\n'
    data = get_data(query)
    count = 0
    for line in data:
        count += 1
        textLine = ';'.join(line)
        #textLine = str(line)
        #info += textLine
        info += f'{str(count)};{textLine}\n'

    fout = docPath + ofName
    info = info.replace(" 0:00:00", "").replace("null", "")
    print()
    text_to_file(info, fout)
    
    #save_and_show(info, fout)
 