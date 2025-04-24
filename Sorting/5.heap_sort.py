def heap_sort(array):
    heapify(array)
    for end_idx in range(len(array) -1, 0, -1):
        array[0], array[end_idx] = array[end_idx], array[0]
        move_down(array, 0, end_idx - 1)
    return array


def heapify(array):
    last_leaf_idx = len(array) //2 - 1
    end_idx = len(array) -1
    for idx in range(last_leaf_idx, -1, -1):
        move_down(array, idx, end_idx)

def move_down(array, start_idx, end_idx):
    child_idx = 2 * start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx = child_idx + 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
            start_idx = child_idx
            child_idx = 2 * start_idx + 1
        else:
            break

_array = [17,59,23,70,11,42,10,31,95,20]
heap_sort(_array)
print(_array)