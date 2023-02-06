import sys


conf_path = 'C:/python/tasks/task5/conf.ini'
#Считываем файл conf.ini
def  _read_conf():
    try:
        with open(conf_path) as f:
            lines = f.read().splitlines()
    except Exception as f:
        print(f)
        sys.exit()
    return lines

a = _read_conf()
print(a)

