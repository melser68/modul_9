
#Доступні функції операцій з введенними даними
def sum_func (x,y):
    return x +y

def substr_func(x,y):
    return x-y

def delenie_func(x,y):
    try:
        return x/y
    except:
         return print('Ділення на "0"')

def umnojenie_func(x,y):
    return x * y

#Виклик відповідної введеному оператору функції
def get_operator(operator):
    if operator == '+':
        return sum_func
    elif operator == '-':
        return substr_func
    elif operator == '/':
        return delenie_func
    elif operator == '*':
        return umnojenie_func
    else:
        return print('Введений оператор невідомий')

#Основна процедура
def main():
    
    if w == 'yes':
        a = float(input('Введіть перше число: '))
        b = float(input('Введіть друге число: '))
        c = input('Введіть оператор: ')
        action_func = get_operator(c)
        
        if isinstance(action_func(a,b), (int, float)) == False:
            print('_________________________________')
            print('Попитка провести некоректну операцію, спробуйте ще раз ввести дані')
            print('_________________________________')
            main()
        else:
            print('_________________________________')
            print('Результат операції: ', action_func(a,b))
            print('_________________________________')
            r = input('Провести розрахунок ще раз - "r", вихід з програми "exit": ')
            if r == 'r':
                main()
    elif w == 'exit':
        print('Вихід з програми.')


print('Старт програми елементарного калькулятора')
w = input('Підтвердження старту (yes), закінчення роботи (exit): ')
main()

