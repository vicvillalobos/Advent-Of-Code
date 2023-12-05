from typing import List

class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class SchematicNumber:
    # each part number will be a list of tiles in order.
    
    def __init__(self, schematic):
        self.schematic = schematic
        self.characters : List[Vector2] = []
        self.values: List[str] = []

    def append(self, x: int, y: int, value: str):
        self.characters.append(Vector2(x, y))
        self.values.append(value)

    def has_number(self, x: int, y: int):

        for c in self.characters:
            if c.x == x and c.y == y:
                return True
        return False


    @property
    def is_part(self):
        # check surrounding tiles for each number
        for v2 in self.characters:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    r = self.schematic.get(v2.x + dx, v2.y + dy)
                    if not r.isdigit() and r != ".":
                        return True
                    
        return False
    
    @property
    def number(self):
        if len(self.values) <= 0:
            return -1
        return int("".join(self.values))
    
    def __str__(self) -> str:
        if self.is_part:
            return str(self.number) + " (P)"
        else:
            return str(self.number)
    
    def __repr__(self) -> str:
        if self.is_part:
            return str(self.number) + " (P)"
        else:
            return str(self.number)



class Schematic:

    def __init__(self, schematic_input: List[str]):
        self.map_data = schematic_input

        self.width = len(self.map_data[0])
        self.height = len(self.map_data)
        self.numbers = self.calculate_numbers()
        self.gears : List[Gear] = self.calculate_gears()

    def get(self, x: int, y: int):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return "."
        
        return self.map_data[y][x]
    
    def get_number_at_pos(self, x: int, y: int):
        # Checks if the position exists in a number.
        for n in self.numbers:
            if n.has_number(x, y):
                return n
            
        return None
    
    def calculate_numbers(self) -> List[SchematicNumber]:

        numbers = []
        for y in range(self.height):

            line_numbers = []
            writing_mode = False
            buffer_number = None
            
            for x in range(self.width):
                
                char = self.get(x,y)

                if writing_mode is True:
                    if not char.isdigit():
                        # Stop writing the number
                        line_numbers.append(buffer_number)
                        buffer_number = None
                        writing_mode = False

                    else:
                        # Write the number into the buffer.
                        buffer_number.append(x, y, char)

                else:
                    if char.isdigit():
                        # Clear the buffer and write the character
                        buffer_number = None
                        buffer_number = SchematicNumber(self)
                        buffer_number.append(x, y, char)
                        writing_mode = True

            if buffer_number is not None:
                line_numbers.append(buffer_number)
                buffer_number = None
            writing_mode = False

            numbers.extend(line_numbers)
        
        return numbers
    
    def calculate_gears(self) -> List:
        gears = []
        for y in range(self.height):
            for x in range(self.width):

                char = self.get(x,y)

                if char == "*":
                    gears.append(Gear.create(x, y, self))

        return gears
    
    @property
    def valid_gears(self):
        return [g for g in self.gears if g.is_valid]
    
    @property
    def gear_ratio_sum(self):
        return sum([g.ratio for g in self.gears if g.is_valid])
    
    @property
    def part_numbers(self):
        return [n.number for n in self.numbers if n.is_part]
    
    @property
    def numbers_sum(self):
        return sum(self.numbers)
        
    @property
    def part_numbers_sum(self):
        return sum(self.part_numbers)


class Gear:
    def __init__(self, position: Vector2, parts: List[SchematicNumber]):
        self.position = position
        self.parts = parts

    @property
    def is_valid(self):
        return len(self.parts) == 2
    
    @property
    def ratio(self):
        if self.is_valid:
            return self.parts[0].number * self.parts[1].number
        return 0
    
    def __repr__(self):
        if self.is_valid:
            return f"Gear at {self.position} (V)"
        return f"Gear at {self.position}"

    @staticmethod
    def create(x: int, y: int, schematic: Schematic):
        # get the parts adjacent to it
        parts : List[SchematicNumber] = []

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:

                num = schematic.get_number_at_pos(x + dx, y + dy)

                try:
                    parts.index(num)
                    part_found = True
                except:
                    part_found = False

                if num is not None and not part_found:
                    parts.append(num)

        return Gear(Vector2(x,y), parts)