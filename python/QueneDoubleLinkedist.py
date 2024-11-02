class LinkedList:
    class _Node:
        def __init__(self,element,prev,ptr):
            self.element = element
            self.previous = prev
            self.next    = ptr

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def enque(self,e):
        node = self._Node(e,None,None)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        temp = self.tail 
        self.tail = node 
        self.tail.previous = temp
        self.size+=1
    def deque(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self.head.element
        self.head  = self.head.next
        self.size-=1
        return answer
    

def previous(queue,value):
    current = queue.head
    while current is not None and current.element!=value:
        current = current.next
    if current is None:
        return -1
    return current.previous.element if current.previous else -1
    
if __name__ == '__main__':
    obj=LinkedList()
    obj.enque(1)
    obj.enque(8)
    obj.enque(3)
    obj.enque(4)
    print(previous(obj,3))
    print(previous(obj,1))
    print(previous(obj,9))


        
        
