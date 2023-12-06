from task_2023_1_1 import execute as tb1ex
from task_2023_1_2 import execute as tb2ex, word_processing


def test_part_one():
    # Testing trebuchet_1 with the provided example values
    assert tb1ex("2023/1/example_1.csv")[1] == [12, 38, 15, 77]
    assert tb1ex("2023/1/example_1.csv")[0] == 142

def test_wordProcess():
    # Testing word_processing function with different case values
    assert word_processing("asdasd") == 0
    assert word_processing("asdasdas5") == 55
    assert word_processing("1") == 11
    assert word_processing("11") == 11
    assert word_processing("289") == 29
    assert word_processing("one1") == 11
    assert word_processing("one2") == 12
    assert word_processing("onetwo") == 12
    assert word_processing("one3two") == 12
    assert word_processing("one3three2two") == 12
    assert word_processing("oneight") == 18
    assert word_processing("twone3") == 23
    assert word_processing("twone") == 21
    assert word_processing("tthreeeoneoneight") == 38
    assert word_processing("8mnlsqkpqp18jkftxzfcklsgkvjr4threergdbrrzbb") == 83
    assert word_processing("hlrbll8vnhjlfjrkd") == 88
    assert word_processing("twoneighthree") == 23
    assert word_processing("8hbmfjxmqckxqrdjqxrnhg") == 88

def test_part_two_example_2():
    # Testing trebuchet_2 with the provided example values
    example2 = tb2ex("2023/1/example_2.csv")
    assert example2[1] == [29, 83, 13, 24, 42, 14, 76]
    assert example2[0] == 281
