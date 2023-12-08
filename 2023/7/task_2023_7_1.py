from functools import cmp_to_key
from hands import CamelCardsHand

def execute(data_file):
    hands = []
    with open(data_file) as f:
        lines = f.readlines()
        
        for line in lines:
            hand_data, bid = line.split()
            hands.append(CamelCardsHand(hand_data, int(bid)))


    sorted_hands = sorted(hands, key=cmp_to_key(CamelCardsHand.compare_hands))

    sum_total = 0
    for n in range(len(sorted_hands)):
        print(sorted_hands[n].data, sorted_hands[n].bid, n + 1)
        sum_total += sorted_hands[n].bid * (n + 1)

    return sum_total

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 7  Part 1 | Answer: ", answer)