def selection_sort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


_array = [17,59,23,70,11,42,10,31,95,20]

selection_sort(_array)

print(_array)