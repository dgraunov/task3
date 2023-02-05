conf_path = 'C:/python/tasks/task7/conf.ini'

def  read_conf():
    with open(conf_path) as f:
        data_dict = {}
        for line in f:
            k, v = line.strip().split('=')
            data_dict[k.strip()] = v.strip()
    return data_dict




