arr = [9,8,7,6,5,1,4,3,2]

# Using Bubble Sort
'''
for i in range(len(arr)):#0,1,2,3
    min_index = i#9
    for ind in range(i+1,len(arr)):
        if arr[min_index] > arr[ind]:
            min_index = ind
    arr[min_index],arr[i] = arr[i],arr[min_index]
    print(arr)

print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

for i in range(len(arr)):
    max_index=i
    for index in range(i+1,len(arr)):
        if arr[max_index] < arr[index]:
            max_index = index
    arr[max_index],arr[i] = arr[i],arr[max_index]
    print(arr)

print(arr) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
