def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) -1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(quick_sort(arr)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
