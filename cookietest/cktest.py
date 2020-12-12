from flask import Flask, url_for, Blueprint, request, make_response, redirect, render_template

cookie_app = Blueprint('cktest', __name__)

@cookie_app.route('/')
def cktest_index():
    resp = make_response()
    resp.set_cookie('test1', 'test2')
    return render_template("cktest/cktest.html")

@cookie_app.route('/test')
def read_ck():
    mess = request.cookies.get('test1')
    return redirect(url_for('cktest.cktest_index', mess=mess))
