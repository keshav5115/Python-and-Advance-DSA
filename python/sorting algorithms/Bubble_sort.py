'''
Bubble sort is a simple comparison-based sorting algorithm 
that repeatedly steps through the list, compares adjacent elements, 
and swaps them if they are in the wrong order. 
This process is repeated until the list is sorted.

'''
'''
How Bubble Sort Works:
1,Compare the first two elements of the array.
2,If the first element is greater than the second, swap them.
3,Move to the next pair of elements and repeat the comparison and swapping process.
4,After each pass through the list, the largest unsorted element will have "bubbled" to its correct position.
5,Repeat the process for the rest of the elements until the entire list is sorted.

'''
'''
Time Complexity:
Worst-case and Average-case Time Complexity: O(n²) where n is the number of elements.
Best-case Time Complexity: O(n) if the array is already sorted.
'''
# Ascending order
def bubble_sort(arr):
    for i in range(len(arr)):#0,1,2,3
        min_index = i#9
        for ind in range(i+1,len(arr)):
            if arr[min_index] > arr[ind]:
                min_index = ind
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr

arr = [9,8,7,6,5,4,3,2,1]
print(bubble_sort(arr))



'''
end=time.time()
print(end-start)

start = time.time()
# Descending order
for i in range(len(arr)):
    max_index=i
    for index in range(i+1,len(arr)):
        if arr[max_index] < arr[index]:
            max_index = index
    arr[max_index],arr[i] = arr[i],arr[max_index]
    print(arr)

print(arr) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

end=time.time()
print(end-start)
'''
