# Dictionaries - Declare
dictionarie = {}
print(type(dictionarie))

dictionarie = dict()
print(type(dictionarie))

dictionarie = {'Total': 50}
print(dictionarie)
print(dictionarie.keys())
print(type(dictionarie.values()))
print(dictionarie['Total'])


new_dictionarie = {'Total': 50, 10: 'Discount', (1, 2, 3): True, 'Skills': {
    'programacion': True, 'base_de_datos': False}}
print(new_dictionarie)

# Important! Print key - values
for key, value in new_dictionarie.items():
    print(key, value)

print(new_dictionarie.items())
print(new_dictionarie.get('Total'), [])

# keys
# values
# items

k = tuple(new_dictionarie.keys())
print(k)
v = tuple(new_dictionarie.values())
print(v)
i = tuple(new_dictionarie.items())
print(i)

# Delete elements
print(len(new_dictionarie))
del new_dictionarie[10]
val = new_dictionarie.pop('Total')
new_dictionarie.pop((1,2,3))
# print(new_dictionarie)
print(len(new_dictionarie))
new_dictionarie.clear()
print(len(new_dictionarie))
print(new_dictionarie)
