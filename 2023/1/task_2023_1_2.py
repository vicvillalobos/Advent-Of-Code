import re

def word_processing(word: str) -> int:
    lg_len = len(word) + 1
    
    # Create an array with keys and other with the corresponding values.
    keys = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

    # Initialize matching arrays. these will contain a default value, and then some of them will be replaced with the actual indices of the matches.
    matches = [lg_len for x in keys] # If word is "abc" (lenght 3), Inititalizes to [4, 4, 4, 4, 4, 4, ..., 4, 4] (length 18). Each value will be connected with a value in 'keys' via their indexes.
    rmatches = [-1 for x in keys] # This is the same, but filled with -1, used for matches looked up in reverse.

    # For each possible value to be found (keys array)
    for n in range(len(keys)):
        match = word.find(keys[n]) # Find the first occurrence (left to right) of the iterated key (e.g. "three") and return it's index (or -1 if not found.)
        if match >= 0: # if found (a.k.a. match is greater or equal to zero, and by extension not -1)
            matches[n] = match # Replace the value of 'matches' array with our index. (Remember larger indexes means the word was found more to the right in the string)

        # Same but with reverse find

        matchr = word.rfind(keys[n]) # Find the first occurrence (right to left) of the iterated key (e.g. "eight") and return it's index (or -1 if not found.)
        if matchr >= 0: # if found
            rmatches[n] = matchr # Replace the value of rmatches array with our index.

    # After iterating over our values

    if sum(matches) == lg_len * len(keys): # If our array is not modified (since it's a predefined value and the sum of the match indexes can't be that high)
        return 0 # Return 0, the word doesn't have any keys in it.

    # Get min of match and max of matchr
    minimum = min(matches) # This will return the smallest index of each key's match. If several keys are found, this variable will hold the one that was first from the left.
    maximum = max(rmatches) # This will return the largest index of each key's match. If several keys are found, this variable will hold the one that was first from the right.

    # Now we get the index of each index (yeah I know) in our index holding arrays. These values now represent the indexes from the original arrays connected to these minimum and maximum values.
    minimum_index = matches.index(minimum)
    maximum_index = rmatches.index(maximum)

    # We evaluate the indexes in the numbers array, containing the corresponding integer values of each key.
    # The result is the concatenation of both numbers.    
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