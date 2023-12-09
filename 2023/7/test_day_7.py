from task_2023_7_1 import execute as ex1
from task_2023_7_2 import execute as ex2

def test_example_1():
    assert ex1("2023/7/example.csv") == 6440

def test_example_2():
    assert ex2("2023/7/example.csv") == 5905
