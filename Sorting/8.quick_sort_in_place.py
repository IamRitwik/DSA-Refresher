def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # step 1 - partition the array
        pivot = partition(arr, low, high)
        # step 2 - recursively sort elements
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high] # last element as pivot
    i = low - 1       # pointer for smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


_array = [17,59,23,70,11,42,10,31,95,20]
quick_sort(_array)
print(_array)