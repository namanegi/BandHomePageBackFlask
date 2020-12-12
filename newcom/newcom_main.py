from flask import Flask, render_template, make_response, request, redirect, Blueprint, url_for
from data.db_manage import insert_comment
from datetime import date

newcom_app = Blueprint('newcom', __name__)

@newcom_app.route('/')
def newcom_index():
    try:
        usr = request.cookies.get('usr')
    except:
        return redirect(url_for("login.login_index"))
    return render_template("newcom/newcom.html", usr=usr)

@newcom_app.route('/sendcom', methods=['POST'])
def add_new_comment():
    try:
        usr = request.cookies.get('usr')
        uid = request.cookies.get('uid')
    except:
        return redirect(url_for("comment.comment_index"))
    com = request.form['comment']
    insert_comment(usr, uid, com)
    return redirect(url_for("comment.comment_index"))
        
