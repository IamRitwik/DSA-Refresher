def recursive_binary_search(arr, target, low, high):
    """
    Searches for a target value in a sorted array using recursive binary search.

    Args:
        arr: A sorted list or array.
        target: The value to search for.
        low: The starting index of the current search space.
        high: The ending index of the current search space.

    Returns:
        The index of the target value if found, otherwise -1.
    """
    if low > high:
        return -1  # Base case: Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Target found at the middle index
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)  # Search in the right half
    else:
        return recursive_binary_search(arr, target, low, mid - 1)  # Search in the left half

# Example usage:
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23
index = recursive_binary_search(sorted_list, target_value, 0, len(sorted_list) - 1)

if index != -1:
    print(f"Element {target_value} found at index {index}")
else:
    print(f"Element {target_value} not found in the list")