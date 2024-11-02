'''
A deque (short for double-ended queue) is a generalized queue 
that allows insertion and removal of elements from both ends 
(front and back). 
'''


class QueneArray:
    ARRAY_SIZE = 5
    def __init__(self):
        self._data = [None]*QueneArray.ARRAY_SIZE
        self.first = 0
        self.last  = 0
        self.size  = 0

    def add_last(self,e):
        if self.size>=QueneArray.ARRAY_SIZE:
            raise Exception('Quene is full')
        # position = (self.size+self.last)% QueneArray.ARRAY_SIZE
        if self.is_empty():
            position = self.last
        else:
            position = (self.last+1) % QueneArray.ARRAY_SIZE
        
        self._data[position]=e
        self.size+=1
        self.last=position
        

    def add_first(self,e):
        if self.size>=QueneArray.ARRAY_SIZE:
            raise Exception('Quene is full')
        if self.is_empty():
            position = self.first
        else:
            position = (self.first + QueneArray.ARRAY_SIZE-1) % QueneArray.ARRAY_SIZE

        self._data[position]=e
        self.size+=1
        self.first = position

        

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self.size == 0

    def delete_first(self):
        if self.is_empty():
            raise Exception('Quene is empty')
        answer = self._data[self.first]
        self._data[self.first]=None 
        self.size-=1
        if self.size == 0:
            self.first = self.last = 0
        else:
            self.first=(self.first+1)%QueneArray.ARRAY_SIZE
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Exception('Quene is empty')
        answer = self._data[self.last]
        self._data[self.last]=None 
        self.size-=1
        if self.size == 0:
            self.first = self.last = 0
        else:
            self.last=(self.first + self.size-1) % QueneArray.ARRAY_SIZE
        return answer



if __name__ == '__main__':
    obj = QueneArray()
    

