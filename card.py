class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    # used with str()
    def __str__(self):
        return f"Card-{self.rank}-{self.suit}"

    # used with repr()
    def __repr__(self):
        # Card('4', 'Diamonds')
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('4', 'Diamonds')
    print(c1)
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    print(repr(c1))
    print(f"{c1 = }")
    