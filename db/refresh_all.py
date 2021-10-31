import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 


from papa_pg import *
import os
import subprocess


#os.system('python runsharp.py')

app_path = file_to_vec('Config/app_path.txt')[0]
try:
  #os.startfile('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
  subprocess.run(app_path)
except Exception as ex:
   print(ex)

verb = True

insert_all_deps()
insert_all_terms()
insert_all_otbor()
