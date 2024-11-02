# Function to merge two halves
def merge(left, right):
    merged = []
    i = j = 0
    
    # Merge elements from both arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # If there are remaining elements in the left half
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # If there are remaining elements in the right half
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Function to divide the array
def divide(arr):
    # Base case: if array has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Find the middle index
    mid = len(arr) // 2
    
    # Recursively divide the array into two halves
    left_half = divide(arr[:mid])
    right_half = divide(arr[mid:])
    
    # Conquer (merge) the two halves
    return merge(left_half, right_half)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = divide(arr)
print("Sorted Array:", sorted_arr)
