#Импортируем наш модуль с функциями
#!/usr/bin/env python3
import cgi
print("Content-type: text/html\n")
import sys
sys.path.insert(0, 'C:/python/tasks/lib')
sys.path.insert(0, 'C:/python/tasks/database')
import tools
import db
import re
import sqlite3
form = cgi.FieldStorage()
login = form.getfirst('user_name')
passw = form.getfirst('user_passw')
action = form.getvalue('action')
passw2 = form.getfirst('user_passw2')



#Определить константы кодов ответа
RC_OK = 0
RC_ERROR = -1

if action == 'log':
    # Запросить у пользователя ввод входных параметров
    user_name, user_passw = login, passw

    # Если на вход ничего не передали напечатать ошибку
    if user_name == '' or user_passw == '':
        print('Логин и пароль не может быть пустой строкой')
        sys.exit()

    # Вызываем функцию и если код ответа 0 приветсвуем пользователя, иначе шлем его
    login_result = tools.login(user_name, user_passw)
    if login_result == RC_OK:
        print('Добро пожаловать,', user_name)
    else:
        print('Давай досвидания')

elif action == 'reg':
    # Запросить у пользователя ввод входных параметров
    user_name, user_passw = login, passw
    result_check_name = tools.check_user_name(user_name)
    if result_check_name == False:
        print('Имя пользователя должно содержать только буквы и цифры')
        sys.exit()

    if passw == passw2:
        pass
    else:
        print('Пароли не совпадают')
        sys.exit()

    result_check_passw = tools.check_user_passw(user_passw)
    if result_check_passw == True:
        hash_user_passw = tools.get_sha1_hash(user_passw)
        reg_result = tools.reg_user(user_name, hash_user_passw)
        if reg_result == RC_OK:
            print('Поздравляю! Вы успешно зарегистрированы!')
        else:
            print('Что то пошло не так')
    else:
        sys.exit()

elif action == 'del':
    user_name = input('Введите имя пользователя, которого надо удалить: ')
    result_del = tools.del_user(user_name)
    if result_del == RC_OK:
        print(f'Пользователь {user_name} удален')
    else:
        print('Пользователь с таким именем не найден')

elif action == 'change_passwd':
    user_name = input('Введите имя пользователя, которому меняем пароль: ')
    db.cursor.execute('SELECT * FROM users WHERE login = ?', (user_name,))
    check_user = db.cursor.fetchone()
    if check_user != None:
        user_passw = input('Введите новый пароль: ')
        check_passw = tools.check_user_passw(user_passw)
        if check_passw == True:
            res_change_passw = tools.change_passwd(user_name, user_passw)
            if res_change_passw == RC_OK:
                print('Пароль успешно изменен')
            else:
                print('Ошибка при смене пароля')
    else:
        print('Пользователь с таким именем не найден ')
        sys.exit()

else:
    print('Ошибка! Введите reg, log, del или change_passwd')
    sys.exit()



