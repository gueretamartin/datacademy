class User:

    # Object
    def __init__(self,username = '',password=''):
        self.username = username
        self.password = password

user1 = User('Martin','m4rt1n')
print(user1.__dict__)

user2 = User()
print(user2.__dict__)

