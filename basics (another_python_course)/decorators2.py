# Function -> Input  ... Function -> Ouput
# a -> Main Function (Decorator)
# b -> Function (to decorated)
# c -> Function decorated

# a(b) -> c

def function_a(function_b):

    def function_c(*arg,**kwargs):
        res = function_b(*arg,**kwargs)
        print(res)
    return function_c


@function_a
def say_hello():
    print('Hello')


@function_a
def sum(n1,n2):
    return n1 + n2


sum(10,30)
