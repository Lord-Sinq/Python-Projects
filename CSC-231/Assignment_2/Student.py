'''
Assignment 1
Name: Sinclair DeYoung
Date: May 26, 2023
Description: This is a student file that take student ID's and student names
and a way to look up students
'''
 # class function
class Student:
    # __intit__ assigns each value received and gives them a self. value
    def __init__(self,ID=None,name=''):
        self.__ID = ID
        self.__name = name
# getters
    def getID(self):
        return self.__ID
    def getName(self):
        return self.__name
# setters
    def setID(self, ID):
        self.__ID = ID
    def setName(self,name):
        self.__name = name
# how the string will produce
    def __str__(self):
        return str(self.__ID) + " (" + self.__name + ")"
# compairs each ID number
    def __cmp__(self, other):
        if (self.__ID > other.__ID):
            return 1
        elif (self.__ID < other.__ID):
            return -1
        else:
            return 0
# checks each number for the following conditions
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    def __ne__(self, other):
        return self.__cmp__(other) != 0
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    def __le__(self, other):
        return self.__cmp__(other) <= 0
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    def __ge__(self, other):
        return self.__cmp__(other) >= 0
# find functions used to pair the numbers
def find(ID,Target_ID):
    for num in ID:
        if num == Target_ID:
            return num
    return None
# Binary search
# i couldn't figure it out
# main fucntion
def main():
    '''
    Creates a new empty list and ask for a file then iterate over each line
    splitting the ID numbers of each student then assign each number to
    a character, the following "with statement" implements a way to check the
    ID from the ID only file and matches them up with the correct name from the
    other file.
    '''
    students = []
    with open('/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_2/listOfNames_short.txt','r') as file:
        for line in file:
            line = line.strip()
            ID, name = line.split('\t')
            ID = int(ID)
            student = Student(ID,name)
            students.append(student)
    # close the file and sort the new list
    file.close()
    students.sort()

    with open('/Users/sinq/PycharmProjects/pythonProject/CSC-231/Assignment_2/searchIds_short.txt','r') as file:
            for line in file:
                line = line.strip()
                ID = int(line)
                target_student = Student(ID)
                found_student = find(students, target_student)
                if found_student is not None:
                    print(found_student)
                else:
                    None
    file.close()
# calls the main fucntion
if __name__ == "__main__":
    main()