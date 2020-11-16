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
    pass
