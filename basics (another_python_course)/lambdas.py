# Functions could be assign to vars, use like argument to another functions, functions could return functions

def degrees_to_farenheit(degree):
    return degree * 1.8 + 32


my_function = degrees_to_farenheit

print(type(my_function))
print(my_function(10))


function_lambda = lambda degrees : degrees * 1.8 + 32


print(function_lambda(10))

# Default parameters

funcion_l = lambda degree : degree * 1.8 + 32 
function_l2 = lambda degree = 1 : degree * 1.8 + 32
function_l3 = lambda *args, **kwargs : len(args) + len(kwargs)

