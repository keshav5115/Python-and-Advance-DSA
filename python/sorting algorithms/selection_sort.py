arr = [9,2,5,6,5,7,3,8,1]
def selectionSort(arr):
    # Traverse through all elements in the array
    for i in range(len(arr)-1):
        # Find the index of minimum element in the unsorted portion
        min_index = i
        for ind in range(i+1,len(arr)):
            if arr[min_index] > arr[ind]:
                min_index = ind 
        # Swap the found minimum element with the first element of the unsorted portion
        arr[min_index],arr[i] = arr[i],arr[min_index]
        
    return arr

print(selectionSort(arr)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    