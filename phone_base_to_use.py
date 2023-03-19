import phone_book_list as pb_list


def read_phone_base():
    with open('phone_base_txt', 'r', encoding='UTF = 8') as file:
        phone_book = file.readlines()
    return pb_list.set_phone_base(string_to_list_in_phone_book(phone_book))


def string_to_list_in_phone_book(phone_book: str) -> list:
    new_phone_book = []
    for item in phone_book:
        new_phone_book.append(item.strip().split(
            ';'))  # strip() - это удаление "лишних" элементов (пробелов и прочее, включая \n) в начале и конце строки
    return new_phone_book


def save_ch_to_phone_base():
    with open('phone_base_txt', 'w', encoding='UTF = 8') as file:
        file.write(list_to_string_in_phone_book())


def list_to_string_in_phone_book() -> str:
    phone_book = pb_list.get_phone_base()
    txt_phone_book = ''
    for item in phone_book:
        item_new = ';'.join(item)
        txt_phone_book += item_new + '\n'
    return txt_phone_book