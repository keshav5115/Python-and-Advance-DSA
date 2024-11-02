#WAP to find first index of an element by using recursion
# eg- [1, 2, 3, 1, 2, 3]
# element=2, first occurence = 1

def firstIndexOfAnElement(l1,x):
    # 1. Base Case
    if(len(l1)==0):
        return -1
    
    if(l1[0]==x):
        return 0
    
    ansFromRecursion =  firstIndexOfAnElement(l1[1:],x)

    if(ansFromRecursion==-1):
        return ansFromRecursion
    else:
        return ansFromRecursion +1

lst=[1,2,3,1,2,3,1,2,3]
print(firstIndexOfAnElement(lst,2))

#



def lastIndexOfAnElement(l1,x):
    # 1. Base Case
    if(len(l1)==0):
        return -1
    if(l1[len(l1)-1]==x):
        return len(l1) - 1
    
    
    lastFromRecursion =lastIndexOfAnElement(l1[:len(l1)-1],x)#6,2
    if lastFromRecursion==-1:
        return lastFromRecursion
    else:
        return lastFromRecursion
    

# print(firstIndexOfAnElement([3,2,5,2,8,2,1],2))
# print(firstIndexOfAnElement([3,2,5,2,8,2,1],10))
# print(firstIndexOfAnElement([1,2,5,2,8,2,1],1))
# print(lastIndexOfAnElement([3,2,5,2,8,2,1],10))


