from card import Card

def execute(data_file):

    with open(data_file, "r") as file:
        data = file.read()
        lines = data.split("\n")

    points_sum = 0

    for i in range(len(lines)):
        card = Card(lines[i], i)
        points_sum += card.value

    return points_sum

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 4  Part 1 | Answer: ", answer)