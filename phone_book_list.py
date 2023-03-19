phone_base = []


def get_phone_base():
    global phone_base
    return phone_base


def set_phone_base(phone_base_new: list):
    global phone_base
    phone_base = phone_base_new


def add_contact(new_contact):
    global phone_base
    return phone_base.append(new_contact)


def remove_contact(id: int):
    global phone_base
    contact = phone_base[id - 1]
    verification = input(f'Вы точно хотите удалить контакт {contact}? Y/N: ')
    if verification == 'Y':
        phone_base.pop(id - 1)
        return True
    else:
        print()
        print('Контакт не был удален.')
        return False


def search_contact(search: str) -> list:
    global phone_base
    search = search.lower()
    i = 0
    search_list = []
    while i < len(phone_base):
        for item in range(len(phone_base)):
            contact = ';'.join(phone_base[item]).lower()
            for char in range(len(contact)):
                if contact[char:char + len(search)] == search:
                    search_for = item
                    search_list.append(search_for)
                    break
            i += 1
    return search_list


def change_contact(id: int):
    global phone_base
    contact = phone_base[id-1]
    for i in range(len(contact)):
        insert = input(f'Вы хотите изменить элемент "{contact[i]}"? Y/N: ')
        if insert == 'Y':
            new_item = input('Введите новое значение элемента: ')
            contact[i] = new_item
        else:
            print('Элемент без изменений')