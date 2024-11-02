# Linked list is a linear data structure made up of chain of nodes in which each nodes
# contains a data and link or reference of next node

# In each node, it can contain only one data field and one link field or two links

# head node --> starting point of linked list
# tail node  --> ending point of linked list

# The nodes are stored randomly in memory

# Advantage:
# Inserting and deleting is easy in linked list
# They are used to represent polynomials (x2+x-12)

# Disadvantage
# Need extra memory coz it stores element and memory address
# Accessing random node is not possible

# In real world
# Used in web browser to go to prev and next page
# Music player
# Image viewer
# Like a treasure hunt game

# Types
# single linked list --> If nodes contain only one link, It allows to move in one direction only
# doubly linked list --> If nodes contains two links
# circular -->

# https://www.youtube.com/watch?v=JlMyYuY1aXU


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
            
        print(elems)
    
    def get(self, index):
        if index >= self.length():
           return "Error Index out of range!!!!"
        try:
            cur_idx = 0
            cur_node = self.head
            
            while True:
                cur_node= cur_node.next
                if cur_idx==index:
                    return cur_node.data
                cur_idx+=1
        except:
            pass
            
        
lst = linked_list()
# lst.display()

lst.append(0)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5) 
# print(lst.get(4))

lst.display()

# --------------------------------------------------------------------------------------------------------
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.reference = None

# class linkdlist:
#     def __init__(self):
#         self.head = None

#     def print_LL(self):  #traverse
#         if self.head is None:
#             print("Empty Linked list")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.reference

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.reference= self.head
#         self.head = new_node

#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node

# LL1 = linkdlist()
# LL1.add_end(20)
# LL1.add_begin(10)
# LL1.add_begin(1)
# LL1.add_begin(102)

# LL1.print_LL() 





















# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
