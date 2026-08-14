from faker import Faker

users = []
fake = Faker()


def add_users(x):
    for i in range(x):
        i = {}
        i["name"] = fake.name()
        i["address"] = fake.address()
        i["language_code"] = fake.language_code()
        users.append(i)
    print(users)


add_users(5)
