import sqlite3
import os
from .pass_manage import encoding_str, decoding_str
from random import randint

DATA_ROOT = os.path.dirname(os.path.realpath(__file__))
TEST_DB_PATH = os.path.join(DATA_ROOT,'db.sqlite3')

class UsernameNotExists(Exception):
    pass

class WrongPassword(Exception):
    pass

def insert_data(usr, pwd, email, is_admin=0, qid=0, ans=' '):
    connection = sqlite3.connect(TEST_DB_PATH)
    cursor = connection.cursor()
    
    coded = encoding_str(pwd)
    cursor.execute("SELECT MAX(id) FROM usr_db")
    try:
        new_id = int(cursor.fetchone()[0]) + 1
    except TypeError:
        new_id = 1
    try:
        cursor.execute("INSERT INTO usr_db VALUES (?, ?, ?, ?, ?, ?, ?, NULL)", (new_id, usr, coded, email, is_admin, qid, ans))
    except:
        print('DATABASE ERROR!!')
    connection.commit()
    connection.close()

def reset_pwd(usr):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        new_pwd = ''
        for i in range(8):
            new_pwd = new_pwd + chr(randint(64, 122))
        new_pwd_c = encoding_str(new_pwd)
        cs.execute("UPDATE usr_db SET password = ? WHERE username = ?", (new_pwd_c, usr))
        c.commit()
        return new_pwd

def ch_pwd(usr, pwd):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        coded = encoding_str(pwd)
        cs.execute("UPDATE usr_db SET password = ? WHERE username = ?", (coded, usr))
        c.commit()

def insert_uid(usr, uid):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("UPDATE usr_db SET uid = ? WHERE username = ?",(uid, usr))
        c.commit()

def delete_uid(usr):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("UPDATE usr_db SET uid = NULL WHERE username = ?", (usr, ))
        c.commit()

def insert_video(title, link, ifr, com, usr):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT MAX(id) FROM video_info")
        try:
            max_id = cs.fetchone()[0]
        except:
            max_id = 0
        new_id = max_id + 1
        cs.execute("INSERT INTO video_info VALUES (?, ?, ?, ?, ?, ?, datetime('now', '+9 hours'))", (new_id, title, link, ifr, com, usr))
        c.commit()

def del_video(vid):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("DELETE FROM video_info WHERE id = ?", (vid, ))
        c.commit()

def count_videos():
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT COUNT(id) FROM video_info")
        try:
            return int(cs.fetchone()[0])
        except:
            return 0

def get_videos(b=0,e=5):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT * FROM video_info ORDER BY strftime('%Y-%m-%d %H:%M:%S', up_date) DESC LIMIT ?,?", (b, e))
        return cs.fetchall()
# end for video database

def insert_comment(usr, uid, comment):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT id FROM usr_db WHERE username = ? and uid = ?", (usr, uid))
        if cs.fetchone() is None:
            c.close()
            raise UsernameNotExists
        cs.execute("SELECT MAX(id) FROM comments")
        try:
            max_id = cs.fetchone()[0]
            new_id = max_id + 1
        except:
            new_id = 1
        cs.execute("INSERT INTO comments VALUES (?, ?, ?, datetime('now', '+9 hours'))", (new_id, usr, comment))
        c.commit()

def del_comment(cid):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("DELETE FROM comments WHERE id = ?", (cid, ))
        c.commit()

def count_comments():
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT COUNT(id) FROM comments")
        try:
            return int(cs.fetchone()[0])
        except:
            return 0

def get_comments(b=0,e=5):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT * FROM comments ORDER BY strftime('%Y-%m-%d %H:%M:%S', up_date) DESC LIMIT ?,?", (b, e))
        return cs.fetchall()

def get_usr_comments(usr):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT * FROM comments WHERE username = ? ORDER BY strftime('%Y-%m-%d %H:%M:%S', up_date) DESC", (usr, ))
        return cs.fetchall()

def read_data():
    connection = sqlite3.connect(TEST_DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT username FROM usr_db WHERE is_admin = 0")
    resl = cursor.fetchall()
    connection.close()
    return resl

def read_questions():
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT id, question FROM questions")
        return cs.fetchall()

def get_question(usr):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT questions.question FROM questions JOIN usr_db ON usr_db.question = questions.id WHERE usr_db.username = ?", (usr, ))
        res = cs.fetchone()[0]
        return res

def check_usrpwd(usr, pwd):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cursor = c.cursor()
        
        cursor.execute("SELECT password FROM usr_db WHERE username = ?",(usr, ))
        # check usr
        try:
            decoded = decoding_str(cursor.fetchone()[0]).encode('UTF-8')
        except:
            raise UsernameNotExists
        # check password
        if pwd.encode('UTF-8') != decoded:
            raise WrongPassword
        else:
            return True

def check_admin(usr):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cursor = c.cursor()
        cursor.execute("SELECT is_admin FROM usr_db WHERE username = ?", (usr, ))
        i = cursor.fetchone()[0]
        return i == 1

def check_uid(usr, uid):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT uid FROM usr_db WHERE username = ?", (usr, ))
        try:
            uid_g = cs.fetchone()[0]
        except:
            uid_g = '1'
        return uid == uid_g

def check_usreml(usr, email):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT COUNT(*) FROM usr_db WHERE username = ? and email = ?", (usr, email))
        try:
            res = cs.fetchone()[0]
        except:
            res = 0
        return res == 1

def check_ans(usr, ans):
    with sqlite3.connect(TEST_DB_PATH) as c:
        cs = c.cursor()
        cs.execute("SELECT answer FROM usr_db WHERE username = ?", (usr, ))
        get_ans = cs.fetchone()[0]
        return ans == get_ans

