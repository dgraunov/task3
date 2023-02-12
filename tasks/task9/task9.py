#Импортируем наш модуль с функциями
import tools
import sys
import re

conf_path = 'C:/python/tasks/task8/conf.ini'

#Определить константы кодов ответа
RC_OK = 0
RC_ERROR = -1

action = input('Что делаем log или reg? ')
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
    user_name = input('Введите login: ')
    result_check_name = tools.check_user_name(user_name)
    if result_check_name == False:
        print('Имя пользователя должно содержать только буквы и цифры')
        sys.exit()

    user_passw = input('Введите password: ')
    result_check_passw = tools.check_user_passw(user_passw)
    if result_check_passw == False:
        sys.exit()
    else:
        reg_result = tools.reg_user(user_name, user_passw)
        print('Поздравляю! Вы успешно зарегистрированы!')


else:
    print('Ошибка! Введите reg или log')
    sys.exit()



