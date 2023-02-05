conf_path = 'C:/python/tasks/task5/conf.ini'

def  _read_conf():
    with open(conf_path) as f:
        lines = f.read().splitlines()
    return lines

