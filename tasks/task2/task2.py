from sys import argv



user_name, user_passw = argv[1], argv[2]
users_list = ['dmitry', 'nikita', 'vasya']
if user_name in users_list:
    print('Добро пожаловать,', user_name)
    print('Твой пароль:', user_passw)
else:
    print('Ты кто такой', user_name, '?')

