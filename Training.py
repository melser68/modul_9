
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
def main(w):
    
    if w == 'yes':
        a = float(input('Введіть перше число: '))
        b = float(input('Введіть друге число: '))
        c = input('Введіть оператор: ')
        action_func = get_operator(c)
        
        if type(action_func) != int or type(action_func) != float:
            print('_________________________________')
            r = input('Спроба провести некоректну операцію, повторити ? - "yes" Вихід з програми "exit": ')
            print('_________________________________')
            if  r == 'yes':
                main(r)
            else:
                w = 'exit'
                print('Вихід з програми.')
        else:
            print('_________________________________')
            print('Результат операції: ', action_func(a,b))
            print('_________________________________')
            r = input('Провести розрахунок ще раз - "r", вихід з програми "exit": ')
            if r == 'r':
                main(r)
            else:
                print('Вихід з програми.')
    elif w == 'exit':
        print('Вихід з програми.')


print('Старт програми елементарного калькулятора')
w = input('Підтвердження старту (yes), закінчення роботи (exit): ')
main(w)

