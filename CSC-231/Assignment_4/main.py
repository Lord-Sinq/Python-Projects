'''
Name: Sinclair DeYoung
Date: Jun 15, 2023
Description: This is the final assignment for csc-231.
we will be using Hash tables to find student records
'''
from HashTable import HashTableProbing
from HashTable import HashTableChaining
from LinkedList import LinkedList
from Student import Student
import matplotlib.pyplot as plt
import time
def main():
    '''
    Main functionn used to open and test the files
    '''
    # part 1
    # prime numbers from assignment 4 instructions
    primeNumbers = (750019, 740011, 730003, 720007, 710009, 700001, 690037,
                    680003, 670001, 660001, 650011, 640007, 630017, 620003)
    # load the file data
    # take each line of the file and split it between the numbers
    # and student names.
    studentList = []
    filename = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_short.txt'
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            studentId, studentName = line.split('\t')
            studentId = int(studentId)
            student = Student(studentId, studentName)
            studentList.append(student)
    # hash table with chaining, with time used to measure how long it takes
    for tableSize in primeNumbers:
        print('Using chaining, table size =', tableSize)
        startTime = time.time()
        chainingTable = HashTableChaining(tableSize)
        for student in studentList:
            chainingTable.insert(student)
        insertTime = time.time() - startTime
        print('Time to insert', len(studentList), 'student records is', insertTime,'seconds')
        startTime = time.time()
        for student in studentList:
            result = chainingTable.find(student)
            # if student not found
            if result is None or result != student:
                print('Error: student', student, 'not found in the hash table.')
                break
        findTime = time.time() - startTime
        print('Time to insert', len(studentList), 'student record is',findTime,'seconds','\n')
    # hash table with probing, with time used to measure how long it takes
    for tableSize in primeNumbers:
        print('Using probing, table size =', tableSize)
        startTime = time.time()
        probingTable = HashTableProbing(tableSize)
        for student in studentList:
            probingTable.insert(student)
        insertTime = time.time() - startTime
        print('Time to insert', len(studentList), 'student records is', insertTime, 'seconds')
        startTime = time.time()
        for student in studentList:
            result = probingTable.find(student)
            if result is None or result != student:
                print('Error: student', student, 'not found in the hash table.')
                break
            findTime = time.time() - startTime
            print('Time to insert', len(studentList), 'student record is', findTime, 'seconds', '\n')
    # part 2
    chainingTimes = []
    probingTimes = []
    table_Sizes = []
    # hash table with chaining
    for tableSize in primeNumbers:
        table_Sizes.append(tableSize)
        startTime = time.time()
        chainingTable = HashTableChaining(tableSize)
        for student in studentList:
            chainingTable.insert(student)
        insertTime = time.time() - startTime
        chainingTimes.append(insertTime)
    # hash table with probing
    for tableSize in primeNumbers:
        startTime = time.time()
        probingTable = HashTableProbing(tableSize)
        for student in studentList:
            probingTable.insert(student)
        insertTime = time.time() - startTime
        probingTimes.append(insertTime)
    # scatter chart
    # takes a few seconds after you ru the program
    # after the last output from the console the scatter plot will show up
    plt.scatter(table_Sizes, chainingTimes, label='Chaining')
    plt.scatter(table_Sizes, probingTimes, label='Probing')
    plt.xlabel('Table Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison: Chaining vs. Probing')
    plt.legend()
    plt.show()
if __name__ == '__main__':
    main()