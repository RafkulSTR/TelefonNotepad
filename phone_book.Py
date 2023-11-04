# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def enter_first_name():
    return input('Введите имя абонента: ').capitalize()

def enter_second_name():
    return input('Введите фамилию абонента: ').capitalize()

def enter_family_name():
    return input('Введите отчество абонента: ').capitalize()

def enter_phone_number():
    return input('Введите номер абонента: ')


def enter_address_abonent():
    return input('Введите адрес абонента: ')


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
    update = input('Введите на что меняем')
    with open('book.txt', 'r', encoding='utf8') as file:
        file.seek(0)
        list_contact = file.read().strip().split('\n\n')
        for i in range(len(list_contact)):
            if str in list_contact[i][index]:
                list_contact[i][index] = update
    # with open('book.txt', 'w', encoding='utf8') as file:
    #     file.write(*list_contact)
    print(*list_contact)

    

def interface():
    cmd = 0
    while cmd != '5':
        print('Варианты действий:\n'
            '1. Добавить контакт\n'
            '2. Вывести все контакты\n'
            '3. Поиск контакта\n'
            '4. Изменить контакт\n'
            '5. Выход')
        cmd = input("Введите действие:")
        while cmd not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            cmd = input("Введите действие:")
        match cmd:
            case "1": enter_data()
            case "2": print_data()
            case "3": search_contact()
            case "4": update_date()
            case "5": print('Всего доброго')


interface()


    