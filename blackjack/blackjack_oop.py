class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def to_string(self):
        # TODO Complete this method so that it returns the correct string to represent the hand
        return ''

    @ property
    def points(self):
        # TODO Complete this method so that it gets the correct number of points for a card
        return 0


class Hand:
    def __init__(self, cards):
        all_cards = all(isinstance(card, Card) for card in cards)

        if (not all_cards):
            raise Exception('A Hand can only contain Cards')

        self.cards = cards

    @property
    def points(self):
        # TODO Complete this method so that it calculates the points for a hand of cards
        return 0


class Deck:
    def __init__(self):
        # TODO Complete this method so the deck contains all the correct cards
        self.cards = []

    def draw(self):
        return self.cards.pop(0)

    def shuffle(self):
        # TODO Complete this method so that it shuffles the deck
        print(self.cards)
