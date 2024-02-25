from my_project import *

def test_average():
    assert get_average([1]) == 1
    assert get_average([2, 1]) == 1.5
    assert get_average([10, 50, 30]) == 30
    assert get_average([0, 0, 0, 4]) == 1


def test_data_set():
    assert do_algorithm([1, 2, 2, 5, 5]) == 3
