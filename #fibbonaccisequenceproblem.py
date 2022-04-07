#initialize the node class with 3 attributes.
# 2 to do left and the right node, and 1 to hold the position.
class Node:
    def __init__ (self,data):
        self.left = None
        self.right = None
        self.data = data
#This function will allow us to insert some data into the tree
# and put it into the correct place. We do this by comparing the data.        
    def insert_value(self, data):
# if the data we're passing in is less than the position on 
# the tree then we need to put it to the left. This function will 
#use recursion to help put everything into it's right place.
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
# Write a function called tree_print" to print the data within each branch of the tree 
# starting at the left side, and use recursion if possible.
#(PROBLEM)
    


# Use the insert method to add a root and nodes of your choosing.
root = Node(0)
root.insert_value(1)
root.insert_value(1)
root.insert_value(21)
root.insert_value(34)
root.insert_value(55)
root.insert_value(13)
root.insert_value(2)
root.insert_value(3)
root.insert_value(5)
root.insert_value(8)
root.tree_print()