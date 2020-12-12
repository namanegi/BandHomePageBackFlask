from flask import Flask, render_template, make_response, request, redirect, Blueprint, url_for
from data.db_manage import count_videos, get_videos

videolist_app = Blueprint('videolist', __name__)

@videolist_app.route('/')
def videolist_index():
    lines = count_videos()
    p_num = lines // 5 + 1 if lines % 5 != 0 else lines // 5 
    datas = get_videos()
    return render_template("contents/videolist.html", p_num=p_num, datas=datas)

@videolist_app.route('/id=<p_id>')
def videolist_index_p(p_id):
    lines = count_videos()
    p_ = int(p_id)
    datas = get_videos((p_-1)*5,p_*5)
    p_num = lines // 5 + 1 if lines % 5 != 0 else lines // 5
    return render_template("contents/videolist.html", p_num=p_num, datas=datas)
