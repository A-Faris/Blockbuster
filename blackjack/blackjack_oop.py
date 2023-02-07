class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def to_string(self) -> str:
        """Returns the correct string to represent the hand"""
        return ''

    @property
    def points(self) -> int:
        """Gets the correct number of points for a card"""
        return 0


class Hand:
    def __init__(self, cards: list) -> None:
        all_cards = all(isinstance(card, Card) for card in cards)

        if (not all_cards):
            raise Exception('A Hand can only contain Cards')

        self.cards = cards

    @property
    def points(self) -> int:
        """Calculates the points for a hand of cards"""
        return 0


class Deck:
    def __init__(self) -> None:
        # TODO Complete this method so the deck contains all the correct cards
        self.cards = []

    def draw(self) -> Card:
        """Removes and returns the top card from the deck"""
        return self.cards.pop(0)

    def shuffle(self) -> None:
        """Shuffles the cards in this deck"""
        print(self.cards)
