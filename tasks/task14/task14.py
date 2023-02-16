#Импортируем наш модуль с функциями
import sys
sys.path.insert(0, 'C:/python/tasks/lib')
sys.path.insert(0, 'C:/python/tasks/database')
import tools
import db
import re

conf_path = 'C:/python/tasks/conf.ini'

#Определить константы кодов ответа
RC_OK = 0
RC_ERROR = -1

action = input('Что делаем log, reg, del, change_passwd? ')
if action == 'log':
    # Запросить у пользователя ввод входных параметров
    user_name, user_passw = input('login: '), input('password: ')

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
    user_name, user_passw = input('Введите login: '), input('Введите password: ')
    result_check_name = tools.check_user_name(user_name)
    if result_check_name == False:
        print('Имя пользователя должно содержать только буквы и цифры')
        sys.exit()

    result_check_passw = tools.check_user_passw(user_passw)
    if result_check_passw == False:
        sys.exit()
    else:
        reg_result = tools.reg_user(user_name, user_passw)
        res_rewrite = tools.rewrite_config(reg_result)
        print('Поздравляю! Вы успешно зарегистрированы!')

elif action == 'del':
    user_name = input('Введите имя пользователя, которого надо удалить: ')
    result_del = tools.del_user(user_name)

elif action == 'change_passwd':
    user_name = input('Введите имя пользователя, которому меняем пароль: ')
    check_user = tools.read_conf()
    if user_name in check_user:
        user_passw = input('Введите новый пароль: ')
        check_passw = tools.check_user_passw(user_passw)
        if check_passw == True:
            res_change_passw = tools.change_passwd(user_name, user_passw)
            if res_change_passw == True:
                print('Пароль успешно изменен')
            else:
                print('Ошибка при смене пароля')
    else:
        print('Пользователь с таким именем не найден ')
        sys.exit()

else:
    print('Ошибка! Введите reg, log, del или change_passwd')
    sys.exit()
