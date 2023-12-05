from typing import List

class Deck:
    
    def __init__(self, input: List[str]):
        self.cards = []

        for i in range(len(input)):
            card = Card(input[i], i)
            self.cards.append({"index": i, "card": card, "amount": 1 })

        # Now we can check the deck

    def check(self):
        for c in self.cards:
            c["card"].check(self)

    @property
    def total_amount(self):
        amount = 0
        for card in self.cards:
            amount += card["amount"]
        return amount

class Card:

    def __init__(self, input : str, index):

        self.index = index

        header, data = input.split(": ")

        win_numbers, card_numbers = data.split(" | ")

        self.winning_numbers = win_numbers.strip().replace("  ", " ").split(" ")
        self.card_numbers = card_numbers.strip().replace("  ", " ").split(" ")
        self.matches = self.get_matches()

    def check(self, deck : Deck):
        
        # 1. Check the matching numbers of this card. if no matches then return
        if len(self.matches) <= 0:
            return

        # for each matching card
        for i in range(len(self.matches)):
            ix = self.index + (i + 1)

            # 3. Add 1 to their counter
            deck.cards[ix]['amount'] += 1

            # 4. Execute the check recursive method on those cards.
            deck.cards[ix]['card'].check(deck)

        return


    def get_matches(self):
        matches = []
        for wnum in self.winning_numbers:
            try:
                self.card_numbers.index(wnum)
                matches.append(wnum)
            except:
                pass
        return matches
    
    @property
    def value(self):
        matches = len(self.matches)
        if matches <= 0:
            return 0
        return pow(2, matches - 1)

