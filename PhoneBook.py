'''на Отлично в одного человека надо сделать консольное приложение Телефонный справочник 
с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр,
сохранение, импорт, поиск, удаление. 
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения 
и удаления данных.'''

import random, json, os, os.path
def AddNewContact():
    number_of_telNumbrs:int = 1
    name = input("Введите имя нового контакта: ")
    tel_number:list=[]
    while True:
        number = input(f"Введите {number_of_telNumbrs}й номер телефона. Если его нет нажмите  Enter: ")
        if number!='':
            tel_number.append(number)
            number_of_telNumbrs+=1
        else:
            break
    bith_day = input("Введите ДР: ")
    mail = input("Введите email: ")
    value = {"phone_numbers": tel_number, "birth_day": bith_day, "email": mail}
    return [name,value]
def Save():
    with open("phone_book.json", "w+", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    print("Телефонная книга обновлена")
def Load():
    if os.path.getsize('phone_book.json')==0:
        print('книга пуста')
        phone_book = dict()
        return phone_book
    with open("phone_book.json", "r", encoding="utf-8") as fh:
            phone_book = json.load(fh)
    print("Загрузка контактов выполнена успешно")
    return phone_book
def Delete():
    with open("phone_book.json", "r", encoding="utf-8") as fh:
        phone_book = dict(json.load(fh))
    os.system('cls')
    print(*phone_book)
    name = input("Введите имя контакта для удаления: ")
    while name not in phone_book:
        name=input(f"Конакта {name} нет в телефонной книге.\
                   Введите имя контакта из телефонной книги для удаления: ")
    os.system('cls')
    print(f"Контакт {name} будет удален из телефонной книги")
    phone_book.pop(name)
    return  phone_book
def EditContact(phone_book:dict)->dict:
    name_for_change = input("Введите имя контакта для изменения: ")
    while name_for_change not in phone_book:
        name_for_change=input(f"Конакта {name_for_change} нет в телефонной книге.\
                   Введите имя контакта из телефонной книги для изменения: ")
    name = name_for_change
    contact_data:dict=phone_book[name]
    phone_number:list=contact_data['phone_numbers']
    birth_day = contact_data['birth_day']
    email = contact_data['email']
    phone_book.pop(name)
    value = {"phone_numbers": phone_number, "birth_day": birth_day, "email": email}
    os.system('cls')
    while True:
        print('Что именно хотите поменять в контакте: ')
        print(f'1 - Имя - {name}')
        print(f'2 - Телефон - {phone_number} ')
        print(f'3 - Дату рождения - {birth_day}')
        print(f'4 - Электронную почту - {email}')
        print(f'5 - Сохранить изменения и выйти - {name}: {value} ')
        command = input('Введите номер команды для изменения контакта')
        if command == '1':
            os.system('cls')
            print(f'1 - Имя - {name}')
            name = input("Введите новое имя контакта: ")
        elif command == '2':
            os.system('cls')
            print(f'2 - Телефон - {phone_number} ')
            number_of_phoneNumber=1
            phone_number=[]
            while True:
                number = input(f"Введите {number_of_phoneNumber}й номер телефона. Если его нет нажмите  Enter: ")
                if number!='':
                    phone_number.append(number)
                    number_of_phoneNumber+=1
                else:
                    break
        elif command=='3':
            os.system('cls')
            print(f'3 - Дату рождения - {birth_day}')
            birth_day = input('Введите новую дату рождения: ')
        elif command=='4':
            os.system('cls')
            print(f'4 - Электронную почту - {email}')
            email = input('Введите новый адрес электронной почты: ')
        elif command=='5':
            break            
    value = {"phone_numbers": phone_number, "birth_day": birth_day, "email": email}
    phone_book[name]=value 
    os.system('cls')
    print(f"Контакт {name} был изменен")
    return  phone_book
def Menu():
    print('1 - Add New Contact')
    print('2 - Delete Contact')
    print('3 - Contact search')
    print('4 - Show all contacts')
    print('5 - Edit contact')
    print('6 - Exit')



    
os.system('cls')
phone_book:dict = Load()
while True:
    Menu()
    command = input("Введите номер команды: ")
    if command == "1":
        new_contact:list=AddNewContact()
        name=new_contact[0]
        value=new_contact[1]
        phone_book[name] = value 
        os.system('cls')
        print("Контакт добавлен")
        Save()     
    elif command == "4":
        os.system('cls')
        print("Список всех контактов")
        print(phone_book)
    elif command == "3":
        os.system('cls')
        name = input("Введите имя для поиска: ")
        if name in phone_book:
            print(name, phone_book[name])
    elif command == "2":
        phone_book=Delete()
        Save()
    elif command =="5":
        EditContact(phone_book)
        Save()
    elif command == '6':
        break