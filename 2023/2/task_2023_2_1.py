from game import Game, GameSet

def execute(data_file: str, red: int, green: int, blue: int):

    id_sum = 0

    with open(data_file, "r") as file:
        data = file.read()
        lines = data.split("\n")

    for line in lines:
        game = Game(line)
        if game.is_possible(red, green, blue):
            id_sum += int(game.id)

    return id_sum

if __name__ == '__main__':
    answer = execute("input.csv", 12, 13, 14)
    print("Day 2  Part 1 | Answer: ", answer)
