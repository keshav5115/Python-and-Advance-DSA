'''
1) Assume the first element is already sorted.
2) Pick the next element from the unsorted portion of the array.
3) Compare it with the elements in the sorted portion and shift the elements greater than the current element to the right.
4) Insert the current element in the correct position.
5) Repeat until all elements are sorted.
'''

arr=[9,8,7,6,5,4,3,2,1]
size = len(arr)

for i in range(1,size):
    key = arr[i]
    j   = i-1 #1

    while j>=0 and key < arr[j]:#8<9
        arr[j+1] = arr[j]#[8,8,9]
        j=j-1
    arr[j+1] = key#[8,9]
print(arr)
'''
Time Complexity:
Worst-case and Average-case Time Complexity: O(n²), where n is the number of elements.
Best-case Time Complexity: O(n), when the array is already sorted.
'''