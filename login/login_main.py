from flask import Flask, render_template, make_response, request, redirect, Blueprint, url_for
from data.db_manage import check_admin, check_usrpwd, insert_uid, UsernameNotExists, WrongPassword
from random import randint

login_app = Blueprint('login', __name__)

@login_app.route('/')
def login_index():
    """check if already login
    """
    try:
        err_id = request.args['err_id']
    except:
        err_id = '0'
    if err_id == '1':
        error_message = 'Wrong username! Please make sure your username is right or you have registered before.'
    elif err_id == '2':
        error_message = 'Wrong password! Please type again with correct one!'
    else:
        error_message = ''
    if check_login():
        did_login = True
    else:
        did_login = False
    if not did_login:    
        """show login page"""
        return render_template("login/login.html", message=error_message)
    else:
        """jump to manage page"""
        return redirect(url_for('manage.manage_index'))

@login_app.route('/usrpwd', methods=['POST'])
def clarify_usrpwd():
    usr = request.form['username']
    pwd = request.form['passwd']
    try:
        if check_usrpwd(usr, pwd):
            uid = get_uid()
            insert_uid(usr, uid)
            if check_admin(usr):
                resp = make_response(redirect(url_for('manage.manage_index')))
                resp.set_cookie('usr', usr)
                resp.set_cookie('uid', uid)
                return resp
            else:
                resp = redirect('/comment')
                resp.set_cookie('usr', usr)
                resp.set_cookie('uid', uid)
                return resp
    except UsernameNotExists:
        err_id = 1
    except WrongPassword:
        err_id = 2
    return redirect(url_for('login.login_index', err_id = err_id))

def get_uid():
    res = ''
    for i in range(16):
        res = res + chr(randint(33,127))
    return res

def make_cookie(usr, uid):
    resp_ck = make_response()
    resp_ck.set_cookie('usr', usr)
    resp_ck.set_cookie('uid', uid)
    return resp_ck

def check_login():
    usr = request.cookies.get('usr')
    uid = request.cookies.get('uid')
    return usr is not None and uid is not None

if __name__ == '__main__':
    login_app.run('0.0.0.0', 8000, debug=True)
