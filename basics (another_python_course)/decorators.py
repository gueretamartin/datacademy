# Function -> Input  ... Function -> Ouput
# a -> Main Function (Decorator)
# b -> Function (to decorated)
# c -> Function decorated

# a(b) -> c

def function_a(function_b):

    def function_c():
        function_b()
        print('Hello b')
    return function_c


@function_a
def say_hello():
    print('Hello')


@function_a
def sum():
    print(10+50)


say_hello()
sum()
