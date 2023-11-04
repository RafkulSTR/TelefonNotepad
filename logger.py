from data_create import *

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    famali = enter_family_name()
    number = enter_phone_number()
    address = enter_address_abonent()
    with open('book.txt', 'a', encoding='utf8') as file:
        file.write(f'{name} {surname} {famali}\n{number}\n{address}\n\n')

def print_data():
     with open('book.txt', 'r', encoding='utf8') as file:
         print(file.read())


def search_contact():
    print('Выбирите вариант поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант:'))

    str = input('Введите искомое данное: ').title()
    with open('book.txt', 'r', encoding='utf8') as file:
        file.seek(0)
        list_contact = file.read().strip().split('\n\n')
        #print(list_contact)
        for val in list_contact:
            val = val.replace('\n',' ').split()
            if str in val[index-1]: 
                print(*val)
                print()


def update_date():
    print('Выбирите вариант изменения:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант:'))
    str = input('Введите искомое данное: ').title()
    update = input('Введите на что меняем: ')
    with open('book.txt', 'r', encoding='utf8') as file:
        file.seek(0)
        list_contact = file.read().strip().split('\n\n')
        for i in range(len(list_contact)-1):
            if str in list_contact[i][index-1]:
                list_contact[i][index-1] = update
    with open('book.txt', 'w', encoding='utf8') as file:
        for item in list_contact:
            file.write(str(item) + "\n")     
    