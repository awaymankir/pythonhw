def print_menu():
    print('\n1. Открыть txt-файл телефонной книги')
    print('2. Показать телефонную книгу')
    print('3. Сохранить изменения в телефонной книге (txt)')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')


def input_choice_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(0, 8):
                return choice
            else:
                print('Введите число согласно нумерации пунктов меню!')
        except:
            print('Введите корректное значение пункта меню!')


def out_of_menu():
    print('Спасибо, до свидания!')


def print_phone_book(new_phone_book: list):
    if len(new_phone_book) > 0:
        for id, item in enumerate(new_phone_book, 1):
            print(id, *item)  # * - это распаковка списка, когда выводит на печать только его элементы, без [] и запятых
    else:
        print('Телефонная книга пуста!')


def print_open_db():
    print('Txt-файл с телефонной книгой открыт, книга может быть отображена.')


def print_save_db():
    print('Txt-файл с телефонной книгой обновлен.')


def print_add_contact():
    print()
    print('Новый контакт добавлен.')


def new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите номер телефона: ')
    other = input('Введите доп.информацию: ')
    new_contact = [name, phone, other]
    return new_contact


def insert_id(phone_book: list) -> int:
    while True:
        try:
            id = int(input('Введите id контакта: '))
            if id in range(1, len(phone_book) + 1):
                return id
            else:
                print('Контакта с таким id нет в списке номеров!')
        except:
            print('Введите корректный id контакта!')


def print_remove_contact():
    print()
    print('Контакт успешно удален.')


def for_search():
    search = input('Введите элемент для поиска: ')
    print()
    return search


def searching_contacts(search_list: list, phone_book: list):
    print('Искомые контакты - это: ')
    for item in range(len(phone_book)):
        if item in search_list:
            print(*phone_book[item])


def print_no_searching_contacts():
    print('Контакты не обнаружены')


def print_success_changes():
    print()
    print('Внесение изменений в контакт завершено.')