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

    race_time = ""
    race_distance = ""
    for t in times:
        race_time += str(t)
    
    for d in distances:
        race_distance += str(d)


    print("Time:", race_time)
    print("Distance:", race_distance)

    # Do the thing 
    possible_win_count = 0

    for t in range(int(race_time)):
        # Calculate distance if we hold for t milliseconds.
        if calculate_distance(t, int(race_time)) > int(race_distance):
            possible_win_count += 1

    # Not the most elegant solution by all means, but it is correct.
    return possible_win_count

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 6  Part 2 | Answer: ", answer)