from blackjack_oop import Deck, Card, Hand
import pytest


def test_card_rank():
    card = Card('J', 'H')
    assert card.rank == 'J'


def test_card_suit():
    card = Card('J', 'H')
    assert card.suit == 'H'


def test_card_uppercased():
    card = Card('J', 'h')
    assert card.suit == 'H'


def test_card_points():
    card = Card('J', 'H')
    anotherCard = Card('3', 'S')

    assert card.points == 10
    assert anotherCard.points == 3


def test_card_to_string():
    card = Card('J', 'H')
    anotherCard = Card('3', 'S')

    assert card.toString() == "JH"
    assert anotherCard.toString() == "3S"


def test_hand_raise_exception():
    with pytest.raises(Exception):
        Hand(['AC', '7H'])


def test_hand_points_empty():
    assert Hand([]).points == 0


def test_hand_points_numbers_only():
    hand = Hand([Card('7', 'H'),  Card('2', 'D')])
    assert hand.points == 9


def test_hand_points_numbers_and_face():
    hand = Hand([
        Card('3', 'D'),
        Card('J', 'C'),
        Card('Q', 'H'),
        Card('2', 'H'),
        Card('A', 'C')
    ])
    assert hand.points == 36


def test_hand_points_two_aces():
    hand = Hand([Card('A', 'D'),  Card('A', 'C')])
    assert hand.points == 21


def test_hand_points_two_aces_and_others():
    hand = Hand([
        Card('2', 'D'),
        Card('A', 'D'),
        Card('A', 'C')
    ])
    assert hand.points == 24


def test_deck_generate_order():
    deck = Deck()

    cards_in_deck = list(map(lambda num: deck.draw().toString(), deck.cards))

    assert cards_in_deck == [
        "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"
    ]
