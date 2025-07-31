class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

user1 = User("aziz001", "aziz@example.com", True)
print(user1.username, user1.email, user1.is_active)