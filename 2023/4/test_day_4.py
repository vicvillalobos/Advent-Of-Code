from task_2023_4_1 import execute as sc1ex
from task_2023_4_2 import execute as sc2ex

def test_example_1():
    assert sc1ex("2023/4/example.csv") == 13

def test_example_1_2():
    assert sc1ex("2023/4/example_2.csv") == 559

def test_example_2():
    assert sc2ex("2023/4/example.csv") == 30