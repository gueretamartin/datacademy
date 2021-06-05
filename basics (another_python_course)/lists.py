# Lists
list = ['Python', 'Java', 'Ruby', 'Django']
print(list[::-1])  # print reverse.
print(list[::2])  # print skip by 2
print(list[:-1])  # print without last element
print(list[1:])  # print without first element

list.append('C#')  # Add element
print(list)

print(len(list))  # Print lenght

list.insert(0, 'Rails')  # Insert on first position
list.insert(-1, 'C')  # Insert before last position

print(list)  # Print list

new_list = ['Docker', 'Javascript']  # Create a new list

list.extend(new_list)  # Add the new list on "list"
print(list)

list.clear()  # Clear list.
print(list)

list.extend(new_list)  # Add sublist
del list[0]  # Delete first element
print(list)

# Strings
name = 'martin'  # Strings like lists.
print(name[::-1])  # Print reverse
print(name[2])
print(name[::2])  # Print with skip

# Order
name = ['Martin', 'Marcelo']
numbers = [2, 35, 0, 234]
name.sort()
numbers.sort()
print(name)
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(min(numbers))  # min
print(max(numbers))  # max

print(34 in numbers)  # Search element in list
print(4 not in numbers)
print(numbers.index(34))  # Return the first index

# Matrices

column_a = [10, 20, 3, 4]
column_b = [30, 40, 2, 3]
matriz = [column_a, column_b]
print(matriz[0][3])
