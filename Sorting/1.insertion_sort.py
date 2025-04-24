def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
    return array


_array = [11,7,59,23,90,77,2]

insertion_sort(_array)

print(_array)
