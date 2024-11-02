# data Structures
'''
# A data structure is a particular way of 
# organizing data in a 
# computer so that it can be used effectively.'''
'''
# DEF: A stack is a data structure that 
# stores items in an Last-In/First-Out manner.
# This is frequently referred to as LIFO. 
#This means that the last element added to the stack 
# will be the first one to be removed.'''
# This is in contrast to a queue,
# which stores items in a First-In/First-Out (FIFO) manner.

# Eg:
# It’s probably easiest to understand a stack 
# if you think of a use case 
# you’re likely familiar with:

# the Undo feature in your editor.

# In python stack can be implimented in diff ways

# 1.)List
# 2.)collections.deque
# 3.)queue

# from collections import deque
# l1 = []
# l1.append(1)
# l1.append(2)
# l1.append(3)

# print(l1.pop())
# print(l1.pop())

# print(l1)


# 1.Using List
l1 = []
n = int(input('Enter the limit: '))
i = 1
while i <= n:
    print('Enter 1.Add Items in Stack, 2.Delete Items in Stack, 3.To Exit')
    choice = int(input('Choose the operation: '))
    if choice == 1:
        num = eval(input('Enter the input: '))
        l1.append(num)
        print('Item Added')
        print(l1)
    if choice == 2:
        if l1 == []:
            print('Stack is empty')
        else:
            print(l1.pop())
            print('Item Deleted')
        print(l1)
    if choice == 3:
        break
    i = i+1
# ----------------------------------------------------------

# 2.)collection deque
# from collections import deque
# (Doubly Ended Queue)

# stack = deque()
# n = int(input('Enter the limit: '))
# i = 1
# while i <= n:
#     print('Enter 1.Add Items in Stack, 2.Delete Items in Stack, 3.To Exit')
#     choice = int(input('Choose the operation: '))
#     if choice == 1:
#         num = int(input('Enter the input: '))
#         stack.append(num)
#         print('Item Added')
#         print(stack)
#     if choice == 2:
#         if not stack:
#             print('Stack is empty')
#         else:
#             stack.pop()
#             print('Item Added')
#         print(stack)
#     if choice == 3:
#         break
#     i = i+1
# --------------------------------------------------------------------

# from queue import LifoQueue
# # i = 0
# stack = LifoQueue(maxsize=7)
# # # stack = LifoQueue()
# # stack.put('Hello')
# stack.get()
# print(stack)

# --------------------------------------------------------------------
# use stack to chek weather, the set of paranthesis are balanced or not

# Eg:
#     "{[]}" --> balanced paranthesis
#     "())" --> unbalanced
#     "((" ---> unbalanced



# open_list = ["[","{","("]
# close_list = ["]","}",")"]

# def check(myStr):
# 	stack = []
# 	for i in myStr:
# 		if i in open_list:
# 			stack.append(i)
# 		elif i in close_list:
# 			pos = close_list.index(i)
# 			if ((len(stack) > 0) and
# 				(open_list[pos] == stack[len(stack)-1])):
# 				stack.pop()
# 			else:
# 				return "Unbalanced"
# 	if len(stack) == 0:
# 		return "Balanced"
# 	else:
# 		return "Unbalanced"

# string = "{[]{()}}"
# print(string,"-", check(string))

# string = "[{}{})(]"
# print(string,"-", check(string))

# string = "((()"
# print(string,"-",check(string))


# l1 = []
# n = int(input("Enter the numer of elements: "))

# (){} --> balanced
# ({} --> unbalanced