from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _build_deck(self):
        super()._build_deck()  # call _build_deck() in parent class
        for joker in range(1, 3):  # 1,2
            joker_name = f"Joker{joker}"
            card = Card(joker_name, joker_name)
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    print(j)
    j.shuffle()
    print(j.cards)
    print()
    for i in range(10):
        print(j.draw())
