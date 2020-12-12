from flask import Flask, request, Blueprint, render_template, redirect, url_for
from data.db_manage import read_questions, insert_data

signup_app = Blueprint('signup', __name__)

@signup_app.route('/')
def signup_index():
    q_dic = read_questions()
    return render_template("signup/signup.html", q_dic=q_dic)

@signup_app.route('/reg', methods=['POST'])
def signup():
    usr = request.form['username']
    pwd = request.form['passwd']
    pwdr = request.form['passwdrp']
    email = request.form['email']
    qid = int(request.form['qid'])
    ans = request.form['ans']
    if pwd == pwdr:
        insert_data(usr, pwd, email, 0, qid, ans)
        return redirect(url_for('login.login_index'))
