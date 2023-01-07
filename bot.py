import os


dict_phone = {}
#Заповнюємо словник існуючими контактами
def fill_dict_phone():
    file_book = open('phonebook.msf')
    line_count = sum(1 for line in open('phonebook.msf'))
    
    if line_count >0:
        for i in file_book:
            key, value = i.split(' , ')
            dict_phone[key] = value[:-1]
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
    name = ''
    while check_correct == False:
        while name_contact == False:
            name = input("Введи ім'я контакту:  ")
            try:
                int(name[1])
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
            phonebook = open('phonebook.msf','a+' )
            phonebook.write(str(rez[0]) + ' , '+ str(rez[1]))
            phonebook.write('\n')
            phonebook.close()
        else:
            print('Введено некоректні дані, повтори ввод')

#Виведення збереженного списку контактів
def print_phone():
    os.system('CLS')
    for name_book, number_book in dict_phone.items():
        print ('Контакт: ', name_book , '  ' 'Номер телефону: ', number_book)
#Зміна номеру телефону у збереженного контакта
def change_phone(name_search, new_number):
    if len(dict_phone) == 0:
        fill_dict_phone()
    for name_book, number_book in dict_phone.items():
        if name_search == name_book:
            if check_contact(name_search, new_number) != False:
                dict_phone.update({name_book:new_number})
                os.system('CLS')
                print('Змінено дані:\nКонтакт: == ', name_book, ' новий номер телефону: == ', new_number)            
                phonebook = open('phonebook.msf', 'w')
                for i,y in dict_phone.items():
                    phonebook.write(i + ' , ' + y)
                    phonebook.write('\n')
                phonebook.close()


#Пошук існуючого контакту, або контактів у довіднику
def search_kontakts(name_list):
    rez_search = {}
    for y in name_list:
        for kontakt, num_tel in dict_phone.items():
            if kontakt.lower().find(y) != -1:
                rez_search.update({kontakt:num_tel})    
    return(rez_search)

#Видалення контакту з довідника контактів
def del_kontakts(name_kontakt):
    if len(dict_phone) == 0:
        fill_dict_phone()
    for name_search_1 in dict_phone:
        if name_kontakt == name_search_1:
            dict_phone.pop(name_search_1)
            break
    phonebook = open('phonebook.msf', 'w+')
    for key, data in dict_phone.items():
        phonebook.write(key + ' , ' + data)
        phonebook.write('\n')
    phonebook.close()
    
    



#Основна процедура
def main():
    activate_menu = False
    print('Вітаю. Це бот помічник. Для початку роботи введи "hello"')
    print('Для завершення роботи любе слово яким ти користуєшся при прощанні')
    command = input(':  ').lower()    
    if hello_and_goodbay(command) == 'enter':
        os.system('CLS')
        print('How can I help you?')
        activate_menu = True
        mode_menu = True
        
    while activate_menu == True:        
        if mode_menu == True:
            os.system('CLS')
            print('Початкове меню.')
            print('1. Я можу створити для тебе книгу контактів з номерами телефонів\n та надавати тобі звідти інформацію.')
            print('2. Бізнес-календар зараз в стадії розробки sorry')
            print('3. Вихід "0"')
            chois_menu = input('Бажаєш розпочати роботу ? (введи номер відповідного пункту меню):  ')
                       
        if chois_menu == '1':
            os.system('CLS')
            menu_telefon = True
            fill_dict_phone() 
            chois_phone = ''       
            while menu_telefon == True:
                fill_dict_phone()                    
                print('OK\nЯкщо бажаєш додати новий контакт то введи "add"\n' 
                'Якщо бажаєш змінити або доповнити існуючий контакт то введи "change"\nЯкщо бажаєш продивитися усі контакти  то введи "show all"\n'
                'Видалити контакт "del"\n'
                'Повернення у попереднє меню введи "0"')
                if chois_phone == '':
                    chois_phone = input(': ')
                if chois_phone == 'add':
                    input_contact()
                    tel_menu = input('Повернутися до меню телефонної книги ? (yes/no): ').lower()
                    if tel_menu == 'no':
                        menu_telefon = False
                    else:
                        os.system('CLS')
                        chois_phone = ''
                elif chois_phone == 'change':
                    
                    name_search = input("Введіть ім'я контакту номер якого потрібно змінити:  ").lower() 
                    name_list = name_search.split(' ')
                    rezultat = search_kontakts(name_list)
                    if len(rezultat) >=1:
                        print('Знайдено похожі контакти : ')
                        for k,s in rezultat.items():
                            print(k,' ', s)
                        name_search = input("Введи ім'я контакту номер якого бажаєш змінити\n: ").lower()
                        name_list = name_search.split(':')
                        rezultat = search_kontakts(name_list)
                        if len(rezultat) ==1:
                            for name in rezultat.keys():
                                new_number = input(f'Введіть новий номер для {name}:\nПриклад: +38-067-2972960:  ')
                                rez = check_contact(name, new_number)
                                if rez != False:
                                    change_phone(name, new_number)
                                    chois_phone = ''
                                else:
                                    print('Некоректний номер телефону, повтор введення')
                                    chois_phone = 'change'
                    else:
                        q = input('За введеним значенням контактів не знайдено. Повторити пошук ? (yes/no)')
                        if q == 'yes':
                            chois_phone = 'change'
                        else:
                            chois_phone = '0'
                            continue

                elif chois_phone == 'del':

                    name_search = input(
                        "Введи ім'я контакту номер якого потрібно видалити:  ").lower()
                    name_list = name_search.split(' ')
                    rezultat = search_kontakts(name_list)
                    if len(rezultat) >= 1:
                        print('Знайдено похожі контакти : ')
                        for k, s in rezultat.items():
                            print(k, ' ', s)
                        name_search = input(
                            "Введи ім'я контакту номер якого бажаєш видалити\n: ").lower()
                        name_list = name_search.split(':')
                        rezultat = search_kontakts(name_list)
                        if len(rezultat) == 1:
                            for name in rezultat.keys():
                                respond = input(f'Буде видалено контакт {name}:\n"(yes/no)":  ')
                                if respond == 'yes':
                                    del_kontakts(name)
                                    chois_phone = ''
                                else:
                                    print('Операція відмінена')
                                    os.system('CLS')
                                    chois_phone = '0'
                                    continue
                    else:
                        q = input(
                            'За введеним значенням контактів не знайдено. Повторити пошук ? (yes/no)')
                        if q == 'yes':
                            chois_phone = 'change'
                        else:
                            chois_phone = '0'
                            continue
                    
                elif chois_phone == 'show all':
                    print_phone()
                    tel_menu = input('Повернутися до меню телефонної книги ? (yes/no): ').lower()
                    if tel_menu == 'no':
                        menu_telefon = False
                    else:
                        os.system('CLS')
                        chois_phone = ''
                            
                elif chois_phone == '0':
                    os.system('CLS')
                    
                    menu_telefon = False
                    chois_phone = ''
                else:
                    os.system('CLS')
                    print(f'Команда "{chois_phone}" не розпізнана')
                    tel_menu = input('Повернутися до меню телефонної книги ? (yes/no): ').lower()
                    if tel_menu == 'no':
                        menu_telefon = False
                    else:
                        os.system('CLS')
                        chois_phone = ''
        else:            
            activate_menu = False
            mode_menu = 'no'

    else:
        print('== Good bye! ==')
        activate_menu = False


main()
