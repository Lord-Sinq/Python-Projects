"""
Name: Sinclair DeYoung
Class: CSC-380
Date: Jan 11, 2024
Purpose: this is homework 1 code
    I originally was using map plot to plot everything but i switched to
    using excel.
    the Big-O of problem 1:O(log(min(m,n)))
    the Big-O of problem 2:O(log(min(m,n)))
    the Big-O of problem 3:O(min(m,n))
    the best one is problem 2 in my opinion
"""
import time

""" Problem 1 """
def gcd_book(m, n):
    t = min(m, n)
    while( t > 0):
        if(m % t == 0 and n % t ==0):
            return t
        else:
            t -= 1

def gcd(m , n):
    count = 1
    while n != 0:
        count += 1
        r = m % n
        m = n
        n = r
    return n

def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

def main():

    """ Univeral elements """
    m = int(input("Please enter a m value:"))
    n = int(input("Please enter a n value:"))
    data = list()
    count = 0

    print("N\tproblem_1\tproblem_2\tproblem_3")

    while count < 10:

        """ Part 1 of problem 1 """
        startClock = time.process_time()
        gcd(m,n)
        stopClock = time.process_time()
        diffClock = startClock - stopClock
        data.append(('GCD',diffClock))

        """ Part 2 of problem 1 """
        startClockx = time.process_time()
        if n == 0:
            print(f"start: {m}")
        else:
            gcd_recursive(m, n)
        stopClockx = time.process_time()
        diffClockx = startClockx - stopClockx
        data.append(('GCD recursively', diffClockx))

        """ Part 3 of problem 1"""
        #clock for part 3
        startClockxx = time.process_time()
        gcd_book(m, n)
        stopClockxx = time.process_time()
        diffClockxx = startClockxx - stopClockxx
        data.append(('GCD from the book', diffClockxx))

        """ Print the results """
        print(gcd_book(m,n),"\t",diffClock,"\t",diffClockx, "\t", diffClockxx)
        count += 1

if __name__ == "__main__":
    main()

