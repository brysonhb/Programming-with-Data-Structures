class Node:
#initialize the node class with 3 attributes.
# 2 to do left and the right node, and 1 to hold the position.
    def __init__ (self,data):
        self.left = None
        self.right = None
        self.data = data
#This function will allow us to insert some data into the tree
# and put it into the correct place. We do this by comparing the data.        
    def insert_value(self, data):
# if the data we're passing in is less than the position on 
# the tree then we need to put it to the left.
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert_value(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert_value(data)
# Print the data within each branch of the tree starting at the left side
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add a root and nodes of your choosing.
root = Node(1)
root.insert_value('james')
root.insert_value(14)
root.insert_value(3)
root.PrintTree()