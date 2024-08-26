def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        cursor = array[i]
        pos = i - 1

        while pos >=0 and cursor < array[pos]:
            array[pos + 1] = array[pos]
            pos -= 1

        array[pos+1] = cursor

    return array
