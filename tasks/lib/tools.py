import re
import sys
sys.path.insert(0, 'C:/python/tasks/database')
sys.path.insert(0, 'C:/python/tasks/database/users.db')
import db
import sqlite3


conf_path = 'C:/python/tasks/conf.ini'

RC_OK = 0
RC_ERROR = -1

def  read_conf():
    data_dict = {}
    try:
        with open(conf_path) as f:
            for line in f:
                k, v = line.strip().split('=')
                data_dict[k.strip()] = v.strip()
    except Exception as f:
        print(f)

    return data_dict


def login(user_name, user_passw):
    db.cursor.execute('SELECT * FROM users WHERE login = ?', (user_name,))
    result = db.cursor.fetchone()
    if result != None:
        return RC_OK
    else:
        return RC_ERROR

def reg_user(user_name, user_passw):
    db.cursor.execute('SELECT * FROM users WHERE login = ?', (user_name,))
    result = db.cursor.fetchone()
    if result != None:
        print('Пользователь с таким логином уже зарегистрирован')
        sys.exit()
    else:
        sql = 'insert into users(login, password) values(?,?)'
        bind_values = (user_name, user_passw)
        db.cursor.execute(sql, bind_values)
        db.conn.commit()
    return db.conn.total_changes


def rewrite_config(users_list):
    try:
        file = open(conf_path,'w')
        for key, value in users_list.items():
            data = key + '=' + value +'\n'
            file.write(data)
        file.close()
        return True
    except Exception as f:
        print(f)
        return False


def check_user_name(user_name):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]$'
    if re.match(pattern, user_name):
        return True
    else:
        return False

def check_user_passw(user_passw):
    val = True
    if len(user_passw) < 8:
        print('Пароль должен содержать минимум 8 символов')
        val = False
    elif re.search('[0-9]', user_passw) is None:
        print('Убедитесь, что в пароле есть хотя бы одна цифра')
        val = False
    elif re.search('[A-Z]', user_passw) is None:
        print('Убедитесь, что в пароле есть хотя бы одна заглавная буква')
        val = False
    elif re.search('[!@#$%^&*()]', user_passw) is None:
        print('Убедитесь, что пароль содержит хотя бы один из символов: !@#$%^&*()')
        val = False
    elif re.search('[a-zA-Z]', user_passw[0]) is None:
        print('Убедитесь, что пароль начинается с латинской буквы')
        val = False
    return val

def del_user(user_name):
    users_list = read_conf()
    if user_name not in users_list:
        print('Пользователь с таким именем не найден')
    else:
        del users_list[user_name]
        res_del = rewrite_config(users_list)
        print(f'Пользователь {user_name} удален')

def change_passwd(user_name, user_passw):
    users_list = read_conf()
    res_change_passwd = False
    if user_name in users_list:
        users_list[user_name] = user_passw
        res_change_passwd = rewrite_config(users_list)

    return res_change_passwd





