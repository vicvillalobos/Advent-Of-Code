class SeedMap:

    def __init__(self, destination_start, source_start, length):
        self.destination_start = int(destination_start)
        self.source_start = int(source_start)
        self.length = int(length)

    def has_seed(self, seed):
        return seed >= self.source_start and (seed < int(self.source_start) + int(self.length))

    def map_seed(self, seed):
        index = int(seed) - int(self.source_start) + int(self.destination_start)
        return index

class SeedMapGroup:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.source_group = None
        self.destination_group = None
        self.seeds = []

    def add(self, destination_start, source_start, length):
        self.seeds.append(SeedMap(destination_start, source_start, length))

    def map_seed(self, seed):
        for seed_map in self.seeds:
            if seed_map.has_seed(seed):
                return seed_map.map_seed(seed)
        return seed
    
    def assign_source_group(self, group):
        self.source_group = group

    def assign_destination_group(self, group):
        self.destination_group = group

    def look_location(self, seed):
        # look for the location value
        value = self.map_seed(seed)

        if self.destination != "location":
            if not self.destination_group:
                return 0
            return self.destination_group.look_location(value)
        else:
            return value
    
    def __repr__(self):
        return f"SeedMapGroup ([{self.source}] to [{self.destination}])"
    