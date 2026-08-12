# Static attributes
# A static attribute (sometimes called a class attribute) is an attribute that belongs to the class itself,
# not to any specific instance of the class.

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


user1 = User("Shawn", "shawn@gmail.com")
user2 = User("Bart", "bart@yahoo.com")
print(User.user_count)
print(user1.user_count)
print(user2.user_count)
