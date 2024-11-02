def binarySearch(arr,target,low,high):
    # if element is not present
    if low>high:
        return -1
    mid = (low+high)//2
    # if element is present at the middle
    if arr[mid] == target:
        return mid
    # if element is smaller than mid element
    elif arr[mid] > target and arr[:mid]:
        return binarySearch(arr, target, low,mid-1)
    # if element is greater than mid element
    elif arr[mid] < target:
        return binarySearch(arr, target,mid+1,high)
    
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binarySearch(arr, 13,0,len(arr)-1)) # True