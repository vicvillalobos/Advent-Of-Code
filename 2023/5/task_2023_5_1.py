import re
from seeds import SeedMapGroup

def execute(data_file):

    with open(data_file, "r") as file:
        data = file.read()
        lines = data.split("\n")

    # First we format the input data
    regex_map = re.compile(r"(\w+)-to-(\w+) map:")

    seeds = []
    seed_groups = []
    initial_group = None
    current_group = None

    for i in range(len(lines)):

        if i == 0:
            seeds = lines[i].split(": ")[1].split(" ")
        else:
            map_match = regex_map.match(lines[i])
            if map_match:
                print("Map header!", map_match.group(1), map_match.group(2))
                if current_group:
                    seed_groups.append(current_group)
                current_group = SeedMapGroup(map_match.group(1), map_match.group(2))
            elif lines[i].strip() != "":
                destination, source, length = lines[i].split(" ")
                current_group.add(destination, source, length)

    # Append last group
    seed_groups.append(current_group)

    # Let's link the groups together
    for seed_group_1 in seed_groups:

        if seed_group_1.source == "seed":
            initial_group = seed_group_1

        for seed_group_2 in seed_groups:

            if seed_group_1.destination != seed_group_2.destination or seed_group_1.source != seed_group_2.source:
                # Different groups.
                if seed_group_1.source == seed_group_2.destination:
                    seed_group_1.assign_source_group(seed_group_2)
                if seed_group_1.destination == seed_group_2.source:
                    seed_group_1.assign_destination_group(seed_group_2)

    # Data is organized in groups and sets, now we can do the thing!

    min_location = float('inf')

    for seed in seeds:
        location = initial_group.look_location(int(seed))
        print(f"Located seed {seed}: {location}")
        min_location = min(min_location, location)
    
    return min_location

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 5  Part 1 | Answer: ", answer)