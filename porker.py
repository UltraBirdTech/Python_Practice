import random

def main():
    deck = Deck()
    player = Player(deck)
    player.print_my_hand()
    player.exchange(deck)
    player.print_my_hand()
    player.check_poker_hand()

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

    def check_poker_hand(self):
        self.hand.check_porker_hand()
        return
        if self.check_straight_flash():
            return 
        if self.check_straight():
            return
        if self.check_flash():
            return
        if self.check_four_card():
            return
        if self.check_full_house():
            return
        if self.check_three_card():
            return
        if self.check_two_pair():
            return
        if self.check_one_pair():
            return
        
        self.print_porker_hand('PE☆KE')


    def check_four_card(self):
        pass

    def check_full_house(self):
        pass

    def check_three_card(self):
        pass

    def check_two_pair(self):
        pass

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
        Check(self)

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
    def __init__(self, hand):
        flash = Flash()
        flash.check(hand)
        
        straight = Straight()
        straight.check(hand)
        
        if flash.result and straight.result:
            pass

        one_pair = OnePair()
        one_pair.check(hand)
        if one_pair.result:
            one_pair.print_porker_hand()


        print('PE☆KE')
        



class PorkerHand():
    def __init__(self, porker_hand):
        self.porker_hand = porker_hand 
        self.result = False

    def check_conditions(self, hand):
        print('You should write about conditions for each class.')

    def check(self, hand):
        self.check_conditions(hand)

    def print_porker_hand(self):
        print('My hand is ' + self.porker_hand)

class RoyalStraightFlash(PorkerHand):
    def __init__(self):
        super().__init__('RoyalStraightFlash')

    def check_conditions(self, hand):
        if self.is_royal(hand):
            self.porker_hand = 'StraightFlash'
        
        self.result = True
        

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


main()

