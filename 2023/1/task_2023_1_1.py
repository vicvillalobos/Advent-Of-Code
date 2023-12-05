import re

def execute(data_file):
    intervals = []
    with open(data_file, "r") as file:
        data = file.read()

        parameters = data.split("\n")

        data_sum = 0

        for param in parameters:
            pnumber = re.sub(r'[^0-9]*', "", param)
            interval = int(pnumber[0] + pnumber[-1])
            intervals.append(interval)
            data_sum += interval

    return data_sum, intervals


if __name__ == '__main__':
    answer = execute("calibrations.csv")
    print("Day 1  Part 1 | Answer: ", answer[0])

    