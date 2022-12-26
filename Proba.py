def get_operator(operator):
    if operator == '+':
        return 1
    elif operator == '-':
        return 2
    elif operator == '/':
        return 3
    elif operator == '*':
        return 4
    else:
        return print('Введений оператор невідомий')

a = input('Введіть оператор: ')
get_operator(a)
print(type(get_operator) != int)
