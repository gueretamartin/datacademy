# v_tuple s - Inmmutable structure. - Readonly
# Faster than list
# They save on special read-only memmory

v_tuple = ('Monday', 10, 15.4, [1, 2, 3], ('NewTuple', 'Element2'))
print(v_tuple[-1][0])  # Print NewTuple
print(type(v_tuple))


list = v_tuple[3]  # Extract list from v_tuple
print(type(list))

sub_tuple = v_tuple[::2]  # Generate a subtuple
print(sub_tuple)

# Unpack v_tuple s
one, two, three, *rest = v_tuple
print(one, two, three)
print(*rest)
print(*rest[0])

newone, newtwo, newthree, *_ = v_tuple  # Doesn't matter the rest of elements

tuple2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
one, _, _, four, *_, ten = v_tuple
print(one, four, ten)

# Packing v_tuple s
list_pack = [1, 2, 3, 4, 5]
tuple_pack = (30, 43, 34, 30)

result = zip(tuple_pack, list_pack)
result = tuple(result)
print(result)
