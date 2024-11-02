
class QueneArray:
    def __init__(self):
        self._data = []

    def push(self,e):
        self._data.append(e)

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def pop(self):
        if self.is_empty():
            raise Exception('Quene is empty')
        return self._data.pop(0)

if __name__ == '__main__':
    obj = QueneArray()
    obj.push(5)
    obj.push(6)
    obj.push(2)
    start= time.time()
    obj.pop()
    end= time.time()
    print(end-start)

'''
Characteristics:
    Push Operation: Adds elements to the end of the list.
    Pop Operation: Removes elements from the front using pop(0).
    Dynamic Size: List size can grow indefinitely as Python lists are dynamically resized.
Pros:
    Simplicity and clarity.
    The size is dynamic, and you don't need to worry about a fixed array size.
Cons:
    Inefficiency in pop: Removing the first element in a list requires 
    shifting all subsequent elements, which has a time complexity of 𝑂(𝑛)
    where 𝑛 is the number of elements.


'''

