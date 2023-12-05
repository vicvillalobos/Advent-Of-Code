from game import Game, GameSet

def execute(data_file: str):

    power_sum = 0

    with open(data_file, "r") as file:
        data = file.read()
        lines = data.split("\n")

    for line in lines:
        game = Game(line)
        power_sum += game.min_cubeset.power

    return power_sum

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 2  Part 2 | Answer: ", answer)
