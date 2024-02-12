'''
Name: Sinclair DeYoung
Date: May 30, 2023
Description: Takes in 20 random numbers and puts them in a Queue.
From there it evaluates different protocols to produce varying results.
'''
import random

class Queue:
    def __init__(self):
        '''
        Constructor: makes a Queue to hold elements
        '''
        self.__items = []
    def enqueue(self, item):
        # adds elements to the back
        self.__items.insert(0, item)
    def dequeue(self):
        # removes the element and returns to the front of the queue
        if (self.isEmpty()):
            return None
        else:
            return self.__items.pop()
    def peek(self):
        # shows element in front of queue without removing
        if (self.isEmpty()):
            return None
        else:
            return self.__items[-1]
    def __len__(self):
        # returns number of items in the queue
        return len(self.__items)
    def isEmpty(self):
        # checks for an empty queue
        return len(self.__items) == 0

def main():
    '''
    Main: checks the Queue class and asks to show that the above classes
    parameter are working.
    '''
    # class
    Q = Queue()
    # checks with empty queue
    print('queue is empty =', Q.isEmpty())
    print('length of the queue is',len(Q))
    print('the item at the front is', Q.peek())
    # ask for a range of numbers
    for i in range(20):
        x = random.randint(-100,100)
        print(x)
        Q.enqueue(x)
    # with new numbers check the class
    print('The queue is empty =', Q.isEmpty())
    print('the size of the queue is', len(Q))
    print('the item at the front is', Q.peek())
    # slowly empty the queue and shows the results after
    while not Q.isEmpty():
        print('dequeue the value',Q.dequeue())
    print('The queue is empty =', Q.isEmpty())
    print('the size of the queue is', len(Q))
    print('the item at the front is', Q.peek())
# calls the main function
if __name__ == '__main__':
    main()