import random


class Table:
    def __init__(self, player, funds=100):
        self.player = Player(player, funds)
        self.dealer = Dealer()
        self.box = Box()
        self.table_setup()

    def table_setup(self):
        self.player.place_bet()
        self.box.shuffle()
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)

    def deal_card(self, player):
        card = self.box.stack.pop()
        player.hand.append(card)

class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.score = 0
        self.hand = []



class Player:
    def __init__(self, name, funds, bet=0):
        self.name = name
        self.funds = funds
        self.score = 0
        self.hand = []
        self.bet = bet

    def place_bet(self, amount=10):
        self.funds -= amount
        self.bet += amount


class Box:
    def __init__(self):
        self.stack = self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 10), ('Q', 10), ('K', 10)] * 4

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.stack)

    def draw_card(self):
        card = self.stack.pop()
        return card

