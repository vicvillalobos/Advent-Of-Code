import re, math
from seeds import SeedMapGroup
from alive_progress import alive_bar


def execute(data_file):

    with open(data_file, "r") as file:
        data = file.read()
        lines = data.split("\n")

    # First we format the input data
    regex_map = re.compile(r"(\w+)-to-(\w+) map:")
    seeds_values = []
    seed_groups = []
    initial_group = None
    current_group = None

    for i in range(len(lines)):

        if i == 0:
            seeds_values = lines[i].split(": ")[1].split(" ")
        else:
            map_match = regex_map.match(lines[i])
            if map_match:
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

    # Note:
    # This approach is horribly slow and inefficient. Took almost 20 hours to get the data
    # (Granted it was a small container with a fraction of my cpu's power inside an already fractioned WSL2 environment)
    # A better solution would be to go map by map instead of seed by seed, and sort out the values in each mapping task
    # and then remove possible duplicates.

    # A way to group source values by destination would be great, but it seems 
    # my current environment doesn't have enough RAM to do anything of the sort.


    min_location = float('inf')

    total = 0
    for i in range(len(seeds_values)):
        even = i % 2 == 0
        if not even:
            total += int(seeds_values[i])

    with alive_bar(total) as bar:
        for i in range(len(seeds_values)):
            seed_value = int(seeds_values[i])
            even = i % 2 == 0
            if even:
                seed_range = int(seeds_values[i+1])
                print(f"Pair: {seed_value} - {seed_range}")
                for j in range(seed_range):
                    # If we store seeds this time, it will be terribly slow.
                    location = initial_group.look_location(int(seed_value)+j)
                    min_location = min(min_location, location)
                    bar()
        
    return min_location

if __name__ == '__main__':
    answer = execute("input.csv")
    print("Day 5  Part 2 | Answer: ", answer)