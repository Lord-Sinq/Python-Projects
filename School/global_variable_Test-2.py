test_global_var = 99
# maing a main function
def main():
    global test_global_var
    print('The global variable before any modifications is', test_global_var)
    test_global_var = 0
    print('The global variable is known to the main function as', test_global_var)
    func_1()
    func_2()
def func_1():
    global test_global_var
    x = 6
    print('x is a local variable with value', x,'infunction_1')
    test_global_var = -2
    print('The global variable is known to the main function as', test_global_var)
def func_2():
    global test_global_var
    x = 10
    print('x is a local variable with value', x,'infunction_2')
    test_global_var = 300
    print('The global variable is known to the main function as', test_global_var)
# call the main code
main()