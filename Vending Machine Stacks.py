#This program will...
#Questions to consider. 
#What is the big O performance of a stack?
#How might it be better than a list?

class Stack:
   def __init__(self):
      self.stack = []
      self.candycount = 0
   def add(self, candy):
      if self.candycount < 5:
         self.stack.append(candy)
      else:
         return False
      # for i in self.stack:
      #    if i == candy:
      self.candycount += 1

self = Stack()


#Test Cases
#These test cases should output 
for i in range(7):
   self.add("Snickers")
self.candycount = 0
for i in range(4):
   self.add("Recees")
self.candycount = 0
for i in range(2):
   self.add("Twix")
print(self.stack)

#Write the code so that the remaining 
# stack contains only 1 of each candy.