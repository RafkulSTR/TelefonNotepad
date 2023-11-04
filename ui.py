from logger import *

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
        while cmd not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            cmd = input("Введите действие:")
        match cmd:
            case "1": enter_data()
            case "2": print_data()
            case "3": search_contact()
            case "4": update_date()
            case "5": print('Всего доброго')