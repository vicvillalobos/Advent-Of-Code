import re

def word_processing(word: str) -> int:
    lg_len = len(word) + 1
    
    text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

    matches = [lg_len for x in text]
    rmatches = [-1 for x in text]

    for n in range(len(text)):
        match = word.find(text[n])
        if match >= 0:
            matches[n] = match

        matchr = word.rfind(text[n])
        if matchr >= 0:
            rmatches[n] = matchr

    if sum(matches) == lg_len * len(text):
        return 0

    # Get min of match and max of matchr
    minimum = min(matches)
    maximum = max(rmatches)
    minimum_index = matches.index(minimum)
    maximum_index = rmatches.index(maximum)
    res = int(str(numbers[minimum_index]) + str(numbers[maximum_index]))

    return res


def execute(data_file):
    intervals = []
    with open(data_file, "r") as file:
        data = file.read()

        parameters = data.split("\n")

        data_sum = 0

        for param in parameters:
            interval = word_processing(param)
            intervals.append(interval)

            data_sum += interval

    return data_sum, intervals

if __name__ == '__main__':
    answer = execute("calibrations.csv")
    print("Day 1  Part 2 | Answer: ", answer[0])