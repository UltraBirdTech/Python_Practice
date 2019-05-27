from random import choice


class Pokemon():
    def __init__(self, name, type, moves):
        self.name = name
        self.type = type
        self.moves = moves

    def attack(self):
        print(choice(self.moves))

picachu = Pokemon('Picachu', 'thunder', ['thunder shock', 'iron tail'])
picachu.name
picachu.attack()
