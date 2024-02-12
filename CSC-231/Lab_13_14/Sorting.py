'''
Name: Sinclair DeYoung
Date: Jun 14, 2023
Description: Lab 13 will be using sorting.
specifically bubble, selection, and insertion sorting.
'''
import random

def swap(theList, i, j):
    '''
    Swaps the values in the list at position i and j
    '''
    a = theList[i]
    theList[i] = theList[j]
    theList[j] = a
def bubbleSort(theList):
    '''
    Sorts by using Bubble sort algorithm
    '''
    N = len(theList)
    i = N-1
    stopEarly = False

    while i > 0 and not stopEarly:
        stopEarly = True

        for j in range(0, i):
            if theList[j]> theList[j+1]:
                swap(theList, j, j+1)
                stopEarly = False
        i -= 1
def insertionSort(theList):
    '''
    Sorts by using the Insertion sorting algorithm
    '''
    N = len(theList)

    for i in range(1, N):
        holdValue = theList[i]
        j = i
        while j > 0 and theList[j-1] > holdValue:
            theList[j] = theList[j-1]
            j -= 1
        theList[j] = holdValue
def selectionSort(theList):
    '''
    Sorts by using the Selection sort algorithm
    '''
    N = len(theList)
    for i in range(N-1):
        smallestPosition = i
        for j in range(i +1, N):
            if theList[smallestPosition] > theList[j]:
                smallestPosition = j
        swap(theList, i, smallestPosition)
        
def main():
    '''
    Main function used to test the sorting algorithms
    '''
    for _ in range(3):
        # random numbers for the list
        myList = [random.randint(1,100) for i in range(30)]
        # testing will unsorted list and python built in sorter
        print('The sorted list =' + str(sorted(myList)))
        print('Unsorted list =' + str(myList) + '\n')
        # testing bubble sort
        bubblelist = myList.copy()
        bubbleSort(bubblelist)
        print('After Bubble sorting =' + str(myList))
        # testing insertion sort
        insertionlist = myList.copy()
        insertionSort(insertionlist)
        print('After Insertion Sorting =' + str(myList))
        # testing selection sort
        selectionlist = myList.copy()
        selectionSort(selectionlist)
        print('After Selection sorting ='+ str(myList))
        print('\n')
if __name__ == '__main__':
    main()
