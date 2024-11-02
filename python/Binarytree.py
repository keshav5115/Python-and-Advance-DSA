'''
A tree is a hierarchical data structure in computer science consisting of nodes 
connected by edges, where each node contains data and may have child nodes.
It is unidirectional

Real-world Applications of Trees:
   1. File Systems: File directories are structured as a tree where folders are nodes and 
    subfolders or files are the children.
   2. Routing Algorithms: Trees are used in networking to represent routing paths.
   3.Databases: B-trees and B+ trees are used in database indexing.
   4. Artificial Intelligence: Decision trees are used in machine learning for 
    decision-making and classification problems.
   5. Compilers: Abstract syntax trees are used to represent the structure of program code.


Traversal Methods:
    Depth-First Search (DFS):

        Preorder Traversal: Visit the root, then recursively visit left and right subtrees.
        Inorder Traversal: Recursively visit the left subtree, visit the root, and 
                            then visit the right subtree. Common in BSTs.
        Postorder Traversal: Recursively visit left and right subtrees, then visit the root.

    Breadth-First Search (BFS):

        Also known as Level Order Traversal, it explores all the nodes at the present depth
        level before moving on to nodes at the next depth level.

'''



class BinaryTree:

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None 

    def _create_node(self,data):
        return BinaryTree(data)
    
    def insert_node(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = self._create_node(data)
                else:
                    self.left.insert_node(data)

            else:
                if self.right is None :
                    self.right = self._create_node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data
    def printTree(self):
      if self.left:
         self.left.printTree()
      print(self.data)
      if self.right:
         self.right.printTree()




    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    

    def preorderTraversal(self,root):
        res =[]
        if root :
            res.append(root.data)
            res=res + self.preorderTraversal(root.left)
            res=res + self.preorderTraversal(root.right)
        return res
    
    def postorderTraversal(self,root):
        res=[]
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res 
    def height(self,root):
        if not root:
            return -1
        else:
            lheight = self.height(root.left)
            rheight = self.height(root.right)
            if lheight > rheight:
                return lheight+1
            else:

                return rheight+1 
    def binarysearch(self,data):
        if self.data == data:
            return self
            
        elif self.data > data and self.left is not None:
            return self.left.binarysearch(data)
        elif self.data < data and self.right is not None :

            return self.right.binarysearch(data)
        else:
            return None
    def height_value(self,value):
        node = self.binarysearch(value)
        if node:
            return self.height(node)
        else:
            return -1

            
    def bfs(self,root):
        if not root:
            return []
        queue = []
        queue.append(root)
        traversal = []
        while queue:
            node = queue.pop(0)
            traversal.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal

root = BinaryTree(27)
root.insert_node(14)
root.insert_node(35)
root.insert_node(10)
root.insert_node(19)
root.insert_node(31)
root.insert_node(42)
# print(root.bfs(root))
print(root.height(root))
# print(root.binarysearch(35))
print(root.height_value(14))



# out = root.inorderTraversal(root)
# print(out)
# print(root.preorderTraversal(root))
# print(root.postorderTraversal(root))

'''
Depth-First Traversal (DFT):

    Pre-order Traversal (Root, Left, Right)
    In-order Traversal(Left, Root, Right)
    Post-order Traversal (Left, Right, Root)

 Breadth-First Traversal (BFT)
    Level-order Traversal visits nodes level by level from left to right. 
    This traversal uses a queue data structure to visit nodes level-wise.

'''

        