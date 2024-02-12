"""
Name: Sinclair DeYoung
Date: Jun 2, 2023
Description: This program reads student information from a file, creates a linked list of Student objects,
and searches for a specific student record using the student ID. It also measures the time
taken for insertion and search operations.
"""
from LinkedList_ import LinkedList
from Student import Student
import time

def main():
    # File names
    student_file = "listOfNames_short.txt"
    search_file = "searchIds_short.txt"
    # Read student information from file and create a linked list of Student objects
    student_list = read_student_file(student_file)
    # Search for students in the list
    search_student(search_file, student_list)

def read_student_file(filename):
    """
    Read the student information from a file and create a linked list of Student objects.
    Parameters: (filename) is the place holder for the file's
    Returns: student_list
    """
    student_list = LinkedList()
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            student_id, student_name = line.split("\t")
            student_id = int(student_id)
            student = Student(student_id, student_name)
            student_list.add(student)
    return student_list

def search_student(filename, student_list):
    """
    Read each line from a file and search for a matching student record in the list of Student objects.
    Parameters:
    - filename: The name of the file containing student IDs to search.
    - student_list: A linked list of Student objects.
    Prints the matching student record or an appropriate message if no match is found.
    """
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            student_id = int(line)
            found_student = student_list.search_student(student_id)
            if found_student is not None:
                print('Found Student Record:',found_student)
            else:
                print("No matching student found for ID:", student_id)
if __name__ == "__main__":
    startTime = time.time()
    main()
    endTime = time.time()
    print("Time to execute the program:", format(endTime - startTime, "6.4f"), "seconds.")