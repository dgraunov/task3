import sys
#Определить константы кодов ответа
RC_OK = 0
RC_ERROR = -1

#Запросить у пользователя ввод входных параметров
user_name, user_passw = input('login: '), input('password: ')
#Если на вход ничего не передали напечатать ошибку
if user_name == '' or user_passw == '':
    print('Логин и пароль не может быть пустой строкой')
    sys.exit()

#Функция проверки юзера и пароля в словаре
def _login(user_name, user_passw):
    users_prms = {
        'dmitry': '1234',
        'nikita': 'qwert1',
        'vasya': '1111'
    }
    if user_name in users_prms and user_passw == users_prms[user_name]:
        return RC_OK
    else:
        return RC_ERROR

#Вызываем функцию и если код ответа 0 приветсвуем пользователя, иначе шлем его
welcome = _login(user_name,user_passw)
if welcome == 0:
    print('Добро, пожаловать,', user_name)
else:
    print('Давай досвидания')


