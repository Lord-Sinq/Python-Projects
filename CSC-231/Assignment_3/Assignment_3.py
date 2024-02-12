'''
Name: Sinclair DeYoung
Date: Jun 9, 2023
Description: This assignment uses the other two assignments to search for student records
and adding to the past assignments. this file also makes a binary tree out of
the values provided.
'''
from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree
from AVL import AVLTree
from Student import Student
import time
def main():
    '''
    This main is how we grab and set the files to variables to use
    in this file.
    '''
    studentFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_long.txt'
    searchFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/searchIds_long.txt'
    # Part 1
    # Binary Search Tree for inserting student records
    bst = BinarySearchTree()
    studentList = readStudentFile(studentFile)
    for student in studentList:
        bst.insert(student)
    searchStudent(searchFile, bst)
    # AVL Tree for inserting student records
    avl = AVLTree()
    studentList = readStudentFile(studentFile)
    for student in studentList:
        avl.insert(student)
    searchStudent(searchFile, avl)
    # Part 2
    # short
    studentFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_short.txt'
    searchFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/searchIds_short.txt'
    measureTime(studentFile, searchFile)
    # med
    studentFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_med.txt'
    searchFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/searchIds_med.txt'
    measureTime(studentFile, searchFile)
    # long
    studentFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_long.txt'
    searchFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/searchIds_long.txt'
    measureTime(studentFile, searchFile)
    # Short short
    studentFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_short_sorted.txt'
    searchFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/searchIds_short.txt'
    measureTime(studentFile, searchFile)
    # Med Sort
    studentFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_med_sorted.txt'
    searchFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/searchIds_med.txt'
    measureTime(studentFile, searchFile)
    # Long Sort
    studentFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/listOfNames_long_sorted.txt'
    searchFile = '/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_3/searchIds_long.txt'
    measureTime(studentFile, searchFile)
def readStudentFile(filename):
    '''
    This function reads the student file
    '''
    studentList = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            studentId, studentName = line.split('\t')
            studentId = int(studentId)
            student = Student(studentId, studentName)
            studentList.append(student)
    return studentList
def searchStudent(filename, studentTree):
    '''
    This function searches inRead each line from a file and search for a matching student record in the list of Student objects.
    Prints the matching student record or an appropriate message if no match is found. a file
    '''
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            studentId = int(line)
            foundStudent = studentTree.find(studentId)
            if foundStudent is not None:
                print('Found Student Record:', foundStudent)
            else:
                print('No Matching student found for ID:', studentId)
def measureTime(studentFile, searchFile):
    '''
    This is the measuring function that times the fines adn there
    length it takes them to find and insert into a AVL Tree
    '''
    studentList = readStudentFile(studentFile)
    startTime = time.time()
    avltree = AVLTree()
    for student in studentList:
        avltree.insert(student)
    insertionTime = time.time() - startTime
    startTime = time.time()
    with open(searchFile, 'r') as file:
        for line in file:
            line = line.strip()
            studentId = int(line)
            avltree.find(studentId)
    searchTime = time.time() - startTime
    print('Time to insert' ,len(studentList), 'records into the AVL Tree:', format(insertionTime,'.6f'),'seconds')
    print('Time to find', len(studentList),' records from the AVL Tree:', format(searchTime,'.6f'),' seconds')

if __name__ == '__main__':
    main()