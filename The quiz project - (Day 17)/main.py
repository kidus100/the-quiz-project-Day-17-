class User:
    def __init__(self, user_id, username, followers):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "kidus")

print(user_1.id)
