from random import choice

class Pokemon():
    def __init__(self, name, attribute, moves, is_mega=False):
        self.name = name
        self.attribute = attribute
        self.moves = moves
        self.is_mega = is_mega

    def attack(self):
        print(choice(self.moves))

    def mega_shinka(self):
        if self.is_mega:
            print('メガシンカ！！！！！')
        else:
            print('対応していません')

class Pikachu(Pokemon):
    def __init__(self, moves):
        self.name = 'Pikachu'
        self.attribute = 'thunder'
        self.moves = moves
        super().__init__(self.name, self.attribute, self.moves)

class Garura(Pokemon):
    def __init__(self, moves):
        self.name = 'Garura'
        self.attribute = 'normal'
        self.moves = moves
        self.mega = True
        super().__init__(self.name, self.attribute, self.moves, self.mega)

p1 = Pikachu(['thunder shock', 'iron tail', 'Volt Tackle', 'Grass Knot'])
print(p1.name + '=' * 20)
p1.attack()
p1.mega_shinka()

g1 = Garura(['Grow Punch', 'Fake Out', 'Earthquake', 'Ice Beam'])
print(g1.name + '=' * 20)
g1.attack()
g1.mega_shinka()