class Animal:
    def __init__(self, name):
        self.name =  name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Dog(Animal):
    def speak(self):
        print('WOOF!')

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog('Scooby')
cat = Cat('Garfield')
mouse = Mouse('Micky')

print(cat.name)
print(cat.is_alive)
cat.eat()
dog.speak()