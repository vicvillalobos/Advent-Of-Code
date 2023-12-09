from functools import cmp_to_key

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

possible_cards = ["A", "K", "Q", "J","T", "9", "8", "7", "6", "5", "4", "3", "2"]
possible_cards_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

class CamelCardsHand:
    def __init__(self, hand_data : str, bid : int, enable_jokers : bool = False):
        self.data : str = hand_data
        self.bid = bid
        self.jokers_enabled = enable_jokers
        self.jokers = 0
        self.joker_card = "J"
        if enable_jokers:
            self.jokers = hand_data.count("J")
            self.joker_card = self.choose_jokers()
        
        self.cards = [self.jokers for n in range(len(possible_cards))]

        for char in hand_data:
            ix = possible_cards.index(char)
            self.cards[ix] += 1
            
        print(self.cards)
        print(self.get_type())

    def choose_jokers(self):
        max_hand = None
        max_hand_card = ""
        # choose an alternative card for jokers that would make it the best hand.
        for i in range(len(possible_cards_2) - 1):
            virtual_hand_data = self.data.replace("J", possible_cards_2[i])
            virtual_hand = CamelCardsHand(virtual_hand_data, self.bid, False)
            virtual_hand_card = possible_cards_2[i]
            if i > 0:
                comparation = CamelCardsHand.compare_hands(virtual_hand, max_hand)
                if comparation > 0:
                    max_hand_card = virtual_hand_card
                    max_hand = virtual_hand
            else:
                max_hand_card = virtual_hand_card
                max_hand = virtual_hand
        
        return max_hand_card
    
        
    def get_type(self):
        if self.jokers_enabled:
            joker_strong_hand = CamelCardsHand(self.data.replace("J", self.joker_card), self.bid)
            return joker_strong_hand.get_type()
        else:
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
    def compare_hands_2(hand1, hand2):
        # For each card, add the amount to the dictionary.
        
        if hand1.get_type() < hand2.get_type():
            return -1
        elif hand1.get_type() > hand2.get_type():
            return 1
        else:
            for i in range(5):
                hand1_card = possible_cards_2.index(hand1.data[i])
                hand2_card = possible_cards_2.index(hand2.data[i])
                
                if hand1_card > hand2_card:
                    return -1
                elif hand1_card < hand2_card:
                    return 1
        return 0

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