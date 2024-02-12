import numpy as np
import time
'''
Name: Sinclair DeYoung
Purpose: Homework 2
exercise 2.3 problem 4
exercise 2.3 problem 6
exercise 2.4 problem 4
exercise 2.4 problem 9
'''

'''
problem 1
a)The algorithm computes the sum of the squares of integers from 1 to n
b)Basic operation in this algorithm is the multiplication i * i
c)The basic operation is executed nn times
d)The time complexity of this algorithm is O(n)
e)You could make the multiplication and exponent
'''
def Mystery(n):
    '''
    return: the values of n and s
    '''
    s = 0
    for i in range(1,n):
        s = s + i * i
    return n, s
'''
problem 2
a)The algorithm checks whether a given matrix A is symmetric
b)The basic operation is the comparison of matrix elements: A[i, j] != A[j, i]
c)The basic operation is executed (n*(n-1))/2 times
d)The time complexity of this algorithm is O(n^2)
e)I do not think I could make it better
'''
def Enigma(A):
    '''
    return: boolean answer to if the matrixes match
    '''
    n = len(A)
    for i in range(0, n-1):
        for j in range(i+1,n):
            if A[i][j] != A[j][i]:
                return False
    return True
'''
problem 3
a)The algorithm computes the sum of the first n odd numbers
b)The algorithm performs one multiplication each recursive call so n
c)The algorithm performs one addition in each recursive call n
'''
def Q(n):
    '''
    return: 1 if equal to 1 or calls it returns recursive function
    '''
    if n == 1:
        return 1
    else:
        return Q(n-1)+2 * n-1
'''
Problem 4
a)computes the minimum value in an array
b)uses recursion to repeatedly find the minimum value of the subarray
 until it reaches the base case where the array has only one element
'''
def Riddle(A):
    n = len(A)
    if n == 1:
        return A[0]
    else:
        temp = Riddle(A[:-1])
        if A[n-1] <= temp:
            return A[n-1]
        else:
            return temp

def main():
    '''
    calls the functions in section 2.3 & 2.4
    Holds a matrix for problem 2, 4,and asks user input a positive number
    '''
    stop = False
    while stop != True:
        valuesN = [10,20,30,50,100,200]
        print("Problem1 time:\tProblem1:\tProblem2 time:\tProblem2:\tProblem3 time:\tProblem3:\tProblem4 time:\tProblem 4:")
        for userInput in valuesN:
            #i = np.arange(0, userInput)
            #j = np.arange(0, userInput)
            A = np.random.randint(0,10,size=(userInput,userInput))
            A = (A +A.T)/2      #Makes the matrix symmetric
            B = np.random.randint(0,100,userInput)
            if userInput < 0:
                print("Sorry: must be a non-negative integer")
            else:
                start1 = time.perf_counter()
                problem1 = Mystery(userInput)
                end1 = time.perf_counter()
                start2 = time.perf_counter()
                problem2 = Enigma(A)
                end2 = time.perf_counter()
                start3 = time.perf_counter()
                problem3 = Q(userInput)
                end3 = time.perf_counter()
                start4 = time.perf_counter()
                problem4 = Riddle(B)
                end4 = time.perf_counter()
                time1= end1 - start1
                time2 = end2 - start2
                time3 = end3 - start3
                time4 = end4 - start4
                print(f"{time1}\t{problem1}\t{time2}\t{problem2}\t{time3}\t{problem3}\t{time4}\t{problem4}")
        stop = True


if __name__ == "__main__":
    main()