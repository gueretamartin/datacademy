def area_circle(radio, pi=3.14):  # Parameters with default value (on the right side)
    return pi * (radio ** 2)


# Literal, i could change the position of the parameters
print(area_circle(2, 3.141592))
print(area_circle(pi=3.141592, radio=2))

# Args


def average(*args):
    print(args)
    print(type(args))
    return sum(args) / len(args)


def combinate(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)


print(average(5, 5, 0, 0))
combinate(3, 4, 5, 4, 5, 6, 67, 7, p4=1000)

def users(**kwargs):
    print(kwargs)
    print(type(kwargs))

users(martin=[10,10,10],juan=[10,1])