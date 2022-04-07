
# Data Structure - Stacks
-Vending Machine Stack Problem

-Stacks are another data structure that are easy to learn and useful for controlling memory.

-Stacks opperate off of FIFO

>"In computing and in systems theory, FIFO an acronym for first in, first out (the first in is the first out) is a method for organizing the manipulation of a data structure (often, specifically a data buffer) where the oldest (first) entry, or "head" of the queue, is processed first."

Think of a stack of pancakes. If you want to get to the bottom pancake, you need to first remove the cakes on top.

Read more about FIFO [here](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)#:~:text=In%20computing%20and%20in%20systems,the%20queue%2C%20is%20processed%20first.)

Big O notation, and basic stack operations:
![slide_36.jpg](slide_36.jpg)

Example Code:
```Stack implementation in python
# Creating a stack
    stack = []

# Adding things into the stack
def push(stack, thing):
    stack.append(thing)
    stack.append(1)
    print("pushed item: " + item)
#result in stack = item,1

# Removing an element from the stack. This will check to see if the stack is empty and then pop off an item if so.
def pop(stack):
    if stack == 0:
        print("stack is empty")

    return stack.pop()
```
Problem: Manage the Vending Maching

-Here is the link to the code [Link](#vendingmachinestacks.py)

Here is the solution [Link](#vendingmachinestacks-solution.py)

Back to [main](MainSection.md)