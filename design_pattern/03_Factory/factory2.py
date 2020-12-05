import abc

def main():
    cow_factory = Factory(Cow)
    cow_factory.check_animal()

    chicken_factory = Factory(Chicken)
    chicken_factory.check_animal()

class Factory:
    def __init__(self, animal_class):
        self.animal = animal_class()

class Animal:
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def speak(self):
        pass

class CowFactory(Factory):
    def factory_method(self):
        return Cow()

class ChickenFactory(Factory):
    def factory_method(self):
        return Chicken()

class Cow(Animal):
    def eat(self):
        print('Cow:eat')

    def speak(self):
        print('Cow:speak')

class Chicken(Animal):
    def eat(self):
        print('Chicken:eat')

    def speak(self):
        print('Chicken:speak')

if __name__ == '__main__':
    main()
