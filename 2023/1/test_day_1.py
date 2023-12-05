from task_2023_1_1 import execute as tb1ex
from task_2023_1_2 import execute as tb2ex, wordProcessing


def test_part_one():
    # Testing trebuchet_1 with the provided example values
    assert tb1ex("2023/1/example_1.csv")[1] == [12, 38, 15, 77]
    assert tb1ex("2023/1/example_1.csv")[0] == 142

def test_wordProcess():
    # Testing wordProcessing function with different case values
    assert wordProcessing("asdasd") == 0
    assert wordProcessing("asdasdas5") == 55
    assert wordProcessing("1") == 11
    assert wordProcessing("11") == 11
    assert wordProcessing("289") == 29
    assert wordProcessing("one1") == 11
    assert wordProcessing("one2") == 12
    assert wordProcessing("onetwo") == 12
    assert wordProcessing("one3two") == 12
    assert wordProcessing("one3three2two") == 12
    assert wordProcessing("oneight") == 18
    assert wordProcessing("twone3") == 23
    assert wordProcessing("twone") == 21
    assert wordProcessing("tthreeeoneoneight") == 38
    assert wordProcessing("8mnlsqkpqp18jkftxzfcklsgkvjr4threergdbrrzbb") == 83
    assert wordProcessing("hlrbll8vnhjlfjrkd") == 88
    assert wordProcessing("twoneighthree") == 23
    assert wordProcessing("8hbmfjxmqckxqrdjqxrnhg") == 88

def test_part_two_example_2():
    # Testing trebuchet_2 with the provided example values
    example2 = tb2ex("2023/1/example_2.csv")
    assert example2[1] == [29, 83, 13, 24, 42, 14, 76]
    assert example2[0] == 281
