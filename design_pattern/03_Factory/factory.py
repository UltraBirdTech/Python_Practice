import abc

def main():
    cow = FactoryCow()
    cow.check_animal()

    chicken = FactoryChicken()
    chicken.check_animal()

class Factory:
    def __init__(self):
        pass
