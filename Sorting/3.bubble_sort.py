def bubble_sort(array):
    for i in range(len(array) - 1):
        has_swapped = False
        for j in range(len(array) -1, i, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                has_swapped = True
        if not has_swapped:
            break
    return array

_array = [17,59,23,70,11,42,10,31,95,20]

bubble_sort(_array)

print(_array)