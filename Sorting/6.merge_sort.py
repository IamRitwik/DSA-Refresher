def merge_sort(array):
    if len(array) < 2:
        return array
    first_half = merge_sort(array[ : len(array) // 2])
    second_half = merge_sort(array[len(array) // 2 : ])
    return merge(first_half, second_half)


def merge(first_half, second_half):
    result = []
    i = j = 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1
    while i < len(first_half):
        result.append(first_half[i])
        i += 1
    while j < len(second_half):
        result.append(second_half[j])
        j += 1
    return result

_array = [17,59,23,70,11,42,10,31,95,20]
result = merge_sort(_array)
print(result)