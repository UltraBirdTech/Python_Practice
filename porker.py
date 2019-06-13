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
        suite = ['♠','♣','♥','♦']
        number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck_list = []
        for s in suite:
            for n in number:
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
        for c in self.hand.all():
            print('[' + c.value + ']', end='')
        print()

    def get_numbers(self):
        numbers = []
        for c in self.hand.all():
            numbers.append(c.num)
        return numbers

    def get_numbers_as_int(self):
        numbers = []
        for c in self.hand.all():
            numbers.append(int(c.card_number()))
        return numbers
        
    def print_porker_hand(self, result):
        print('My Poker Hand is ' + result)

    def check_poker_hand(self):
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


    def check_straight_flash(self):
        if not self.check_straight(True):
            return

        if not self.check_flash(True):
            return

        if self.is_royal():
            self.print_porker_hand('Royal Straight Flash')
        else:
            self.print_porker_hand('Straight Flash')

    def is_royal(self):
        return ['10', 'J', 'Q', 'K', 'A'].sort() == self.get_numbers().sort()

    def check_straight(self, check_after=False):
        numbers = self.get_numbers_as_int()
        numbers.sort()
        result = numbers == range(numbers[0], 5)
        if result and not check_after:
            self.print_porker_hand('Straight')

        return result

    def check_flash(self, check_after=False):
        suites = []
        for h in self.hand.all():
            suites.append(h.suite)
        
        result = (len(set(suites)) == 1) # 重複をはじいた結果が1であればフラッシュ
        if result and not check_after:
            self.print_porker_hand('Flash')

        return result


    def check_four_card(self):
        pass

    def check_full_house(self):
        pass

    def check_three_card(self):
        pass

    def check_two_pair(self):
        pass

    def check_one_pair(self):
        numbers = self.get_numbers()
        result = len(set(numbers)) == 4
        if result:
            self.print_porker_hand('One Pair!!')
        return result

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

class PorkerHand():
    def __init__():
        pass

main()

