# Define a class to represent a node in the tree
class TreeNode:
    def __init__(self, name, position):
        self.name = name        # Employee name
        self.position = position # Employee position
        self.children = []      # List to hold children (subordinates)

    # Function to add child nodes (subordinates)
    def add_child(self, child_node):
        self.children.append(child_node)

    # Function to print the tree hierarchy
    def print_tree(self, level=0):
        indent = " " * (level * 4)  # Indentation to represent tree levels
        print(f"{indent}{self.position}: {self.name}")  # Display position and name
        if self.children:
            for child in self.children:
                child.print_tree(level + 1)  # Recursively print each child

# Step 1: Create the root node (CEO)
ceo = TreeNode("John Smith", "CEO")

# Step 2: Create other top-level managers
cto = TreeNode("Jane Doe", "CTO")
cfo = TreeNode("Robert Brown", "CFO")
coo = TreeNode("Emily Davis", "COO")

# Step 3: Add the top-level managers as children of the CEO
ceo.add_child(cto)
ceo.add_child(cfo)
ceo.add_child(coo)

# Step 4: Add employees under the CTO
cto.add_child(TreeNode("Dev1", "Developer"))
cto.add_child(TreeNode("Dev2", "Developer"))

# Step 5: Add employees under the CFO
cfo.add_child(TreeNode("Acc1", "Accountant"))
cfo.add_child(TreeNode("Acc2", "Accountant"))

# Step 6: Add employees under the COO
coo.add_child(TreeNode("Ops1", "Operations Staff"))
coo.add_child(TreeNode("Ops2", "Operations Staff"))

# Step 7: Print the company hierarchy
ceo.print_tree()







'''
Explanation of Each Step
    Defining the TreeNode Class:

        1. We create a TreeNode class that will represent each employee in the company. 
           The __init__ method initializes the name, position, and children of each node.
        2. The add_child method allows us to add subordinates (child nodes) to each employee (parent node).
        3. The print_tree method recursively prints the tree structure by displaying the employee's 
        position and name, and it indents each level to represent the hierarchy.

    Step 1: Creating the CEO:

        The ceo variable is an instance of the TreeNode class, representing the CEO. 
        The root node is always the top-most employee in the hierarchy.

    Step 2: Creating Other Top-Level Managers:

        We create instances for the CTO, CFO, and COO using the same TreeNode class. 
        These are direct reports to the CEO.

    Step 3: Adding Top-Level Managers as Children of the CEO:

        We use the add_child method to add the CTO, CFO, and COO as children of the CEO. 
        This creates the first level of hierarchy.

    Step 4: Adding Employees under the CTO:

        The CTO has two developers (Dev1 and Dev2) as subordinates, 
        so we add them as children of the CTO using the add_child method.

    Step 5: Adding Employees under the CFO:

        The CFO manages two accountants (Acc1 and Acc2). 
        We add these nodes under the CFO using the same method.

    Step 6: Adding Employees under the COO:

        The COO has two operations staff members (Ops1 and Ops2) as direct reports. 
        These are added as children of the COO node.

    Step 7: Printing the Company Hierarchy:

        Finally, we call the print_tree method on the CEO node, 
        which recursively prints the entire tree structure, 
        showing the hierarchy of employees from the CEO down 
        to each department's employees.


'''