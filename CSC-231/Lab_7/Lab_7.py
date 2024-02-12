'''
Name: Sinclair DeYoung
Date: Jun 5, 2023
Description: This is Lab_7, where we will show examples of recursion and how to use recursion
to get answers to problems. We were given recSum1 and recSum2 but had to code
recMin and recPow
'''

def recSum1(someList):
    '''
    takes in someList and finds the center then takes the sum of both and
    adds them together
    '''
    if len(someList) == 1:
        return someList[0]
    else:
        a = recSum1(someList[:len(someList) // 2])
        b = recSum1(someList[len(someList) // 2:])
        return a + b
def recSum2(someList):
    '''
    takes in someList and returns the values all added together
    '''
    if len(someList) == 1:
        return someList[0]
    else:
        return someList[0] + recSum2(someList[1:])
def recMin(someList):
    '''
    Takes in someList and takes the sum of the first half and back half
    then takes the minimum of the two results
    '''
    if len(someList) == 1:
        return someList[0]
    else:
        a = recMin(someList[:len(someList) // 2])
        b = recMin(someList[len(someList) // 2:])
        if a < b:
            return a
        else:
            return b
def recPow(x, n):
    '''
    takes in two paramiters x , n. n being what power x is raised to.
    then returns the results of the recursive power function
    '''
    if n == 0:
        return 1
    else:
        result = recPow(x, n //2)
        result *= result
        if n % 2 == 1:
            result *= x
        return result
import random

def main():
    '''
    main function was provided for the recSum1 and recSum2
    then was modifided to show the results of the Minimum and power recursive function
    '''
    N = 100
    myList = [random.randint(-500, 500) for i in range(N)]
    x = 3
    n = 5
    result = recPow (x, n)
    print(myList)
    print("The sum of the numbers is: " + str(sum(myList)))
    print("The sum of the numbers using recSum1 is: " + str(recSum1(myList)))
    print("The sum of the numbers using recSum2 is: " + str(recSum2(myList)))
    print('The Min of the numbers using recMin is:' + str(recMin(myList)))
    print('The Power function recMin results are:' + str(result))
if __name__ == "__main__":
    main()