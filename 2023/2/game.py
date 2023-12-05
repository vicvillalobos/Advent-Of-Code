from typing import List

class CubeSet:
    red = 0
    green = 0
    blue = 0

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    @property
    def sum(self):
        return self.red + self.green + self.blue 
    
    @property
    def power(self):
        return max(self.red,1) * max(self.green,1) * max(self.blue,1)


class GameSet:
    cubes = CubeSet

    def __init__(self, input: str):
        # Decode set
        input_cubes = input.split(", ")
        self.cubes = CubeSet()
        
        for cube in input_cubes:
            amount, color = cube.split(" ")

            if color == "red":
                self.cubes.red = int(amount)
            elif color == "green":
                self.cubes.green = int(amount)
            elif color == "blue":
                self.cubes.blue = int(amount)

class Game:
    id: int;
    sets: List[GameSet]

    def __init__(self, input: str):
        # Decode input
        self.sets = []
        
        header, data = input.split(": ")
        self.id = int(header.split(" ")[1])
        
        sets_data = data.split("; ")

        for set_data in sets_data:
            self.sets.append(GameSet(set_data))

    def is_possible(self, red: int, green: int, blue: int):

        cube_amount = red + green + blue

        for set in self.sets:
            # Check total amount of cubes
            if set.cubes.sum > cube_amount:
                return False

            # Check individual amounts
            if set.cubes.red > red or set.cubes.green > green or set.cubes.blue > blue:
                return False
            
        return True

    @property
    def min_cubeset(self) -> CubeSet:

        max_red = 0
        max_green = 0
        max_blue = 0

        for set in self.sets:
            max_red = max(max_red, set.cubes.red)
            max_green = max(max_green, set.cubes.green)
            max_blue = max(max_blue, set.cubes.blue)
        
        return CubeSet(max_red, max_green, max_blue)
            