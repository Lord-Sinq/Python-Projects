'''
Assignment 1
Name: Sinclair DeYoung
Date: May 26, 2023
Description: This is a student file that take student ID's and student names
and a way to look up students
'''
class Student:
    def __init__(self, student_id=None, student_name=''):
        self.student_id = student_id
        self.student_name = student_name

    def getID(self):
        return self.student_id

    def getName(self):
        return self.student_name

    def setID(self, student_id):
        self.student_id = student_id

    def setName(self, student_name):
        self.student_name = student_name

    def __str__(self):
        return f"{self.student_id} ({self.student_name})"

    def __cmp__(self, other):
        if self.student_id < other.student_id:
            return -1
        elif self.student_id > other.student_id:
            return 1
        else:
            return 0

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
def find(student_list, target_student):
    for student in student_list:
        if student == target_student:
            return student
    return None
def main():
    # Reading student information from the first file
    students = []
    with open('student_names.txt', 'r') as file:
        for line in file:
            line = line.strip()
            student_id, student_name = line.split('\t')
            student_id = int(student_id)
            student = Student(student_id, student_name)
            students.append(student)
    # Closing the first file
    file.close()
    # Sorting the list of students
    students.sort()
    # Searching for students in the second file
    with open('search_file.txt', 'r') as file:
        for line in file:
            line = line.strip()
            student_id = int(line)
            target_student = Student(student_id)
            found_student = find(students, target_student)
            if found_student is not None:
                print(found_student)
            else:
                print("Student not found.")
    # Closing the second file
    file.close()
if __name__ == '__main__':
    main()
