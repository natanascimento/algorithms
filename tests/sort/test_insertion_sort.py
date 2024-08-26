from pyalgo.sort import insertion_sort


def test_insertion_sort_injection_should_be_sorted():
    a = [1,4,5,6,7,2]
    
    res = insertion_sort(array=a)

    assert res == [1,2,4,5,6,7]


def test_insertion_sort_injection_should_be_sorted_with_string():
    a = ["1","4","5","6","7","2"]
    
    res = insertion_sort(array=a)

    assert res == ["1","2","4","5","6","7"]
