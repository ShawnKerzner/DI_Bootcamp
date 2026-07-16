# Exercise 1
def get_full_name(first_name, last_name, middle_name=None):
    if middle_name == None:
        print(f"{first_name} {last_name}")
        return first_name + " " + last_name
    else:
        print(f"{first_name} {middle_name} {last_name}")
    return first_name + " " + middle_name + " " + last_name


get_full_name(first_name="Chaim", middle_name="Shmuel", last_name="Kerzner")
get_full_name(first_name="Shawn", last_name="Kerzner")
