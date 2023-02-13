#Импортируем наш модуль с функциями
import tools
import sys
import re

conf_path = 'C:/python/tasks/conf.ini'

#Определить константы кодов ответа
RC_OK = 0
RC_ERROR = -1

action = input('Что делаем log, reg, del? ')
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

else:
    print('Ошибка! Введите reg, log или del')
    sys.exit()


