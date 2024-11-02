#Implimentation of Queue using Linked List
class LinkedList:
    class _Node:
        def __init__(self,element,ptr):
            self.element = element
            self.next    = ptr

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enque(self,e):
        node = self._Node(e,None)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node 
        self.tail = node 
        self.size+=1

    def deque(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self.head.element
        self.head  = self.head.next
        self.size-=1
        return answer
if __name__ == '__main__':
    queue = LinkedList()
    queue.enque(1)
    queue.enque(2)
    queue.enque(3)
    print(queue.deque())
    print(queue.deque())
    print(queue.deque())
    print(queue.is_empty())
        
        
