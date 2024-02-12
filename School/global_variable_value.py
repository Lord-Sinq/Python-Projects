test_global_var = 99
# maing a main function
def main():

    print('The global variable is known to the main function as', test_global_var)
    func_1()
def func_1():
    x = 6
    print('x is a local variable with value', x,'infunction_1')
    print('The global variable is known to the main function as', test_global_var)
    func_2()
def func_2():
    x = 10
    print('x is a local variable with value', x,'infunction_2')
    print('The global variable is known to the main function as', test_global_var)
# call the main code
main()