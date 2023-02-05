from sys import argv



user_name, user_passw = argv[1], argv[2]
users_prms = {
    'dmitry': '1234',
    'nikita': 'qwert1',
    'vasya': '1111'
}
if user_name in users_prms and user_passw == users_prms[user_name]:
    print('Добро пожаловать,', user_name)
else:
    print('Неверный логин или пароль.')