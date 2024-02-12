'''
Name: Sinclair DeYoung
Date: May 30, 2023
Description:Takes in 20 random numbers and puts them in a Stack.
From there it evaluates different protocols to produce varying results.
'''
import random

class Stack:
    def __init__(self):
        '''
        Constructor: makes a stack to hold elements
        '''
        self.__items = []
    def __len__(self):
        # returns number of items in the stack
        return len(self.__items)
    def push(self, item):
        # adds an item to the top of the stack
        self.__items.append(item)
    def pop(self):
        # remove and returns item at the top of the stack
        if self.isEmpty():
            return None
        return self.__items.pop()
    def peek(self):
        # shows element in front of queue without removing
        if self.isEmpty():
            return None
        return self.__items[-1]
    def isEmpty(self):
        # checks for an empty stack
        return len(self.__items) == 0

def main():
    '''
    Main: checks the Stack class and asks to show that the above classes
    parameter are working.
    '''
    # class
    S = Stack()
    # checks with empty stack
    print('Stack is empty =', S.isEmpty())
    print('length of the stack is',len(S))
    print('the item at the front is', S.peek())
    # ask for a range of numbers
    for i in range(20):
        x = random.randint(-100,100)
        print(x)
        S.push(x)
    # with new numbers check the class
    print('The stack is empty =', S.isEmpty())
    print('the size of the stack is', len(S))
    print('the item at the front is', S.peek())
    # slowly empty the stack and shows the results after
    while not S.isEmpty():
        print('Pop the value',S.pop())
    print('The stack is empty =', S.isEmpty())
    print('the size of the stack is', len(S))
    print('the item at the front is', S.peek())
# calls the main function
if __name__ == '__main__':
    main()