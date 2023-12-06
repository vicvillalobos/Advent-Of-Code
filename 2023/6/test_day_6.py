from task_2023_6_1 import execute as ex1
from task_2023_6_2 import execute as ex2

def test_example_1():
    assert ex1("2023/6/example.csv") == 288

def test_example_2():
    assert ex2("2023/6/example.csv") == 71503