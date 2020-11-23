import abc

def main():
    cow = FactoryCow()
    cow.check_animal()

    chicken = FactoryChicken()
    chicken.check_animal()

class Factory:
    def __init__(self):
        self.animal = self.factory_method()

    def check_animal(self):
        self.animal.eat()
        self.animal.cheack()

    @abc.abstractmethod
    def factory_method(self):
        pass

class Animal:
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def speak(self):
        pass

class CowFactory(Animal):
    def factory_method(self):
        return Cow()

class ChickenFactory(Animal):
    def factory_method(self):
        return Chicken()

class Cow(Animal):
    def eat(self):
        print('Cow:eat')

    def speak(self):
        print('Cow:speak')
