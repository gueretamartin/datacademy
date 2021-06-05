animal = 'Frog'  # Global Scope
animal2 = 'Cat' 

def print_animal():
    global animal2
    
    animal = 'Cow'  # Local Scope
    animal2 = 'Dog' # Modifying variable with Global Scope inside a function
    print(animal)
    print(id(animal))


print_animal()
print(animal)
print(id(animal))
print(animal2)
