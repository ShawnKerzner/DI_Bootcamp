menu = {"espresso": 7.0, "latte": 12.0, "cappuccino": 10.0}


def show_menu(menu_dict):
    if menu_dict == {}:
        print("The menu is empty")
    else:
        for key, value in menu_dict.items():
            print(f"{key} - {value}")


def add_item(menu_dict):
    drink_name = str(input("Name of the new drink: "))
    if drink_name in menu_dict:
        print("Item already exists")
    else:
        drink_price = float(input("Price of new drink: "))
        menu_dict[drink_name] = drink_price
        print(f"{drink_name} added!")


def update_price(menu_dict):
    select_drink = input("Which drink would you like to update? ")
    if select_drink in menu_dict:
        new_price = float(input("Insert new price: "))
        menu_dict[select_drink] = new_price
    else:
        print("Item not found")


def delete_items(menu_dict):
    item_delete = input("Which item would you like to remove? ")
    if item_delete in menu_dict:
        del menu_dict[item_delete]
    else:
        print("Item not found")


def show_options():
    print("1. Show Menu\n", "2. Add Item\n",
          "3.Update Price\n", "4. Delete Item\n", "5. Exit")


def run_coffee_shop():
    running = True
    while running:
        show_options()
        action = int(input("Select one of the following numbers above: "))
        if action < 1 or action > 5:
            raise ValueError("Not an option")
        elif action == 1:
            show_menu(menu_dict=menu)
        elif action == 2:
            add_item(menu_dict=menu)
        elif action == 3:
            update_price(menu_dict=menu)
        elif action == 4:
            delete_items(menu_dict=menu)
        else:
            print('Goodbye!!!')
            running = False


run_coffee_shop()
