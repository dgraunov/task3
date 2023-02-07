# Запросим 2 целых числа у пользователя и действие над этими числами
flag = True
while flag:
    num1 = int(input('Введите первое целое число: '))
    num2 = int(input('Введите второе целое число: '))
    action = input('Что делаем: +, -, *, / ? ')

# Проверяем что нужно делать и выполняем вычисление
    if action == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif action == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif action == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif action == '/':
        try:
            print(f'{num1} / {num2} = {num1 / num2}')
        except ZeroDivisionError:
            print('На 0 делить нельзя!!!')
    continue_calc = input('Решим еще? (y/n) ')
    if continue_calc == 'n':
        flag = False



