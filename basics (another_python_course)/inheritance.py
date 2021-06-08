class Animal:

    def eat(self):
        print('Eat')

    def sleep(self):
        print('Sleep')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog1 = Dog()
cat1 = Cat()

dog1.eat()
cat1.sleep()