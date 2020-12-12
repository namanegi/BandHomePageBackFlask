from flask import Flask, render_template, make_response, request, redirect, Blueprint, url_for
from data.db_manage import get_usr_comments, check_uid, ch_pwd

mypage_app = Blueprint('mypage', __name__)

@mypage_app.route('/')
def mypage_index():
    usr = request.cookies.get('usr')
    if usr is None:
        return redirect(url_for('main_index'))
    comments = get_usr_comments(usr)
    return render_template("mypage/mypage.html", datas=comments)

@mypage_app.route('/chpwd')
def chpwd_index():
    try:
        err_id = int(request.args['err_id'])
    except:
        err_id = 0
    if err_id == 1:
        err_message = 'WRONG PASSWORD!'
    else:
        err_message = ''
    return render_template("mypage/chpwd.html", message=err_message)

@mypage_app.route('/newpwd', methods=['POST'])
def set_new_pwd():
    usr = request.cookies.get('usr')
    uid = request.cookies.get('uid')
    old_pwd = request.form['oldpwd']
    old_pwd_r = request.form['oldpwdr']
    new_pwd = request.form['newpwd']
    if old_pwd == old_pwd_r and check_uid(usr, uid):
        ch_pwd(usr, new_pwd)
        return redirect('/logout')
    else:
        return redirect(url_for('mypage.chpwd_index', err_id=1))
