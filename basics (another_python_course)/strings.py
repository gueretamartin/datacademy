# Strings Methods
lenguages = 'Python Ruby C# Others'
lenguages_list = lenguages.split()  # Divide on list by spaces
print(lenguages_list)
print(type(lenguages_list))

lenguages = 'Python/*/Ruby/*/C#/*/Others'
lenguages_list = lenguages.split('/*/')  # Divide on list by /*/
print(lenguages_list)
print(type(lenguages_list))

lenguages = 'Python/*/Ruby/*/C#/*/Others'
# Divide on list by /*/ by only 2 times.
lenguages_list = lenguages.split('/*/', 2)
print(lenguages_list)
print(type(lenguages_list))

# List to Strings  - Join method

new_string = ' '.join(lenguages_list)
print(new_string)
print(type(new_string))

new_string = '/////'.join(lenguages_list)
print(new_string)
print(type(new_string))

new_string = ''.join(lenguages_list)  # All elements was concatenated
print(new_string)
print(type(new_string))

name = 'Martin'
lastname = 'Guereta'
complete = '%s %s' % (name, lastname)  # Deprecated
complete2 = '{} {}'.format(name, lastname)  # Deprecated
complete3 = '{two} {one}'.format(one='Guereta', two='Martin')  # Deprecated

print(complete)
print(complete2)
print(complete3)
print(f'{name} {lastname}')


# Find text in String
print(0 != lenguages.count('Python'))
print('Python' in lenguages)
print('Python'.lower() in lenguages.lower())


print(lenguages.startswith('Python'))
print(lenguages.endswith('Python'))

print('Martín', 'Guereta', '25', sep="***")

message = 'Hello World'
print(message.rjust(50))
print(message.ljust(50), 'Guereta', sep=' ')
print(message.center(50), 'Guereta', sep=' ')
