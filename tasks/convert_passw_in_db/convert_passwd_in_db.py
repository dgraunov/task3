import sqlite3
import hashlib

con = sqlite3.connect('C:/python/tasks/database/users.db')
cur = con.cursor()

def get_sha1_hash(user_passw):
    hash_object = hashlib.sha1(user_passw.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

sql = 'select * from users'
cur.execute(sql)
all = cur.fetchall()
for i in all:
    if len(i[2]) == len(get_sha1_hash(i[2])):
        continue
    else:
        sql = 'UPDATE users SET password = ? WHERE login = ?'
        new_pass = get_sha1_hash(i[2])
        data = (new_pass, i[1])
        cur.execute(sql, data)
        con.commit()
