#module testing
import sys, traceback

def test(expected_result, function, *params):
    """this function supports unit testing of functions. The named function is called
        with the specified parameters, and the returned result is compared to the
        expected result. The function prints details about the function call, including
        the function name and parameter values, and 
        whether the function passed or failed the test. In the event of error,
        the stack trace is printed.

        Parameters:
            expected_result: The result expected from a correct implementation
            function: The name of the function being tested
            *params: a comma-separated list of parameters to the function

        Returns:
            Nothing
    """
    
    funcName = str(function).split()[1]
    p = ""
    for x in params:
        if isinstance(x, str):
            p += "\"" + x +"\","
        else:
            p += str(x)+","
    p = p[:len(p)-1]
    print("Testing "+funcName+"("+str(p)+")")
    try:
        actual_result = function(*params)
        #print("\tActual result = " + str(actual_result) + ", Expected result = " +
              #str(expected_result))
        if are_equal(actual_result, expected_result):
            return True
        else:
            return False
    except:
        print(funcName + " has errors")
        traceback.print_exc()

def testNoPrint(expected_result, function, *params):
    """this function supports unit testing of functions. The named function is called
        with the specified parameters, and the returned result is compared to the
        expected result. The function prints details about the function call, including
        the function name and parameter values, and 
        whether the function passed or failed the test. In the event of error,
        the stack trace is printed.

        Parameters:
            expected_result: The result expected from a correct implementation
            function: The name of the function being tested
            *params: a comma-separated list of parameters to the function

        Returns:
            Nothing
    """
    
    funcName = str(function).split()[1]
    p = ""
    for x in params:
        if isinstance(x, str):
            p += "\"" + x +"\","
        else:
            p += str(x)+","
    p = p[:len(p)-1]
##    print("Testing "+funcName+"("+str(p)+")")
    try:
        actual_result = function(*params)
        #print("\tActual result = " + str(actual_result) + ", Expected result = " +
              #str(expected_result))
        if are_equal(actual_result, expected_result):
            return True
        else:
            return False
    except:
        print(funcName + " has errors")
        traceback.print_exc()

def are_equal(arg1, arg2):
    if (type(arg1) == list or type(arg1) == tuple) and type(arg1) != str:
        return have_same_values(arg1, arg2)
    else:
        return arg1 == arg2

def have_same_values(list1, list2):
    if type(list1) == list:
        list1.sort()
        list2.sort()

    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if isinstance(list1[i], float):
            if round(list1[i], 4) != round(list2[i],4):
                return False
            # No else, keep going
        elif list1[i] != list2[i]:
            return False
        # No else, keep going
        
    return True

def test_LOM(expected_result, function, *params):
    '''
    LOM = "List Order Matters"
    Variation on the test function specifically to deal with list responses
    where the order of items in the list matters.
    '''
    
    funcName = str(function).split()[1]
    p = ""
    for x in params:
        if isinstance(x, str):
            p += "\"" + x +"\","
        else:
            p += str(x)+","
    p = p[:len(p)-1]
    print("Testing "+funcName+"("+str(p)+")")
    try:
        actual_result = function(*params)
        #print("\tActual result = " + str(actual_result) + ", Expected result = " +
              #str(expected_result))
        return actual_result == expected_result
    except:
        print(funcName + " has errors")
        traceback.print_exc()


def test_file_content(expectedFileContents, filename):
    """this function supports unit testing of functions. The named function is called
        with the specified parameters, and the returned result is compared to the
        expected result. The function prints details about the function call, including
        the function name and parameter values, and 
        whether the function passed or failed the test. In the event of error,
        the stack trace is printed.

        Parameters:
            expected_result: The result expected from a correct implementation
            function: The name of the function being tested
            *params: a comma-separated list of parameters to the function

        Returns:
            Nothing
    """

    try:
        infile = open(filename, "r")
    except:
        traceback.print_exc()        

    contents = infile.read()
    
    if len(expectedFileContents) != len(contents):
        return False

    for i in range(len(expectedFileContents)):
        if (expectedFileContents[i] != contents[i]):
            return False
        
    return True
        
