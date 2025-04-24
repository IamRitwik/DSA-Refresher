def heapify(array):
    last_parent_idx = len(array) // 2 - 1
    for idx in range(last_parent_idx, -1, -1):
        move_down(array, idx, len(array) - 1)
    return array

def move_down(array, start_idx, end_idx):
    child_idx = 2 * start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
            start_idx = child_idx
            child_idx = 2 * start_idx + 1
        else:
            break

sample_array = [17,59,23,70,11,42,10,31,95,20]

print(heapify(sample_array))