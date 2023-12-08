from functools import cmp_to_key

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

possible_cards = ["A", "K", "Q", "J","T", "9", "8", "7", "6", "5", "4", "3", "2"] 

class CamelCardsHand:
    def __init__(self, hand_data, bid):
        self.data = hand_data
        self.cards = [0 for n in range(len(possible_cards))]
        self.bid = bid
        for char in hand_data:
            ix = possible_cards.index(char)
            self.cards[ix] += 1
            
        print(self.cards)
        print(self.get_type())
        
    def get_type(self):
        # 
        if self.cards.count(5) > 0:
            return FIVE_OF_A_KIND
        if self.cards.count(4) > 0:
            return FOUR_OF_A_KIND
        if self.cards.count(3) > 0:
            if self.cards.count(2) > 0:
                return FULL_HOUSE
            else:
                return THREE_OF_A_KIND
        if self.cards.count(2) == 2:
            return TWO_PAIR
        if self.cards.count(2) > 0:
            return ONE_PAIR
        return HIGH_CARD
        
    @staticmethod
    def compare_hands(hand1, hand2):
        # For each card, add the amount to the dictionary.
        if hand1.get_type() < hand2.get_type():
            return -1
        elif hand1.get_type() > hand2.get_type():
            return 1
        else:
            for i in range(5):
                hand1_card = possible_cards.index(hand1.data[i])
                hand2_card = possible_cards.index(hand2.data[i])
                
                if hand1_card > hand2_card:
                    return -1
                elif hand1_card < hand2_card:
                    return 1
        return 0
    
    def __repr__(self):
        return self.data + " " + str(self.bid) + "(" + str(self.get_type()) + ")"