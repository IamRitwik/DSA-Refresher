import sys

lst = []
for i in range(100):
    lst.append(i)
    print(f"Length: {len(lst)}, Size in bytes: {sys.getsizeof(lst)}")
