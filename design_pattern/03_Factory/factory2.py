import abc

def main():
    cow_factory = Factory(Cow)
    cow_factory.check_animal()

    chicken_factory = Factory(Chicken)
    chicken_factory.check_animal()

class Factory:
    def __init__(self, animal_class):
        self.animal = animal_class()

    def check_animal(self):
        self.animal.eat()
        self.animal.speak()

class ChickenFactory(Factory):
    def factory_method(self):
        return Chicken()

class Cow():
    def eat(self):
        print('Cow:eat')

    def speak(self):
        print('Cow:speak')

class Chicken():
    def eat(self):
        print('Chicken:eat')

    def speak(self):
        print('Chicken:speak')

if __name__ == '__main__':
    main()
