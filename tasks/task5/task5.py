conf_path = 'C:/python/tasks/task5/conf.ini'
#Считываем файл conf.ini
def  _read_conf():
    try:
        with open(conf_path) as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print('Файл не найден')
    return lines

