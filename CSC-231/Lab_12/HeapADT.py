'''
Name: Sinclair DeYoung
Date: Jun 13, 2023
Description: This lab implements the Heap ADT
'''
import random

class minHeap:
    '''
    this is the Min heap class
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.__size = 0
        self.__theHeap = [None]
    def __len__(self):
        '''
        Overloads the len Operator
        '''
        return self.__size
    def __getParent(self, i):
        '''
         Get the parent of the node
        '''
        return i // 2
    def __getLeftChild(self, i):
        '''
        Get the Left Child of the node
        '''
        return i * 2
    def __getRightChild(self, i):
        '''
        Get the Right Child of the node
        '''
        return i * 2 + 1
    def isEmpty(self):
        '''
        Checks the size to see if it is empty
        '''
        return self.__size == 0
    def insert(self, x):
        '''
        Insert function
        '''
        self.__size += 1
        self.__theHeap.append(x)
        self.__percolateUp(self.__size)
    def deleteMin(self):
        '''
        Delete min function removes the min value and returns it
        '''
        if self.__size < 1:
            return None
        value = self.__theHeap[1]
        # taking the last value and putting it in index 1
        self.__theHeap[1] = self.__theHeap[self.__size]
        # move the last value into the 1st position
        self.__size -= 1
        self.__theHeap.pop()
        # percolate the new value at 1
        self.__percolateDown(1)
        return value
    def __percolateUp(self, i):
        '''
        Percolate up starting at position i
        '''
        parent = self.__getParent(i)
        # if the parent if i is zero, then i is the root and we are done
        while (parent > 0):
            # swap if the parent value is bigger then the child
            if (self.__theHeap[parent] > self.__theHeap[i]):
                self.__swap(parent, i)
                i = parent
                parent = self.__getParent(i)
            else:
                # stops the loop
                parent = 0
    def __percolateDown(self, i):
        '''
        Percolate down starting at position i
        But needs to go left or right
        '''
        lChild = self.__getLeftChild(i)
        rChild = self.__getRightChild(i)
        # heaps are complete tree to no need to worry
        # about having a right and no left
        while (lChild <= self.__size):
            # checks for the bigger child
            min = lChild
            if (rChild <= self.__size and \
                self.__theHeap[rChild] < self.__theHeap[lChild]):
                min = rChild
            # Assertion: min is the smaller of the two children
            if (self.__theHeap[i] > self.__theHeap[min]):
                self.__swap(i, min)
                # this moves down the tree
                i = min
                lChild = self.__getLeftChild(i)
                rChild = self.__getRightChild(i)
            else:
                # once we down swap we are down
                lChild = self.__size + i

    def __swap(self, i, j):
        '''
        Swaps position i with j and position j with i
        '''
        self.__theHeap[i], self.__theHeap[j] = self.__theHeap[j], self.__theHeap[i]
    def __str__(self):
        '''
        String function
        '''
        return ', '.join(str(item) for item in self.__theHeap[1:])

def main():
    '''
    Main Function used to test the minHeap class
    '''
    heap = minHeap()
    # check the Heap with no values
    print("Is the heap empty?", heap.isEmpty())
    print("Length of the heap:", len(heap))
    print("Heap contents:", heap)
    # Add 20 random values to the heap
    for i in range(20):
        value = random.randint(1, 100)
        heap.insert(value)
    # test the heap with 20 random values
    print("Is the heap empty?", heap.isEmpty())
    print("Length of the heap:", len(heap))
    print("Heap contents:", heap)
    # Remove and print the minimum values until the heap is empty
    print("Removing and printing minimum values:")
    while not heap.isEmpty():
        print("Root Value = ", heap.deleteMin())
    # shows after all values have been removed
    print("Is the heap empty?", heap.isEmpty())
    print("Length of the heap:", len(heap))
    print("Heap contents:", heap)

if __name__ =='__main__':
    main()

