import view
import phone_base_to_use as pb_to_use
import phone_book_list as pb_list


def menu_actions(choice: int):
    if choice == 1:
        pb_to_use.read_phone_base()
        view.print_open_db()
    elif choice == 2:
        phone_book = pb_list.get_phone_base()
        view.print_phone_book(phone_book)
    elif choice == 3:
        pb_to_use.save_ch_to_phone_base()
        view.print_save_db()
    elif choice == 4:
        new_contact = view.new_contact()
        pb_list.add_contact(new_contact)
        view.print_add_contact()
    elif choice == 5:
        phone_book = pb_list.get_phone_base()
        id = view.insert_id(phone_book)
        pb_list.change_contact(id)
        view.print_success_changes()
    elif choice == 6:
        phone_book = pb_list.get_phone_base()
        id = view.insert_id(phone_book)
        if pb_list.remove_contact(id):
            view.print_remove_contact()
    elif choice == 7:
        search = view.for_search()
        searching_contact_indexes = pb_list.search_contact(search)
        if len(searching_contact_indexes) > 0:
            phone_book = pb_list.get_phone_base()
            view.searching_contacts(searching_contact_indexes, phone_book)
        else:
            view.print_no_searching_contacts()
    else:
        return True


def start():
    while True:
        view.print_menu()
        choice = view.input_choice_menu()
        print()
        if menu_actions(choice):
            view.out_of_menu()
            break