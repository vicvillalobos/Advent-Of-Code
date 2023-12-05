from card import Card, Deck

def execute(data_file):

    with open(data_file, "r") as file:
        data = file.read()
        lines = data.split("\n")

    deck = Deck(lines)
    
    deck.check()

    return deck.total_amount


if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 4  Part 2 | Answer: ", answer)