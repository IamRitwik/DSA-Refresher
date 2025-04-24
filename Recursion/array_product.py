num = [2,4,5,8,3]

def iterative(arr):
    total = 1
    for n in arr:
        total = total * n
    return total

print(iterative(num))

def recursive(arr, index):
    if index == 0:
        return arr[0]
    else:
        return arr[index] * recursive(arr, index -1)

print(recursive(num, len(num) - 1))

def arr_product(arr):
    if not arr:
        return 1
    return arr[0] * arr_product(arr[1:])

print(arr_product(num))