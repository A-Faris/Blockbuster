export class Card {
  constructor(rank, suit) {
    this.rank = rank
    this.suit = suit
  }

  toString() {
    //TODO Complete this method so that it returns the correct string to represent the hand
    return ''
  }

  get points() {
    //TODO Complete this method so that it gets the correct number of points for a card
    return 0
  }
}

export class Hand {
  constructor(cards) {
    if (!cards.every((card) => card instanceof Card)) {
      throw new TypeError('A Hand can only contain Cards')
    }

    this.cards = cards
  }

  get points() {
    //TODO Complete this method so that it calculates the points for a hand of cards
    return 0
  }
}

export class Deck {
  constructor() {
    //TODO Complete this method so the deck contains all the correct cards
    this.cards = []
  }

  draw() {
    return this.cards.shift()
  }

  shuffle() {
    //TODO Complete this method so that it shuffles the deck
  }
}
