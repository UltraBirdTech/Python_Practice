class Animal():
    def __init__(self, name):
        self.name = name

    def cry(self):
        print(self.voice)


class Dog(Animal):
    def __init__(self):
        name = 'dog'
        self.voice = 'Wow Wow'
        super().__init__(name)


class Cat(Animal):
    def __init__(self):
        name = 'Cat'
        self.voice = 'Nya～'
        super().__init__(name)

Dog().cry()
Cat().cry()

