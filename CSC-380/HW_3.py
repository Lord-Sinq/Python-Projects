'''
Name: Sinclair DeYoung
Date: Feb 13, 2024
Purpose: Homework 3 from CSC-380
'''
import time
import random

def selection_sort(thing):
    n = len(thing)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if thing[j] < thing[min_idx]:
                min_idx = i
    thing[i], thing[min_idx] = thing[min_idx], thing[i]

def bubble_sort(thing):
    n = len(thing)
    for i in range(n):
        for j in range(0, n-i-1):
            if thing[j] > thing[j+1]:
                thing[j], thing[j+1] = thing[j+1], thing[j]

def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

def measure_time_sorting(sort_function, array):
    start_time = time.perf_counter()
    sort_function(array)
    end_time = time.perf_counter()
    return end_time - start_time




def main():

    sizes = list(range(100, 3001, 100))
    selection_times = []
    bubble_times = []

    for size in sizes:
        array = generate_random_array(size)

        selection_time = measure_time_sorting(selection_sort, array.copy())
        bubble_time = measure_time_sorting(bubble_sort, array.copy())

        selection_times.append(selection_time)
        bubble_times.append(bubble_time)
    print(f" Size \t Selection_time \t Bubble_time ")
    for size, selection_time, bubble_time in zip(sizes, selection_times, bubble_times):
        print(f"{size}\t{selection_time: .6f}\t{bubble_time: .6f}")


if __name__ == "__main__":
    main()