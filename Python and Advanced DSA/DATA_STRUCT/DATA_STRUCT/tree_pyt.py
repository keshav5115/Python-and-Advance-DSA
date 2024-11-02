# It is a non-linear data structure, It is a collection of entities called nodes.
# It is also called as heirarchical data structure
# It is unidirectional
# each node will have childrens and all nodes are connected by edges
# The last nodes are called as leaves or terminal nodes or external nodes
# nodes which belong to same nodes are called siblings

# Application
# bineary search tree
# Trees (with some ordering e.g., BST) provide moderate access/search
# (quicker than Linked List and slower than arrays).
# Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists).


# char of tree
# Root node can be used to traverse through all nodes
# If tree containes N nodes the num of edges will always N-l edges
# all children will have only one parent node, but parent can have multiple childrens

# Degree of node --> The num of children of that node is degree of node
# Degree of tree --> It is the node which contains highest num of children
# Level of tree ---> How many steps that tree contains
# Height of node ---> It is the longest num of edges connected to leaf node to that node
# Depth of tree --> It is the number of edges connected from root node to that noe

# Binary Tree: A tree whose elements have at most 2 children is called a binary tree.
# Since each element in a binary tree can have only 2 children, we typically name them the left
# and right child.

#  types of binart tree
# Full binary tree or strict binary tree --> all node other than leaf node can have only 0 or 2 child nodes  ## No1 child nodes
# complete binary tree ---> All level except last level have to be completely filled 
# and last level also have to be filled from left to right, it cannot
# have ore than 2 nodes
# perfect binary tree --> all internal nodes have two children and all leaf nodes are in same level
# Balanced binary tree --> it is a binary tree in whcih height of the left and right nodes difer atmost 1 (i.e have to find th edifff between the height of left and right sub tree, diff have to be 1 or lessthan 1)
# Pathological --> every parent has only one child node

# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

# sorting : https://stackabuse.com/sorting-algorithms-in-python/

# l1 = [5, 3, 8, 12, 4]

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self, data):  #self is root
        if self.key is None:
            self.key = data
            return 
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                
    def search(self, data):
        if self.key == data:
            print("Node is found!!")
            return 
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in Tree..")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in Tree..")
                    
root = BST(None)
# print(root.key)
# print(root.lchild)
# print(root.rchild)

# root.insert(78)
l1 = [6,3,1,6,98,3,7]
for val in l1:
    root.insert(val)
    

root.search(3)

