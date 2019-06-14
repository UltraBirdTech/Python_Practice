import random

def main():
    deck = Deck()
    player = Player(deck)
    player.print_my_hand()
    player.exchange(deck)
    player.print_my_hand()
    player.check_poker_hand()
    player.print_result()

class Card():
    def __init__(self, suite, num):
        self.suite = suite
        self.num = num
        self.value = suite + num

    def card_number(self):
        if self.num not in ['A', 'J', 'Q', 'K']:
            return self.num

        card_mapping = {
            'K': 13,
            'Q': 12,
            'J': 11,
            'A': 1 
        }
        return card_mapping[self.num]


class Deck():
    def __init__(self):
        suites = ['♠','♣','♥','♦']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck_list = []
        for s in suites:
            for n in numbers:
                deck_list.append(Card(s, n))
        
        self.deck_list = deck_list

    def draw(self):
        card = random.choice(self.deck_list)
        self.deck_list.remove(card)
        return card

class Player():
    def __init__(self, deck):
        self.hand = Hand()
        for i in range(0, self.hand.max_hand):
            self.draw(deck)

    def draw(self, deck):
        self.hand.add(deck.draw())

    def cut(self, num):
        self.hand.cut(int(num))

    def exchange(self, deck):
        input_value = input()
        input_list = input_value.split(',')
        input_list.reverse()
        for i in input_list:
            self.cut(i)
        
        for i in range(len(self.hand.all()), self.hand.max_hand):
            self.draw(deck)

    def print_my_hand(self):
        self.hand.print_my_hand()

    def print_result(self):
        self.hand.porker_hand.display()

    def check_poker_hand(self):
        self.hand.check_porker_hand()

class Hand():
    def __init__(self):
        self.max_hand = 5
        self.hand = []

    def add(self, card):
        self.hand.append(card)

    def cut(self, num):
        del self.hand[num]

    def all(self):
        return self.hand

    def print_my_hand(self):
        for c in self.hand:
            print('[' + c.value + ']', end='')
        print()

    def check_porker_hand(self):
        self.porker_hand = Check().check(self)

    def get_numbers(self):
        numbers = []
        for c in self.hand:
            numbers.append(c.num)
        return numbers

    def get_numbers_as_int(self):
        numbers = []
        for c in self.hand:
            numbers.append(int(c.card_number()))
        return numbers
 
    def get_all_suites(self):
        suites = []
        for h in self.hand:
            suites.append(h.suite)
        return suites


class Check():
    def __init__(self):
        self.initialize_porker_hands()

    def check(self, hand):
        self.flash.check(hand)
        self.straight.check(hand)

        self.royal_straight_flash.check(hand, self.flash.result, self.straight.result)
        if self.royal_straight_flash.result:
            return self.royal_straight_flash

        if self.flash.result:
            return self.flash
            
        if self.straight.result:
            return self.straight 

        self.one_pair.check(hand)
        if self.one_pair.result:
            return self.one_pair 

        return self.peke

    def initialize_porker_hands(self):
        self.royal_straight_flash = StraightFlash()
        self.flash = Flash()
        self.straight = Straight()
        self.one_pair = OnePair()
        self.peke = Peke()

class PorkerHand():
    def __init__(self, porker_hand):
        self.porker_hand = porker_hand 
        self.result = False

    def check_conditions(self, hand):
        print('You should write about conditions for each class.')

    def check(self, hand):
        self.check_conditions(hand)

    def display(self):
        print('My hand is ' + self.porker_hand)

class StraightFlash(PorkerHand):
    def __init__(self):
        super().__init__('StraightFlash')

    def check_conditions(self, hand, straight_result, flash_result):
        if not (straight_result and flash_result):
            return

        if self.is_royal(hand):
            self.porker_hand = 'RoyalStraightFlash'
        
        self.result = True

    def check(self, hand, straight_result, flash_result):
        self.check_conditions(hand, straight_result, flash_result)

    def is_royal(self, hand):
        return ['10', 'J', 'Q', 'K', 'A'].sort() == hand.get_numbers().sort()

class Flash(PorkerHand):
    def __init__(self):
        super().__init__('Flash')

    def check_conditions(self, hand):
        suites = hand.get_all_suites() 
        self.result = (len(set(suites)) == 1) # 重複をはじいた結果が1であればフラッシュ

class Straight(PorkerHand):
    def __init__(self):
        super().__init__('Straight')

    def check_conditions(self, hand):
        numbers = hand.get_numbers_as_int()
        numbers.sort()
        self.result = numbers == range(numbers[0], 5)

class OnePair(PorkerHand):
    def __init__(self):
       super().__init__('OnePair')

    def check_conditions(self, hand):
        numbers = hand.get_numbers()
        self.result = len(set(numbers)) == 4

class Peke(PorkerHand):
    def __init__(self):
        super().__init__('PEKE')

    def display(self):
        print('PE☆KE')


main()

