conf_path = 'C:/python/tasks/task7/conf.ini'

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

