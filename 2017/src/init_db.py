# -*- coding: utf-8 -*-

import os
import shutil
from datetime import datetime

from common import DB_NAME, DB_ARCHIVE, exe_sql

if os.path.exists(DB_NAME):
    # save previous db
    now = datetime.now().strftime('%Y.%m.%dT%H.%M.%S')
    shutil.copyfile(DB_NAME, DB_ARCHIVE + now + '.db')
    # delete already exist table
    os.remove(DB_NAME)

create_db = """
create table score (
name_id varchar(30),
q1_1 integer,
q1_2 integer,
q1_3 integer,
q2_1 integer,
q2_2 integer,
q2_3 integer,
q3_1 integer,
q3_2 integer,
q3_3 integer
);
"""
exe_sql(create_db)
print("initialize db completed")
