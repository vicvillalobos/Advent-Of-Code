from task_2023_3_1 import execute as gr1ex
from task_2023_3_2 import execute as gr2ex
from schematic import Schematic

def test_example_1():
    assert gr1ex("2023/3/example.csv") == 4361

def test_example_1_2():
    assert gr1ex("2023/3/example_2.csv") == 3846

def test_example_1_3():
    assert gr1ex("2023/3/example_3.csv") == 1

def test_example_2():
    assert gr2ex("2023/3/example.csv") == 467835


# 543410 is too low.
def test_schematic():

    with open('2023/3/example.csv') as f:
        data = f.read().split('\n')

    schem = Schematic(data)

    assert schem.width == 10
    assert schem.height == 10

    numbers = schem.numbers

    expected_numbers = [467, 114, 35, 633, 617, 58, 592, 755, 664, 598]
    expected_parts = [True, False, True, True, True, False, True, True, True, True]

    for n in range(len(numbers)):

        assert numbers[n].number == expected_numbers[n]
        assert numbers[n].is_part == expected_parts[n]


    