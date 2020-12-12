from flask import Flask, url_for, render_template, redirect, request, Blueprint
from data.db_manage import check_usreml, get_question, check_ans, reset_pwd

forget_app = Blueprint('forget', __name__)

@forget_app.route('/')
def forget_index():
    try:
        err_id = int(request.args['err_id'])
    except:
        err_id = 0
    if err_id == 1:
        message = 'WRONG USERNAME OR EMAIL! Please make sure they are CORRECT and type again.'
    elif err_id == 2:
        message = 'WRONG SECURITY ANS! Please type CORRECT info again!'
    else:
        message = ''
    return render_template("forget/forget.html", message=message)

@forget_app.route('/repwd1', methods=['POST'])
def forget_check_usr():
    usr = request.form['username']
    email = request.form['email']
    if check_usreml(usr, email):
        question = get_question(usr)
        message = []
        message.append(usr)
        message.append(question)
        return redirect(url_for('forget.forget_question', usr=usr, question=question))
    else:
        err_id = 1
        return redirect(url_for('forget.forget_index', err_id=err_id))

@forget_app.route('/question')
def forget_question():
    usr = request.args['usr']
    question = request.args['question']
    return render_template("forget/question.html", usr=usr, question=question)

@forget_app.route('/repwd2', methods=['POST'])
def forget_check_ans():
    usr = request.form['username']
    ans = request.form['ans']
    if check_ans(usr, ans):
        return redirect(url_for('forget.resetpw_index', usr=usr))
    else:
        return redirect(url_for('forget.forget_index', err_id=2))

@forget_app.route('/resetpw')
def resetpw_index():
    usr = request.args['usr']
    new_pwd = reset_pwd(usr)
    return render_template("forget/resetpw.html", usr=usr, pwd=new_pwd)
