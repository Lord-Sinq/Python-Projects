"""
Name: Sinclair DeYoung
Class: CSC-380
Date: Jan 22, 2024
Purpose: Taking the pseudocode Sieve Algorithm and implementing it in python
the big-O of this is O(nlog(logn))
"""
import math
import time


def main():

    valuesN = [100, 500, 1000, 10_000]

    for n in valuesN:
        # start time
        Start = time.perf_counter()
        # inital value and empty list
        n = n
        List = []
        # adds numbers from 2 to n-1 to the list
        for x in range(2, n):
            List.append(x)

        # sets the lowest prime to p
        p = 2

        # sieves algorith: loop until square root of p + 1 is greater then n
        while not int(math.sqrt(p)) + 1 > n:

            # it marks multiple of p in the list as 0
            for x in range(p * 2, n, p):
                List[x - 2] = 0

            # increment p
            p += 1
            # continues until it finds the next non-zero
            while p - 2 < len(List) and List[p - 2] == 0:
                p += 1

        # iterates through the list and prints the numbers that are not marked as 0
        for x in List:
            if x != 0:
                print(x)

        # show time
        Finish = time.perf_counter()
        diffTime = Finish - Start
        print(f"Time it took:{diffTime}")

if __name__ == "__main__":
    main()