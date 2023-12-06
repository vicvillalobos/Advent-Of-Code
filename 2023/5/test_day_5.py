from task_2023_5_1 import execute as ex1
from task_2023_5_2 import execute as ex2

def test_example_1():
    assert ex1("2023/5/example.csv") == 35

def test_example_2():
    assert ex2("2023/5/example.csv") == 46