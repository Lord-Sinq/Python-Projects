#==========================================================================
## I CERTIFY THAT THE CODE SHOWN BELOW IS MY OWN WORK
## AND THAT I HAVE NOT VIOLATED THE UNCW ACADEMIC HONOR CODE
## WHILE WRITING THIS CODE
## you may use your editor, help from the shell, use your textbooks, 
## your previous codes, and the lecture notes as reference
## no other resources can be used during the test.
## no additional import statements please
## If the function is not complete as instructed, you get
## AT BEST 50% of the grade for that question.

# PROGRAM PURPOSE:... Practice 1 
# AUTHOR:............ Last, First
# COURSE:............ CSC 131-YOUR SECTION NUMBER
# TERM:.............. Fall 2020
# COLLABORATION:..... None
#==========================================================================

from testing_practice1 import test,test_file_content,test_LOM,testNoPrint
import sys
import random


#=============================================================================
# q1 - create function quarter() to meet the conditions below
#    - accept one parameter:  a string (month name)
#    - determine the quarter of the year given the month name
#    - return the quarter # (1, 2, 3, or 4)
#    - you can assume that the input parameter is a valid, full name of a month
#
#    --- e.g. for March -> returns 1
#    --- e.g. for June -> returns 2
#    --- e.g. for October -> returns 4
#
#    The quarters are:
#    --- quarter 1: January - March
#    --- quarter 2: April - June
#    --- quarter 3: July - September
#    --- quarter 4: October - December
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS:  You may not use index().
#    - HINT: Use nested if-then-else.
#
#    - param:   string
#    - return:  integer
#=============================================================================
def quarter(month):
    if month == "January" or month == "February" or month == "March":
        return 1
    elif month == "April" or month == "May" or month == "June":
        return 2
    elif month == "July" or month == "August" or month == "September":
        return 3
    elif month == "October" or month == "November" or month == "December":
        return 4
month = str('Please Enter a month')
quarter(month)
    
#=============================================================================
# q2 - create function addem() to meet the conditions below
#    - accept two parameters:  two integer values
#    - calculate the sum of the values from x through y (including both x and y)
#    - return the sum 
#
#    --- e.g. x = 2 and y = 5 -> returns 14 (2+3+4+5)
#    --- e.g. x = 5 and y = 2 -> returns 14 (2+3+4+5) , (5+4+3+2)
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS:  you are not allowed to use sum() function
#    - HINT: Use a for loop
#
#    - params:  integer
#               integer
#    - return:  integer
#=============================================================================
def addem(x,y):
    numm = 0
    for n in range(x,y+1):
        numm+= n
    return numm
#==========================================================================
# q3 - create function longestLength() to meet the conditions below
#    - accept two parameters: two strings
#    - return the length of the longest string
#
#    --- e.g. "Hello" and "Good-bye"; function returns 8
#    --- e.g. "Hello" and "Apple"; function returns 5
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS: you are not allowed to use len() function.
#    - HINT: Iterate over the strings and count them.
#
#    - params:  string
#               string
#    - return:  integer
#==========================================================================
def longestLength(first,second):
    final = 0
    counter_1 = 0
    counter_2 = 0
    for i in first:
        counter_1+=1
    for o in second:
        counter_2 += 1
    if counter_1 >= counter_2:
        final = counter_1
    else:
        final = counter_2
    return final
    
    
#==========================================================================
# q4 - create function numTriangle() to meet the conditions below
#    - accept one parameter: a single digit integer
#    - creates a number triangle with x rows.
#    - each row consists of the row number (n) printed n times.
#    - you can assume the parameter is a value between 2 and 9 (both inclusive).
#
#    --- e.g. 3 is passed to the function
#       displays:
#       1
#       22
#       333
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS: None
#    - HINT: This requires nested loops
#
#    - param:   integer
#    - return:  None
#==========================================================================
def numTriangle(n):
    for i in range(n+1):
        for j in range(i):
            print(i, end=" ")
        print("\n")
#==========================================================================
# q5 - create function combineWords() to meet the conditions below
#    - accept two parameters: two lists named firstnames and lastnames
#    - returns a new list representing all possible combinations of EACH
#    - firstname string and EACH lastname string with a space between
#
#    --- e.g. first: ["sara", "alex"] and last: ["smith", "murphy"]
#       returns the final list:
#       ["sara smith", "sara murphy", "alex smith", "alex murphy"]
#       
#
#    - DOCUMENTATION: add a meaningful docstring
#    - HINT: This requires nested loops as well as string concantenation
#
#    - RESTRICTIONS: None
#
#    - params:  list
#               list
#    - return:  list
#==========================================================================
def combineWords(firstnames, lastnames):
    comb = []  # list to store the combinations
    for firstname in firstnames:
        for lastname in lastnames:
            c = firstname + ' ' + lastname  # combine firstname and lastname with a space
            comb.append(c)  # add the combination to the list
    return comb
#==========================================================================
# q6 - create function secondIndex() to meet the conditions below
#    - accept two parameters: a list of integers and an integer
#    - find the index of the SECOND occurrence of the number (2nd parameter) in the list (1st parameter).
#    - return: Index of second occurrence of the integer in the list.
#    - -1 if the number does not occur two or more times in the list.
#
#    --- e.g. 1: secondIndex([2,34,3,45,34,45,3,3], 3) returns 6
#    --- e.g. 2: secondIndex([2,34,3,45,34,45,3,3], 45) returns 5
#    --- e.g. 3: secondIndex([2,34,3,45,134,45,3,3], 134) returns -1
#    --- e.g. 4: secondIndex([2,34,3,45,134,45,3,3], 100) returns -1
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS: None
#    - HINT: This requires a loop, but you will also need a boolean
#            variable to know when you have seen the first occurence
#            of the value.
#
#    - params:  list
#               integer
#    - return:  integer
#==========================================================================
def secondIndex(lst, num):
    count = 0  # variable
    index = -1  # variable to hold the index
    for i, n in enumerate(lst):
        if n == num:
            count += 1
            if count == 2:  # check if this is the second occurrence
                index = i
                break
    return index
#==========================================================================
# q7 - create function lineLengths() to meet the conditions below
#    - accept one parameter: a string (filename)
#    - open the file and read each line
#    - count the characters in each line
#    - don't forget to close the file
#    - return the length of the longest line in the file
#    - it's not required for you to handle the line breaks at the end.
#    - test files (sample1.txt, sample2.txt) will be created by the testing code.
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS: None
#    - HINT: You will need to read each line of the file and count the
#            number of characters similar to question 3.
#
#    - param:   string
#    - return:  integer
#==========================================================================
def lineLengths(filename):
    max_length = 0  # variable to store the length
    try: # using a try statement
        with open(filename, 'r') as file:
            for line in file:
                line_length = len(line.rstrip('\n'))  # count the characters in each line
                max_length = max(max_length, line_length)  # update max_length if needed
    except FileNotFoundError: # error for if file not found
        print(f"Error: File '{filename}' not found.")
        return None
    return max_length
#==========================================================================
# q8 - create function writeRandomNumbers() to meet the conditions below
#    - accept one parameter: a string (filename) 
#    - write ten random integers (of your choice) between 0 and 100 into the textfile
#      ---NOTE:  if done correctly, the output textfile is placed in the same
#                directory as this exam file
#    - don't forget to add the newline (line break) character to each line
#    - don't forget to close the file
#    - the testing code will create two files by itself for two test cases.
#    - return None 
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS:  You should use a loop to write the ten values.
#
#    - param:   string
#    - return:  None
#
#==========================================================================
import random
def writeRandomNumbers(filename):
    try: # used try statement to check for working file
        with open(filename, 'w') as file:
            for _ in range(10):
                random_number = random.randint(0, 100)  # generate a random integer between 0 and 100
                file.write(str(random_number) + '\n')  # write the random number to the file with a line break
    except IOError: # added an error just incase the file failed
        print(f"Error: Failed to write to file '{filename}'.")
    return None
#==========================================================================
# q9 - create function sumNum() to meet the conditions below
#    - accept one parameter: an n-character string
#    - find all the string numbers in the string, convert them to integer
#      and add them together
#    - you may assume all numbers are single digit
#    - return the integer result
#
#    --- e.g. "2KL5", returns 7
#    --- e.g. "Z3r5Q1h2g5Q", returns 16
#    --- e.g. "5A1E3yfE0", returns 9
#
#    - DOCUMENTATION: add a meaningful docstring
#
#    - RESTRICTIONS:  None
#    - HINT: Iterate over the string.  You may use the isdigit() function.
#
#    - param:   string
#    - return:  integer
#==========================================================================
def sumNum(string):
    total_sum = 0  # variable to hold the value of the tring
    for char in string:
        if char.isdigit():  # check if the character is a digit
            total_sum += int(char)  # convert the character to an integer and add it to the total sum
    return total_sum
#==========================================================================
# q10 - DEBUG function numElements(myList)
#    - This function currently returns INCORRECT answers
#    - Find and fix the error(s) in the function below
#
#    - accept one parameter: sentence - a string  
#
#    - numElements should iterate over the list and count how many elments
#      are in the list.
#    - return the number of elements
#
#    ---e.g. [82, -37, 1, 60, "hello"] returns 5
#
#    - RESTRICTIONS: do NOT re-write the function, just find/fix error(s)
#
#    - param:  list
#    - return: integer
#
#==========================================================================
def numElements(myList):
    ''' counts the number of elements in the list '''
    count = 0
    for ch in myList:
        count += 1
    return count
#==========================================================================
# *************************************************************************
# ******************* DO NOT EDIT CODE BELOW THIS POINT *******************
# *************************************************************************
#==========================================================================
def printErr():
    print(" ",sys.exc_info()[0].__name__,"-line",sys.exc_info()[-1].tb_lineno)
    print(" ",sys.exc_info()[1])
    
#==========================================================================   
def test_quarter():
    results = []
    print("\n\t\t**** (10 points) - quarter() ****")
    monthList = [(1,'January'), (1,'February'), (1,'March'), (2,'April'),
                 (2,'May'), (2,'June'), (3,'July'), (3,'August'),
                 (3,'September'), (4,'October'), (4,'November'), (4,'December')]

    passed = 0
    attempted = 0

    for i in range(3):
        attempted += 1
        idx = random.randint(0,11)
        if test(monthList[idx][0], quarter, monthList[idx][1]):
            passed += 1

    return passed, attempted

#==========================================================================
def test_addem():
    results = []
    print("\n\t\t**** (10 points) - addem() ****")
    passed = 0
    attempted = 0
    for i in range(3):        
        a = random.randint(0,6)
        b = random.randint(7,15)
        total = sum(list(range(a,b+1)))
        attempted += 1
        if test(total, addem, a, b):            
            passed += 1
    return passed, attempted
            
#==========================================================================
def test_longestLength():
    import string
    print("\n\t\t**** (10 points) - longestLength() ****")
    lst1 = (('Tom','Alex', 4), ('sara', 'derek', 5),
            ('orange', 'apple', 6))
    lst2 = (('banana', 'cherry', 6), ('book', 'fork', 4),
            ('sam', 'ava', 3))

    passed = 0
    attempted = 0
    for i in range(2):        
        a = random.randint(0,2)
        attempted += 1
        if test(lst1[a][2], longestLength, lst1[a][0], lst1[a][1]):            
            passed += 1
        attempted += 1
        if test(lst2[a][2], longestLength, lst2[a][0], lst2[a][1]):            
            passed += 1
    return passed, attempted    

#==========================================================================
def test_numTriangle():
    results = []
    print("\n\t\t**** (10 points) - numTriangle() ****")
    
    passed = 0
    attempted = 0
    row = random.randint(2,9)
    numTriangle(row)
    row = random.randint(2,9)
    numTriangle(row)
    return passed, attempted    

#==========================================================================
def test_combineWords():
    print("\n\t\t**** (10 points) - combineWords() ****")    
    passed = 0
    attempted = 0
    
    first = ['sara', 'peter', 'alex', 'tom']
    last = ['smith', 'brown', 'jones']
    names = ['alex brown', 'alex jones', 'alex smith', 'peter brown',
             'peter jones', 'peter smith', 'sara brown', 'sara jones',
             'sara smith', 'tom brown', 'tom jones', 'tom smith']
    attempted += 1
    if test(names, combineWords, first, last):
        passed += 1

        
    first = ['rick', 'peter']
    last = ['williams', 'davis', 'wilson']
    names = ['peter davis', 'peter williams', 'peter wilson',
             'rick davis', 'rick williams', 'rick wilson']
    attempted += 1
    if test(names, combineWords, first, last):
        passed += 1

    return passed, attempted

#==========================================================================
def test_secondIndex():
    results = []
    print("\n\t\t**** (10 points) - secondIndex() ****")    
    passed = 0
    attempted = 0
    
    nums = [20,2,5,4,54,24,24,25,2,5,10,10,2]
    values = [(20,-1), (2,8), (5,9), (25,-1), (100,-1)]
    random.shuffle(values)

    for i in range(4):
        attempted += 1
        if test(values[i][1], secondIndex, nums, values[i][0]):            
            passed += 1
    
    return passed, attempted    
        
#==========================================================================
def test_lineLengths():
    results = []
    print("\n\t\t**** (10 points) - lineLengths() ****")
    lst1 = ('pretty', 'sick', 'warm', 'nice', 'tired', 'book',
           'pillow', 'bedroom', 'car', 'sky', 'wonderful')
    maxLen1 = 9
    output_file = open("sample1.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst1)):
        output_file.write(lst1[i]+"\n")
    output_file.close()
    
    lst2 = ('hall', 'gallery', 'factory', 'depot', 'barn', 'airport',
           'garage', 'gym', 'hotel', 'cabin', 'mall', 'kiosk')
    maxLen2 = 7
    output_file = open("sample2.txt",'w')
    ms = ""
    ml = []
    for i in range(len(lst2)):
        output_file.write(lst2[i]+"\n")
    output_file.close()    

    passed = 0
    attempted = 0

    attempted += 1
    if test(maxLen1,lineLengths,"sample1.txt") or test(maxLen1+1,lineLengths,"sample1.txt"):            
        passed += 1
    attempted += 1
    if test(maxLen2,lineLengths,"sample2.txt") or test(maxLen2+1,lineLengths,"sample2.txt"):            
        passed += 1

    return passed, attempted  

#==========================================================================
def test_writeRandomNumbers():
    results = []
    print("\n\t\t**** (10 points) - writeRandomNumbers() ****")
    
    passed = 0
    attempted = 0

    writeRandomNumbers("sample_output1.txt")
    inputFile = open("sample_output1.txt", 'r')
    count = 0
    attempted += 1
    passed += 1
    for i in inputFile:
        count += 1
        if int(i.strip()) < 0 or int(i.strip()) > 100:
            passed = 0
    if count != 10:
        passed = 0

    writeRandomNumbers("sample_output2.txt")
    inputFile = open("sample_output2.txt", 'r')
    count = 0
    attempted += 1
    passed += 1
    for i in inputFile:
        count += 1
        if int(i.strip()) < 0 or int(i.strip()) > 100:
            passed = 0
    if count != 10:
        passed = 0


    return passed, attempted

#==========================================================================
def test_sumNum():
    results = []
    print("\n\t\t**** (5 points) - sumNum() ****")
    passed = 0
    attempted = 0
    lst = [("2KL5",7), ("Z5Q1h2Q",8), ("0r5A1E3yfE2",11)]

    for i in range(len(lst)):
        attempted += 1
        if test(lst[i][1],sumNum,lst[i][0]):            
            passed += 1

    return passed, attempted
        
#==========================================================================   

def test_numElements():
    results = []
    print("\n\t\t**** (5 points) - numElements() ****")
    passed = 0
    attempted = 0
    lst = [([82, -37, "hello", 38.23],4), (["table", 0],2),
           (['a', 'e', 'i', 'o', 'u'],5),
           ([0],1), ([],0), ([1, 2, 3],3),
           ([1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 200, 300],12)]
    for i in range(len(lst)):
        attempted += 1
        if test(lst[i][1],numElements,lst[i][0]):            
            passed += 1

    return passed, attempted    
        
# Main =======================================================================
def main():

    testFunctionList = [test_quarter, test_addem,
                        test_longestLength, test_numTriangle,
                        test_combineWords, test_secondIndex,
                        test_lineLengths, test_writeRandomNumbers,
                        test_sumNum, test_numElements]
    
    functionNames = ["quarter", "addem", 
                     "longestLength", "numTriangle",
                     "combineWords", "secondIndex",
                     "lineLengths", "writeRandomNumbers",
                     "sumNum", "numElements"]

    points = [-1 for i in range(len(testFunctionList))]
    totals = [0 for i in range(len(testFunctionList))]

    for i in range(len(testFunctionList)):
        try:
            points[i], totals[i] = testFunctionList[i]()
                
        except:
            print("**Something is wrong with " + functionNames[i] + "()")
            printErr()
            points[i], totals[i] = -1, 0

    print("\n\n")
    print("Summary of the Test Results")
    print("======================================")

    for i in range(len(testFunctionList)):
        print(format('q'+str(i+1),'<4'), format(functionNames[i], "27s"), end="")
        if points[i] >= 0:
            print("%2d out of %2d" % (points[i], totals[i]))            
            if points[i] == totals[i] and points[i] in [0,1]:
                print("{}: This question will be checked manually".format(functionNames[i]))
        else:
            print("Not defined or error in function")
#fail =========================================================================
def countFailed(points, totals):
    count = 0
    for i in range(len(points)):
        count += points[i] != totals[i]
    return count
#call =========================================================================
if __name__ == "__main__":
    main()



