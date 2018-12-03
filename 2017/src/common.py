# -*- coding: utf-8 -*-

import sqlite3

"""
setting
"""

HOST_IP = 'localhost'
USER_DICT = {
    'A' : 'Iwaさん',
    'B' : 'Iznさん',
    'C' : 'Trtさん',
    'D' : 'Bunさん',
    'E' : 'Yuiさん',
    'F' : 'Yaqさん',
}

"""
constants
"""

DB_ARCHIVE = './db_archive/'
DB_NAME = DB_ARCHIVE + 'bounen.db'
DB_KEYS = ['name_id',
        'q1_1', 'q1_2', 'q1_3',
        'q2_1', 'q2_2', 'q2_3',
        'q3_1', 'q3_2', 'q3_3']
ANSWER = {
        'q1_1' : 1,
        'q1_2' : 0,
        'q1_3' : 2,
        'q2_1' : 2,
        'q2_2' : 1,
        'q2_3' : 0,
        'q3_1' : 3,
        'q3_2' : 1,
        'q3_3' : 5,
}
GROUP_DICT = {
    'q1' : ['A', 'B', 'C', 'D'],
    'q2' : ['A', 'B', 'C'],
    'q3' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
}

"""
functions
"""

def exe_sql(sql):
    con = sqlite3.connect(DB_NAME)
    con.execute(sql)
    con.commit()
    con.close()

def add_name_id(name_id):
    con = sqlite3.connect(DB_NAME)
    sql = "insert into score values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    con.execute(sql, (name_id, -1, -1, -1, -1, -1, -1, -1, -1, -1))
    con.commit()
    con.close()

def get_score():
    score = []
    con = sqlite3.connect(DB_NAME)
    c = con.cursor()
    c.execute("select * from score")
    for row in c:
        score.append({k:i for i,k in zip(row, DB_KEYS)})
    con.close()
    return score

def is_name_exist(name_id):
    score = get_score()
    name_ids = [i['name_id'] for i in score]
    return name_id in name_ids

def update_db(name_id, q, val):
    con = sqlite3.connect(DB_NAME)
    sql = "update score set {1}={2} where name_id='{0}'".format(name_id, q, val)
    con.execute(sql)
    con.commit()
    con.close()

def get_users(users):
    names =  [v for k, v in USER_DICT.items() if k in users]
    name_dict = [{'id':i, 'name':v} for i, v in enumerate(names)]
    return name_dict

def update_db_and_get_name(request, q):
    name_id = request.args.get('name_id')
    val1 = int(request.args.get('val1'))
    update_db(name_id, 'q{0}_1'.format(q), val1)
    val2 = int(request.args.get('val2'))
    update_db(name_id, 'q{0}_2'.format(q), val2)
    val3 = int(request.args.get('val3'))
    update_db(name_id, 'q{0}_3'.format(q), val3)
    return name_id

def calc_score_sum(q_id):
    db = get_score()
    scores = {}
    for dic in db:
        score = 0
        for q in range(q_id):
            add_score = 2 if q == 3 else 1
            score += add_score if dic['q{0}_1'.format(q+1)] == ANSWER['q{0}_1'.format(q+1)] else 0
            score += add_score if dic['q{0}_2'.format(q+1)] == ANSWER['q{0}_2'.format(q+1)] else 0
            score += add_score if dic['q{0}_3'.format(q+1)] == ANSWER['q{0}_3'.format(q+1)] else 0
        scores.update({dic['name_id']:score})
    return [{'name_id':k, 'score':v} for k, v in sorted(scores.items(), key=lambda x: -x[1])]

if __name__ == '__main__':
    import pandas as pd
    db = get_score()
    print(pd.DataFrame(db))
