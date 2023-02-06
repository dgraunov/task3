import sys


conf_path = 'C:/python/tasks/task5/conf.ini'
# Пишем функцию, которая считывает файл conf.ini и обрабатывает исключения
def  _read_conf():
    try:
        with open(conf_path) as f:
            lines = f.read().splitlines()
    except Exception as f:
        print(f)
        sys.exit()
    return lines

# Вызываем нашу функцию и выводим результат
result_read_conf = _read_conf()
print(result_read_conf)

