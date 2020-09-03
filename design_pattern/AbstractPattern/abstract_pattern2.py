amoun_dict = {"high": 1.2, "normal":1.0, "low":0.8}

def main():
    pizza1 = make_pizza(PizzaFactoryA, "high")
    pizza1.check_pizza()

    print("-----")

    pizza2 = make_pizza(PizzaFactoryB, "normal")
    pizza2.check_pizza()


    
