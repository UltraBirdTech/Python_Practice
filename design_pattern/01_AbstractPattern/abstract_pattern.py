amount_dict = {"high": 1.2, "normal":1.0, "low": 0.8}

def main():
    factorya = AbstractPizzaFactory(PizzaFactoryA())
    factorya.make_pizza("high")
    factorya.check_pizza()

    print("-" * 5)
    factoryb = AbstractPizzaFactory(PizzaFactoryA())
    factoryb.make_pizza("normal")
    factoryb.check_pizza()

# AbstractFacotry
class AbstractPizzaFactory():
    def __init__(self, pizza_factory, amount_str="normal"):
        self.factory = pizza_factory

    def make_pizza(self, amount_str):
        amount = amount_dict[amount_str]
        self.pizza_materials = []
        self.pizza_materials.append(self.factory.add_dough(amount))
        self.pizza_materials.append(self.factory.add_source(amount))
        self.pizza_materials.append(self.factory.add_topping(amount))

    def check_pizza(self):
        for pizza_matterial in self.pizza_materials:
            pizza_matterial.check()

    # create product
    def add_dough(self, amount=1):
        pass

    def add_source(self, amount=1):
        pass

    def add_topping(self, amount=1):
        pass

class PizzaFactoryA(AbstractPizzaFactory):
    def __init__(self):
        pass

    def add_dough(self, amount=1):
        return WheatDough(amount)

    def add_source(self, amount=1):
        return TomatoSource(amount)

    def add_topping(self, amount=1):
        return CoanTopping(amount)

class PizzaFactoryB(AbstractPizzaFactory):
    def __init__(self):
        pass

    def add_dough(self, amount=1):
        return RiceFlourDough(amount)

    def add_source(self, amount=1):
        return BasilSource(amount)

    def add_topping(self, amount=1):
        return CheeseTopping(amount)

class Dough:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

class WheatDough(Dough):
    def check(self):
        print("Wheat(amount: {}".format(self.amount))

class RiceFlourDough(Dough):
    def check(self):
        print("FlourDough(amount: {}".format(self.amount))

class TomatoSource(Dough):
    def check(self):
        print("TomatoSource(amount: {}".format(self.amount))

class BasilSource(Dough):
    def check(self):
        print("BasilSource(amount: {}".format(self.amount))

class Topping:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

class CoanTopping(Topping):
    def check(self):
        print("CoanTopping(amount: {}".format(self.amount))

class CheeseTopping(Topping):
    def check(self):
        print("CheeseTopping(amount: {}".format(self.amount))

if __name__ == "__main__":
    main()
    
