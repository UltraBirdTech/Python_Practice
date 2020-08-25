amount_dict = {"high": 1.2, "normal":1.0, "low": 0.8}

def main():
    factorya = AbstractPizzaFactory(PizzaFactoryA())
    pizza1 = factorya.make_pizza("high")
    pizza1.check_pizza()

    print("-" * 5)
    factoryb = AbstractPizzaFactory(PizzaFactoryA())
    pizza2 = factorya.make_pizza("normal")
    pizza2.check_pizza()

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
        for pizza_matterial in serlf.pizza_materials:
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

if __name__ == "__main__":
    main()
    
