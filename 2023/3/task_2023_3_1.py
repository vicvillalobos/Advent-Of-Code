from schematic import Schematic

def execute(data_file):

    with open(data_file, "r") as file:
        data = file.read()
        lines = data.split("\n")

        schematic = Schematic(lines)

    return schematic.part_numbers_sum


if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 3  Part 1 | Answer: ", answer)
