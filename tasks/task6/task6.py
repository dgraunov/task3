conf_path = 'C:/python/tasks/task6/conf.ini'


# Создаем функцию, которая считывает conf.ini и создает словарь
def _read_conf():
    try:
        with open(conf_path) as f:
            data_dict = {}
            for line in f:
                k, v = line.strip().split('=')
                if k[0] == '#':
                    continue
                elif k != '' and v != '':
                    data_dict[k.strip()] = v.strip()
    except Exception as f:
        print(f)
        sys.exit()
    return data_dict

# Вызываем нашу функцию и выводим результат
result_read_conf = _read_conf()
print(result_read_conf)

