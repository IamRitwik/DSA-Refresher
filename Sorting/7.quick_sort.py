def quick_sort(array):
    if len(array) < 2:
        return array
    return partition(array, 0, len(array) -1)

def partition(array, start, end):
    if start >= end:
        return

    pivot = end
    boundary = start
    for i in range(start, end):
        if array[i] <= array[pivot]:
            array[boundary], array[i] = array[i], array[boundary]
            boundary += 1
    array[boundary], array[end] = array[end], array[boundary]
    partition(array, start, boundary -1)
    partition(array, boundary +1, end)
    return array

_array = [17,59,23,70,11,42,10,31,95,20]
quick_sort(_array)
print(_array)