# Запросим 2 целых числа у пользователя и действие над этими числами
flag = True
while flag:
    num1 = input('Введите первое целое число: ')
    if num1.isdigit() == False:
        continue
    num2 = input('Введите второе целое число: ')
    if num2.isdigit() == False:
        continue
    action = input('Что делаем: +, -, *, / ? ')
    if action not in ['+', '-', '*', '/']:
        continue

# Проверяем что нужно делать и выполняем вычисление
    if action == '+':
        print(f'{num1} + {num2} = {int(num1) + int(num2)}')
    elif action == '-':
        print(f'{num1} - {num2} = {int(num1) - int(num2)}')
    elif action == '*':
        print(f'{num1} * {num2} = {int(num1) * int(num2)}')
    elif action == '/':
        try:
            print(f'{num1} / {num2} = {int(num1) / int(num2)}')
        except ZeroDivisionError:
            print('На 0 делить нельзя!!!')
    continue_calc = input('Решим еще? (y/n) ')
    if continue_calc == 'n':
        flag = False



