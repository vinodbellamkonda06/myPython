import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.suit, self.value))

    def sum(self):

        print(self.value)


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())

    def showhand(self):
        for card in self.hand:
            card.show()

    def sum(self):
        for card in self.hand:
            print(card())


    def discard(self):
        return self.hand.pop()


deck = Deck()
deck.shuffle()
vinod = Player("vinod")
sreenu = Player("sreenu")
vinod.draw(deck)
sreenu.draw(deck)
vinod.draw(deck)
sreenu.draw(deck)
vinod.showhand()
sreenu.showhand()




