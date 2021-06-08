# Class attrs
class Usuario:
    username = ''  # Default value
    email = ''


print(Usuario.username)

Usuario.username = 'Martin'

user1 = Usuario()
print(Usuario.username)
print(user1.username)

print(id(Usuario.username))
print(id(user1.username))

# How to python works 
# 1 - Check if exists any instance attr
# 2 - Check if exists any class attr - Readonly
# 3 - Trhow error
# print(id(user1.usernames)) - AttributeError: 'Usuario' object has no attribute 'usernames'

print(user1.__dict__) # Storage instance's attrs

user1.username = 'Juan' # Add instance attr 
user1.password = 'Jose' # Dinamically addded (that's not a good practice)
print(id(user1.username))
print(id(Usuario.username))
print(user1.__dict__)

