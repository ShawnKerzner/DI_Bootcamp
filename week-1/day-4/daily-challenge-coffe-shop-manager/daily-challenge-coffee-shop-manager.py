menu = {"espresso": 7.0, "latte": 12.0, "cappuccino": 10.0}


def show_menu(menu_dict):
    if menu_dict == {}:
        print("The menu is empty")
    else:
        for key, value in menu_dict.items():
            print(f"{key} - {value}")
