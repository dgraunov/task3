#Импортируем наш модуль с функциями
import tools
import sys

conf_path = 'C:/python/tasks/task7/conf.ini'

#Определить константы кодов ответа
RC_OK = 0
RC_ERROR = -1

#Запросить у пользователя ввод входных параметров
user_name, user_passw = input('login: '), input('password: ')

#Если на вход ничего не передали напечатать ошибку
if user_name == '' or user_passw == '':
    print('Логин и пароль не может быть пустой строкой')
    sys.exit()

#Вызываем функцию и если код ответа 0 приветсвуем пользователя, иначе шлем его
login_result = tools.login(user_name,user_passw)
if login_result == RC_OK:
    print('Добро пожаловать,', user_name)
else:
    print('Давай досвидания')



