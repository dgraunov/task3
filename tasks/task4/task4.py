import sys

RC_OK = 0
RC_ERROR = -1

user_name, user_passw = input('login: '), input('password: ')
if user_name == '' or user_passw == '':
    print('error')
    sys.exit()

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

a = _login(user_name,user_passw)
if a == 0:
    print('Добро, пожаловать,', user_name)
else:
    print('Давай досвидания')


