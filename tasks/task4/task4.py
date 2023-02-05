user_name, user_passw = input('login: '), input('password: ')
if user_name == '' or user_passw == '':
    print('error')
users_prms = {
    'dmitry': '1234',
    'nikita': 'qwert1',
    'vasya': '1111'
}


def _login(user_name, user_passw):
    if user_name in users_prms and user_passw == users_prms[user_name]:
        return f'Welcome, {user_name}'
    else:
        return 'Давай досвидания'

a = _login(user_name,user_passw)
print(a)


