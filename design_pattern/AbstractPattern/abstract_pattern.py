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


if __name__ == "__main__":
    main()
    
