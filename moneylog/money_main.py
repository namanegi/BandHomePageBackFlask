import os
import json
import datetime
from flask import Flask, render_template, redirect, request, Blueprint

DATA_FILE = 'moneylog/moneylog.json'

money_app = Blueprint('moneylog', __name__)

@money_app.route('/send', methods=['POST'])
def save():
        """Get data from input form"""
        io = request.form['datatype']
        money = int(request.form['money'])
        ti = request.form['time']
        com = request.form['comment']
        save_data(io, money, ti, com)
        return redirect('/money')

def save_data(io: str, money: int, ti: str, com: str):
        """Save data
        io-----datatype
        money---money
        ti-----time
        com----comment
        return: none
        """

        try:
                with open(DATA_FILE, mode="r", encoding="UTF-8") as f:
                        database = json.load(f)
        except:
                        database = []
                        database.insert(0, {
                                "datatype": "income",
                                "money": 100000,
                                "Remain": 100000,
                                "time": datetime.datetime(2000, 1, 1).strftime("%Y-%m-%d %H:%M"),
                                "comment": ""
                                })

        remain = database[0]["Remain"]
        money = money if io == 'income' else (0 - money)
        database.insert(0, {
                "datatype": io,
                "money": money,
                "Remain": remain + money,
                "time": ti,
                "comment": com
                })

        with open(DATA_FILE, mode="w", encoding="UTF-8") as f:
                json.dump(database, f, indent=4, ensure_ascii=False)

def load_data():
        """load log from json file
        return dic"""
        try:
                with open(DATA_FILE, mode="r", encoding="UTF-8") as f:
                        database = json.load(f)
        except:
                database = []
                database.insert(0, {
                        "datatype": "income",
                        "money": 100000,
                        "Remain": 100000,
                        "time": datetime.datetime(2000, 1, 1).strftime("%Y-%m-%d %H:%M"),
                        "comment": ""
                        })
        return database

@money_app.route('/money')
def index():
        """for top page"""
        rides = load_data()
        return render_template("moneylog/money.html", rides=rides)

@money_app.route('/delete')
def delete():
    """delete all log"""
    if os.path.exists(DATA_FILE) == True:
    	os.remove(DATA_FILE)
    return redirect('/money')

if __name__ == '__main__':
        money_app.run('0.0.0.0', 8000, debug=True)
