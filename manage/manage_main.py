from flask import Flask, url_for, make_response, render_template, redirect, request, Blueprint
from data.db_manage import delete_uid, check_uid, check_admin, get_comments, del_comment, count_comments, insert_video, get_videos, count_videos, del_video

manage_app = Blueprint('manage', __name__)

@manage_app.route('/')
def manage_index():
    usr = request.cookies.get('usr')
    uid = request.cookies.get('uid')
    if check_uid(usr, uid):
        if check_admin(usr):
            lines = count_comments()
            datas = get_comments(0, lines)
            return render_template("manage/manage_com.html", usr=usr, uid=uid, datas=datas)
        else:
            return redirect(url_for('main_index'))
    else:
        return redirect(url_for("login.login_index"))

@manage_app.route('/delcom/<c_id>')
def manage_delcom(c_id):
    del_comment(c_id)
    return redirect(url_for('manage.manage_index'))

@manage_app.route('/video')
def manage_video(): 
    usr = request.cookies.get('usr')
    uid = request.cookies.get('uid')
    if check_uid(usr, uid):
        if check_admin(usr):
            lines = count_videos()
            datas = get_videos(0, lines)
            return render_template("manage/manage_video.html", usr=usr, uid=uid, datas=datas)
        else:
            return redirect(url_for('main_index'))
    else:
        return redirect(url_for("login.login_index"))

@manage_app.route('/delvid/<v_id>')
def manage_delvid(v_id):
    del_video(v_id)
    return redirect(url_for('manage.manage_video'))

@manage_app.route('/newvid', methods=['POST'])
def add_new_video():
    usr = request.cookies.get('usr')
    uid = request.cookies.get('uid')
    title = request.form['title']
    link = request.form['link']
    ifr = request.form['ifr']
    com = request.form['comment']
    if check_uid(usr, uid) and check_admin(usr):
        insert_video(title, link, ifr, com, usr)
    return redirect(url_for('manage.manage_video'))

