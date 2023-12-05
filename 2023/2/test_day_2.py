from task_2023_2_1 import execute as cc1ex
from task_2023_2_2 import execute as cc2ex
from game import Game

def test_example_1():
    assert cc1ex("2023/2/example.csv", 12, 13, 14) == 8

def test_game():
    game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    sums_1 = [7, 9, 2]
    powers_1 = [12, 12, 2]
    cubeset_1 = game_1.min_cubeset

    assert game_1.id == 1
    for i in range(len(game_1.sets)):
        assert game_1.sets[i].cubes.sum == sums_1[i]
        assert game_1.sets[i].cubes.power == powers_1[i]
    
    assert cubeset_1.red == 4
    assert cubeset_1.green == 2
    assert cubeset_1.blue == 6

def test_example_2():
    assert cc2ex("2023/2/example.csv") == 2286
