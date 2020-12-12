# coding:utf-8

from flask import Flask, make_response, redirect, render_template, request, url_for

from moneylog.money_main import money_app
from login.login_main import login_app
from forget.forget_main import forget_app
from manage.manage_main import manage_app
from cookietest.cktest import cookie_app
from signup.signup_main import signup_app
from newcom.newcom_main import newcom_app
from mypage.mypage_main import mypage_app
from comment.comment_main import comment_app
from videolist.videolist_main import videolist_app

from data.db_manage import delete_uid, get_comments, check_admin, count_comments

app = Flask(__name__)
app.debug = True

app.register_blueprint(money_app)
app.register_blueprint(login_app, url_prefix='/login')
app.register_blueprint(forget_app, url_prefix='/forget')
app.register_blueprint(manage_app, url_prefix='/manage')
app.register_blueprint(cookie_app, url_prefix='/cktest')
app.register_blueprint(signup_app, url_prefix='/signup')
app.register_blueprint(newcom_app, url_prefix='/newcom')
app.register_blueprint(mypage_app, url_prefix='/mypage')
app.register_blueprint(comment_app, url_prefix='/comment')
app.register_blueprint(videolist_app, url_prefix='/videolist')

@app.route('/logout')
def log_out():
    usr = request.cookies.get('usr')
    delete_uid(usr)
    resp = make_response(redirect(url_for('main_index')))
    resp.set_cookie('usr', '', expires=0)
    resp.set_cookie('uid', '', expires=0)
    return resp

@app.route('/')
def main_index():    
    return render_template("index.html")

@app.route('/member')
def member_index():
    return render_template("contents/member.html")

@app.route('/contact')
def contact_index():
    return render_template("contents/contact.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
