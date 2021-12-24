# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import os
import shutil
from pathlib import Path
from modules import *
from datetime import datetime
import shutil
from papa_pg import *
from doc_papa import doc_papa



now = str(datetime.strftime(datetime.now(), "%Y-%m-%d"))
#in_path = 'R:/DRM/Access/db2_be.accdb'
out_path = GDRIVE_PATH + 'PG_BACKUP/' + now + '_departments.csv'

in_path = IN_DATA_PATH + 'drm.db'
#out_path = 'R:/DRM/BackupAccess/drm_' + now + '.db'
try:
    shutil.copy(in_path, out_path)
    print(f'\n{out_path}')
except:
    print('\n\tno accback')

