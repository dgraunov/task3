conf_path = 'C:/python/tasks/task5/conf.ini'
#Создаем функцию, которая считывает conf.ini и создает словарь
def  _read_conf():
    with open(conf_path) as f:
        data_dict = {}
        for line in f:
            k, v = line.strip().split('=')
            data_dict[k.strip()] = v.strip()
    return data_dict
