def linear_search(my_list, target):
    """
    Performs a linear search on a list.

    Args:
        my_list: The list to search.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    # Iterate through the list, checking each element.
    for index, element in enumerate(my_list):
        if element == target:
            return index  # Return the index if the target is found.
    return -1  # Return -1 if the target is not found in the list.

# Example Usage
my_list = [10, 5, 2, 8, 12, 7]
target_element = 8

result = linear_search(my_list, target_element)

if result != -1:
    print(f"Target element {target_element} found at index {result}")
else:
    print(f"Target element {target_element} not found in the list")

target_element = 15
result = linear_search(my_list, target_element)
if result != -1:
    print(f"Target element {target_element} found at index {result}")
else:
    print(f"Target element {target_element} not found in the list")
