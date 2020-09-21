amoun_dict = {"high": 1.2, "normal":1.0, "low":0.8}

def main():
    pizza1 = make_pizza(PizzaFactoryA, "high")
    pizza1.check_pizza()

    print("-----")

    pizza2 = make_pizza(PizzaFactoryB, "normal")
    pizza2.check_pizza()

def make_pizza(PizzaFactory, amount_str):
    pizza = PizzaFactory()
    mount = amountdict[amount_str]
    pizza.pizza_matterials = []
    pizza.pizza_matterials.append(piiza.add_dough(amount))
    pizza.pizza_matterials.append(piiza.add_source(amount))
    pizza.pizza_matterials.append(piiza.add_topping(amount))
    return pizza

class PizzaFactoryA:
    def __init__(self):
        pass

    def check_pizza(self):
        for pizza_matterial in self.pizza_materials:
            piiza_matterial.check()

    @classmethod
    def add_dough(self):
        return Class.WheatDaugh()

    @classmethod
    def add_topping(self):
        return Class.CoanTopping()

    @classmethod
    def add_source(self):
        return Class.TomatSource()

    class WheatDough:
        def __init__(self, maount=1):
            self.amount = amount

        def check(self):
            print("Wheat(amount: {})".format(self.amount))

    class CoanTopping:
        def __init__(self, maount=1):
            self.amount = amount

        def check(self):
            print("Coan(amount: {})".format(self.amount))

    class TomatoSource:
        def __init__(self, maount=1):
            self.amount = amount

        def check(self):
            print("TomatSourcce(amount: {})".format(self.amount))

class PizzaFactoryB:
    def __init__(self):
        pass

    def check_pizza(self):
        for pizza_matterial in self.pizza_materials:
            piiza_matterial.check()

    @classmethod
    def add_dough(self):
        return Class.WheatDaugh()

    @classmethod
    def add_topping(self):
        return Class.CoanTopping()

    @classmethod
    def add_source(self):
        return Class.TomatSource()

    class RiceFlourDough:
        def __init__(self, maount=1):
            self.amount = amount

        def check(self):
            print("RiceFlour(amount: {})".format(self.amount))

    class CoanTopping:
        def __init__(self, maount=1):
            self.amount = amount

        def check(self):
            print("Coan(amount: {})".format(self.amount))

    class TomatoSource:
        def __init__(self, maount=1):
            self.amount = amount

        def check(self):
            print("TomatSourcce(amount: {})".format(self.amount))
