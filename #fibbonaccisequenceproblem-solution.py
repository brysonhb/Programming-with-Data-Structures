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
# Print the data within each branch of the tree starting at the left side
    def tree_print(self):           
        if self.left != None:       #if there is something in the left branch
            self.left.tree_print()  #set the pointer to the left branch recursively
        else:
            print(self.data)        #print whatever is in the current node
        if self.right != None:      #If there is something in the right branch
            self.right.tree_print() #Set the pointer to the right side
            

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