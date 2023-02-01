while True:
    user_name = input('Введите имя пользователя: ').lower()
    users_list = ['dmitry', 'nikita', 'vasya']
    if user_name in users_list:
        print('Добро пожаловать,', user_name)
    else:
        print('Ты кто такой', user_name, '?')

