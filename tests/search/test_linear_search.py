from pyalgo.search import linear_search


def test_linear_search_value_should_be_found():
    target = 3
    array = [1,2,3,7]

    res = linear_search(array=array, target=target)

    assert array[res] == target


def test_linear_search_value_should_not_found():
    target = 9
    array = [1,2,3,7]

    res = linear_search(array=array, target=target)

    assert res == -1
