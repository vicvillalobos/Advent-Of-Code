from functools import cmp_to_key
from hands import CamelCardsHand

def execute(data_file):
    hands = []
    with open(data_file) as f:
        lines = f.readlines()
        
        for line in lines:
            hand_data, bid = line.split()
            hands.append(CamelCardsHand(hand_data, int(bid), True))


    sorted_hands = sorted(hands, key=cmp_to_key(CamelCardsHand.compare_hands_2))

    sum_total = 0
    for n in range(len(sorted_hands)):
        print(sorted_hands[n], n + 1)
        sum_total += sorted_hands[n].bid * (n + 1)

    return sum_total

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 7  Part 2 | Answer: ", answer)