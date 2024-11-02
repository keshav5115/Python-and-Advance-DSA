'''
A Linked List is a linear data structure where elements (called nodes) 
are stored in a sequence, but unlike arrays, they are not stored 
in contiguous memory locations. Each node in a linked list contains:

Data: The value or information of the element.
Pointer/Reference: A reference (or link) to the next node in the sequence.

Components of a Linked List:
Node: Each element in a linked list is called a node, and it consists 
of:
    Data: Holds the value of the node.
    Next: A pointer/reference to the next node in the list.
    Head: A pointer to the first node in the linked list. 
        If the list is empty, the head points to None or null.


'''




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
    
'Implementation of stack using linked list'
class LinkedList:
    class _Node:
        def __init__(self,element,ptr):
            self.element = element
            self.next    = ptr
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self,e):
        node = self._Node(e,self.head)
        self.head = node 
        self.size+=1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self.head.element
        self.head  = self.head.next
        self.size-=1
        return answer
    
if __name__ == '__main__':
    stack = LinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop()) # should print 3
    print(stack.pop()) # should print 2
    print(stack.pop()) # should print 1
    print(stack.pop()) # should raise exception 'Stack is empty'
        

        
