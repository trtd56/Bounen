# -*- coding: utf-8 -*-

from src.common import exe_sql, add_name_id, is_name_exist, get_users
from src.common import update_db_and_get_name, calc_score_sum
from src.common import HOST_IP, GROUP_DICT

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/registration')
def registration():
    return render_template('index.html', ip=HOST_IP)

@app.route('/q1')
def q1():
    name_id = request.args.get('name_id')
    if is_name_exist(name_id):
        return render_template('mistake.html', name_id=name_id, ip=HOST_IP)
    else:
        # registration processing
        add_name_id(name_id)
        users = get_users(GROUP_DICT['q1'])
        return render_template('q.html', name_id=name_id, ip=HOST_IP,
                                users=users, q=1, next_q='q2')

@app.route('/q2')
def q2():
    # q1 scpre update
    name_id = update_db_and_get_name(request, 1)
    # q2 page predict
    users = get_users(GROUP_DICT['q2'])
    return render_template('q.html', name_id=name_id, ip=HOST_IP,
                            users=users, q=2, next_q='q3')

@app.route('/q3')
def q3():
    # q2 scpre update
    name_id = update_db_and_get_name(request, 2)
    # q3 page predict
    users = get_users(GROUP_DICT['q3'])
    return render_template('q.html', name_id=name_id, ip=HOST_IP,
                            users=users, q=3, next_q='finish')
@app.route('/finish')
def finish():
    # q3 processing
    update_db_and_get_name(request, 3)
    return render_template('finish.html')

@app.route('/show_q1')
def show_q1():
    q = calc_score_sum(1)
    return render_template('show_score.html', contents=q, ip=HOST_IP)

@app.route('/show_q2')
def show_q2():
    q = calc_score_sum(2)
    return render_template('show_score.html', contents=q, ip=HOST_IP)

@app.route('/show_q3')
def show_q3():
    q = calc_score_sum(3)
    return render_template('show_score.html', contents=q, ip=HOST_IP)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=61203)
