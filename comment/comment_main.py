from flask import Flask, render_template, make_response, request, redirect, Blueprint, url_for
from data.db_manage import check_admin, get_comments, count_comments

comment_app = Blueprint('comment', __name__)

@comment_app.route('/')
def comment_index():
    lines = count_comments()
    datas = get_comments()
    if lines / 5 > 1:
        p_num = lines // 5 + 1 if lines % 5 != 0 else lines // 5
    else:
        p_num = 1
    return render_template("comment/comment.html", login_status=check_login(), p_num=p_num, datas=datas)

@comment_app.route('/id=<p_id>')
def comment_index_p(p_id):
    lines = count_comments()
    p_ = int(p_id)
    datas = get_comments((p_-1)*5,p_*5)
    if lines / 5 > 1:
        p_num = lines // 5 + 1 if lines % 5 != 0 else lines // 5
    else:
        p_num = 1
    return render_template("comment/comment.html", login_status=check_login(), p_num=p_num, datas=datas)

def check_login():
    usr = request.cookies.get('usr')
    uid = request.cookies.get('uid')
    if usr is None or uid is None:
        return 0
    else:
        try:
            b = check_admin(usr)
        except:
            return 0
        if b:
            return 2
        else:
            return 1
