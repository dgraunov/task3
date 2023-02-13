import re
import sys

conf_path = 'C:/python/tasks/conf.ini'

RC_OK = 0
RC_ERROR = -1

def  read_conf():
    try:
        with open(conf_path) as f:
            data_dict = {}
            for line in f:
                k, v = line.strip().split('=')
                data_dict[k.strip()] = v.strip()
    except Exception as f:
        print(f)
        sys.exit()

    return data_dict


def login(user_name, user_passw):
    users_prms = read_conf()
    if user_name in users_prms and user_passw == users_prms[user_name]:
        return RC_OK
    else:
        return RC_ERROR

def reg_user(user_name, user_passw):
    users_list = read_conf()
    if user_name in users_list:
        print('Пользователь с таким логином уже зарегистрирован')
        sys.exit()
    else:
        users_list[user_name] = user_passw
        return users_list


def rewrite_config(users_list):
    file = open(conf_path,'w')
    for key, value in users_list.items():
        data = key + '=' + value +'\n'
        file.write(data)
    file.close()

def check_user_name(user_name):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]$'
    if re.match(pattern, user_name):
        return True
    else:
        return False

def check_user_passw(user_passw):
    val = True
    if len(user_passw) < 8:
        print('Пароль должен содержать минимум 8 символов')
        val = False
    elif re.search('[0-9]', user_passw) is None:
        print('Убедитесь, что в пароле есть хотя бы одна цифра')
        val = False
    elif re.search('[A-Z]', user_passw) is None:
        print('Убедитесь, что в пароле есть хотя бы одна заглавная буква')
        val = False
    elif re.search('[!@#$%^&*()]', user_passw) is None:
        print('Убедитесь, что пароль содержит хотя бы один из символов: !@#$%^&*()')
        val = False
    elif re.search('[a-zA-Z]', user_passw[0]) is None:
        print('Убедитесь, что пароль начинается с латинской буквы')
        val = False
    return val

def del_user(user_name):
    users_list = read_conf()
    if user_name not in users_list:
        print('Пользователь с таким именем не найден')
    else:
        del users_list[user_name]
        res_del = rewrite_config(users_list)
        print(f'Пользователь {user_name} удален')



