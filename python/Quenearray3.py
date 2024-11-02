class QueueArray:
    ARRAY_SIZE = 5
    def __init__(self):
        self._data = [None]*QueueArray.ARRAY_SIZE
        self.first = 0
        self.size  = 0

    def push(self,e):
        if self.size>=QueueArray.ARRAY_SIZE:
            raise Exception('Queue is full')
        position = (self.size+self.first)% QueueArray.ARRAY_SIZE
        self._data[position]=e
        self.size+=1

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self.first]
        self._data[self.first]=None 
        self.first=(self.first+1)%QueueArray.ARRAY_SIZE
        self.size-=1
        return answer

if __name__ == '__main__':
    obj = QueueArray()
    obj.push(3)
    obj.push(6)
    obj.push(9)

'''
Characteristics:
    Push Operation: Adds an element at the next available slot, computed using modular arithmetic, making it a circular buffer.
    Pop Operation: Pops an element using modular arithmetic to wrap around the array.
    Fixed Size: The queue has a fixed capacity (ARRAY_SIZE = 5 in this case).
    Circular Buffer: Efficient memory usage, as the queue uses a circular buffer to avoid memory waste.
Pros:
    Efficient Push/Pop: Both push and pop are O(1).
    Memory Efficiency: Unlike the second implementation, this method uses a fixed-size buffer, so memory usage is constant.
Cons:
    Fixed Size: The queue is bounded by a predefined size,
    which may require resizing logic if the number of elements exceeds the capacity.

'''
