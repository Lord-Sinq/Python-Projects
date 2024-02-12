'''
Name: Sinclair DeYoung
Date: Jun 15, 2023
Description: Lab_14 is a continuation of Lab_13 with using sorting algorithm's
Lab_14 uses the merge and the quick sort algorithm's
'''
import random

def mergeSort(theList):
    '''
    sorts by using the merge sort algorithm
    '''
    # base case
    if len(theList) <= 1:
        return
    N = len(theList)
    midpoint = N // 2
    # copy's of the list
    leftHalf = theList[:midpoint]
    rightHalf = theList[midpoint:]
    # recursively sort the right and left half
    mergeSort(leftHalf)
    mergeSort(rightHalf)
    # index
    i = 0 # left half
    j = 0 # right half
    k = 0 # original list
    # while we haven't exhausted one of the list
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            theList[k] = leftHalf[i]
            i += 1
        else:
            theList[k] = rightHalf[j]
            j += 1
        k += 1
    # now we have exhausted one of the list, so copy the remaining
    # values into the original list.
    while i < len(leftHalf):
        theList[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        theList[k] = rightHalf[j]
        j += 1
        k += 1
def quickSort(theList):
    '''
    sorts the list using the quick sort algorithm
    '''
    if len(theList) <= 1:
        return theList
    point = random.choice(theList)
    less = [x for x in theList if x < point]
    equal = [x for x in theList if x == point]
    greater = [x for x in theList if x > point]
    return quickSort(less) + equal + quickSort(greater)
def main():
    '''
    main function used to test the merge and quick sort algorithm
    '''
    # random numbers for a list
    myList = [random.randint(1,100) for i in range(30)]
    # using the merge sort
    print('Unsorted list =', myList)
    mergeSort(myList)
    print('Merge sorted list =', myList)
    # using the quick sort
    QS = quickSort(myList)
    print('Quick sorted list =', QS)
# call the main function
if __name__ == '__main__':
    main()