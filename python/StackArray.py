class StackArray:

    def __init__(self):

        self._data=[]

    def __len__(self):
         return len(self._data)

    def push(self,val):
        self._data.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception ('stack is empty')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self._data[-1]

if __name__ == '__main__':
    S = StackArray()
