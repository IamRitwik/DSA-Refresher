def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23
index = binary_search(sorted_list, target_value)

print(index, sorted_list[index])