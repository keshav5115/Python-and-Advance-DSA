#[4,8,2,9]
def conquer(left,right):#[8],[2]
    result =[]#[2]
    i = j= 0
    while i<len(left) and  j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])#[2,8]
    result.extend(right[j:])
    return result

def merge_sort(arr):#[8,2]
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    lefthalf = arr[:mid]#[8]
    righthalf = arr[mid:]#[2]
    left_sort = merge_sort(lefthalf)#[8]
    right_sort = merge_sort(righthalf)#[2]
    return conquer(left_sort,right_sort)

print(merge_sort([4,8,2,1,5]))