v = '' or [] or True  # Assing the first True Value
print(v)
v = 'Martin' if [] else True
print(v)

# While - Use it when i don't know the number of iteraccions
cont = 1
# num = 500
while cont <= 5:
    print(cont)
    cont += 1

users = ['user1', 'user2', 'user3']

for user in users:
    print(user)


ran = range(5, 11, 2)  # Skip by 2 to 2.
for r in ran:
    print(r)

# Enumerate
en = [10, 2, 3, 40]
enum = enumerate(en)
print(enum)
for index, number in enumerate(en):
    print(index, number)
