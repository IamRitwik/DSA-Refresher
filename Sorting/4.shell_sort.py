def shell_sort(array):
    gaps = [5,3,1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j+gap] < array[j] and j >= 0:
                array[j], array[j+gap] = array[j+gap], array[j]
                j = j - gap
    return array


_array = [11,7,59,23,90,77,2]

shell_sort(_array)

print(_array)