def calculate_distance(hold_time, total_time):
    # speed = hold_time
    # moving_time = total_time - hold_time
    # distance = speed * moving_time

    return hold_time * (total_time - hold_time)

def execute(input_file):

    with open(input_file) as f:
        data = f.read()
        time, distance = data.split("\n")

    times = time.split("  ")[1:]
    
    # cleanup
    for i in reversed(range(len(times))):
        if times[i] == "":
            del times[i]
        else:
            times[i] = int(times[i])

    distances = distance.split("  ")[1:]
    for i in reversed(range(len(distances))):
        if distances[i] == "":
            del distances[i]
        else:
            distances[i] = int(distances[i])

    print("Times:", times)
    print("Distances:", distances)

    possible_wins = []

    # Do the thing 
    for i in range(len(times)):

        race_time = times[i]
        race_record = distances[i]

        possible_win_count = 0

        for t in range(race_time):
            # Calculate distance if we hold for t milliseconds.
            if calculate_distance(t, race_time) > race_record:
                possible_win_count += 1

        possible_wins.append(possible_win_count)

    mult = 1
    for wins in possible_wins:
        mult *= wins

    return mult

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 6  Part 1 | Answer: ", answer)