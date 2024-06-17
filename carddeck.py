import random

from card import Card

class CardDeck:
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self):
        # build the deck of cards
        self._build_deck()
        self._other_task()

    def _build_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()  # remove and return last element of cards

    def _other_task(self):
        pass

    # responds to len(carddeck object)
    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"CardDeck:{len(self)}"

    def __repr__(self):
        return  f"CardDeck()"

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"{d1 = }")
    d1.shuffle()
    print(f"{d1.cards = }")
    for i in range(5):
        card = d1.draw()
        print(card.rank, card.suit, card)

    print(f"{len(d1) = }")
    print(d1)
#  str -- "human friendly info"
#  repr -- "how to reproduce the object"
        
#  str() --> __str__(self)  
#  repr() --> __repr__(self)
        
#  print(obj)    print(str(obj))
        
#  print(list)   
    import re

    r = re.compile(r"^foo")
    print(str(r))
    print(repr(r))