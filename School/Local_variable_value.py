
# maing a main function
def main():
    func_1()

def func_1():
    x = 6
    print('x is a local variable with value', x,'infunction_1')
    func_2()

def func_2():
    x = 10
    print('x is a local variable with value', x,'infunction_2')

# call the main code
main()