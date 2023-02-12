conf_path = 'C:/python/tasks/task8/conf.ini'

RC_OK = 0
RC_ERROR = -1

def  read_conf():
    with open(conf_path) as f:
        data_dict = {}
        for line in f:
            k, v = line.strip().split('=')
            data_dict[k.strip()] = v.strip()
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
    else:
        rewrite_conf = rewrite_config(user_name, user_passw)


def rewrite_config(user_name, user_passw):
    new_data = user_name + '=' + user_passw
    file = open(conf_path, 'a+')
    file.write('\n' + new_data)
    file.close()



