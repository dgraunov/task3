import tools

conf_path = 'C:/python/tasks/task7/conf.ini'

user_name, user_passw = input('login: '), input('password: ')
if user_name == '' or user_passw == '':
    print('error')

users_prms = tools.read_conf()

def login(user_name, user_passw):
    if user_name in users_prms and user_passw == users_prms[user_name]:
        return f'Welcome, {user_name}'
    else:
        return 'Давай досвидания'

a = login(user_name, user_passw)
print(a)


