class BRT:
    def __init__(self,data):
        self.left = None
        self.right = None 
        self.data  = data 

    def create_node(self,data):
        return BRT(data)
    
    def insert_node(self,data):

        if self.data:
            if self.data > data:
                if self.left is None :
                    self.left = self.create_node(data)
                else:
                    self.left.insert_node(data)
            else:
                if self.right is None :
                    self.right = self.create_node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def binarysearch(self,data):
        if self.data == data:
            return data
            
        elif self.data > data and self.left is not None:
           return  self.left.binarysearch(data)
        elif self.data < data and self.right is not None :

            return self.right.binarysearch(data)
        else:
            return None

    def deletenode(self,data):
        if self.data is None :
            return 

        if self.data > data :
           self.left = self.left.deletenode(data)
        elif self.data < data :

            self.right = self.right.deletenode(data)
        else:
            if self.left is None :
                return self.right
                
            elif self.right is None:
                return  self.left
            
            self.data = self.right.minvalue()
            self.right = self.right.deletenode(self.data)

        return self        
    def minvalue(self):
        current = self 
        while current.left :
            current = current.left
        return current.data
    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

                




root = BRT(27)
root.insert_node(14)
root.insert_node(35)
root.insert_node(10)
root.insert_node(19)
root.insert_node(31)
root.insert_node(42)
print(root.binarysearch(32))
print(root.binarysearch(19))
# print(root.inorderTraversal(root))
# root.deletenode(14)
# print(root.inorderTraversal(root))
        