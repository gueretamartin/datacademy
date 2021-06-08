class Animal:

    def eat(self):
        print('Eat')

    def sleep(self):
        print('Sleep')

class Feline: 
    def hunt(self):
        print('Hunt!')

class Dog(Animal):
    pass


class Cat(Animal, Feline):
    pass


dog1 = Dog()
cat1 = Cat()

dog1.eat()
cat1.sleep()
cat1.hunt()