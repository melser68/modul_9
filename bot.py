
dict_phone = {}
#Заповнюємо словник існуючими контактами
def fill_dict_phone():
    file_book = open('phonebook.txt')
    line_count = sum(1 for line in open('phonebook.txt'))
    
    if line_count >0:
        for i in file_book:
            key, value = i.split('  ')
            dict_phone[key] = value[:-2]
    file_book.close()

#Ведення логу введених даних
def decorator_logger(func):
    def inner(x, y):
        print(f'Введено дані {x}, {y}')
        result = func(x, y)
        return result
    return inner
#Реакція на вході в програму
def hello_and_goodbay(command):    
    if command == 'hello':
        return 'enter'
#Перевірка на коректність телефонного номеру
def phone_book (name, num):
    list_check_phone = num.split('-')
    list_section= list()
    lang = 0
    for i in list_check_phone:
        lang += len(i)
        list_section.append(len(i))    
    if lang == 13 and list_section == [3,3,7]:
        return True        
    else:
        return False
#Відповідь на коректність введеного номеру       
@decorator_logger
def check_contact(name, num):    
    if phone_book(name, num) == True:
        return name, num        
    else:
       return False
#Створення контакту в телефонній книзі
def input_contact():
    check_correct = False
    name_contact = False
    while check_correct == False:
        while name_contact == False:
            name = input("Введи ім'я контакту:  ")
            try:
                type(int(name[0])) == int
                name_contact = False
                print('Спроба вводу номеру замість імені, повторіть введення')
            except:
                name_contact = True
        print('Введи номер телефону контакта у форматі "код країни - код оператора - номер"\nПриклад: +38-067-2972960:  ')
        num = input(':  ')
        rez = check_contact(name, num)
        if rez != False:
            dict_phone.update({rez[0]: rez[1]})            
            print('Прийнято дані:\nКонтакт: == ',rez[0], ' номер телефону: == ', rez[1])
            check_correct = True
            phonebook = open('phonebook.txt','a+' )
            phonebook.write(rez[0] + '  '+ rez[1])
            phonebook.write('\n')
            phonebook.close()
        else:
            print('Введено некоректні дані, повтори ввод')





#Основна процедура
def main():
    activate_menu = False
    print('Вітаю. Це бот помічник. Для початку роботи введи "hello"')
    print('Для завершення роботи любе слово яким ти користуєшся при прощанні')
    command = input(':  ').lower()    
    if hello_and_goodbay(command) == 'enter':
        activate_menu = True
        mode_menu = 'yes'
    while activate_menu == True:        
        if mode_menu == 'yes':
            print('1. Я можу створити для тебе книгу контактів з номерами телефонів\n та надавати тобі звідти інформацію.')
            print('2. Бізнес-календар зараз в стадії розробки sorry')
            chois_menu = input('Бажаєш розпочати роботу ? (введи номер відповідного пункту меню):  ')
            menu_telefon = True            
            if chois_menu == '1': 
                fill_dict_phone()
                print(dict_phone)
                while menu_telefon == True:
                    fill_dict_phone()
                    print(dict_phone)
                    print('OK\nЯкщо бажаєш додати новий контакт то введи "1"\n' 
                    'Якщо бажаєш змінити або доповнити існуючий контакт "2"\nЯкщо бажаєш продивитися усі контакти "3"')
                    chois_phone = input(' ')
                    if chois_phone == '1':
                        input_contact()
                        tel_menu = input('Повернутися до меню телефонної книги ? (yes/no)').lower()
                        if tel_menu == 'no':
                            menu_telefon = False
                    elif chois_phone == '2':
                        print('Розробляється')  
                    elif chois_phone == '3':
                        print('Розробляється') 
    else:
        print('== Good bye! ==')
        activate_menu = False


main()
