class QueneArray:
    def __init__(self):
        self._data = []
        self.first = 0

    def push(self,e):
        self._data.append(e)
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == self.first
    def pop(self):
        if self.is_empty():
            raise Exception('Quene is empty')
        answer = self._data[self.first]
        self._data[self.first]=None 
        self.first+=1
        return answer

if __name__ == '__main__':
    obj = QueneArray()
    obj.push(3)
    obj.push(6)
    obj.push(9)

'''
Characteristics:
    Push Operation: Still appends to the end.
    Pop Operation: Pops the element by shifting a pointer (first) instead of removing elements from the list.
    Memory Inefficiency: The list keeps growing, and elements in the front are set to None but not removed.
Pros:
    Improved pop Efficiency: The pop operation only increments the first pointer, 
    making it O(1).
Cons:
    Memory Inefficiency: Over time, unused None entries pile up at the front of the list.
    List can grow indefinitely.


    You may need a mechanism to shrink the list when too many None values accumulate.
    

'''
