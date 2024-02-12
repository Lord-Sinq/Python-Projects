# this cell will be holding the work for the other cell
# the first function will be the get_user_list() to grab user inputs
def get_user_list():
    input_list = []
    # making a flag to keep the loop asking
    Running = True
    while (Running):
        # asking the user for input
        user_input = input('Please enter 1 number at a time till you are happy with your inputs:')
        # if the input is not blank then it coverts it into a float and adds it to the list
        if user_input != '':
            Float = float(user_input)
            input_list.append(Float)
        # ending the while loop
        else:
            Running = False
    # returning the input list
    return input_list
# defining the positive values to count each positive elements
def number_of_positive_Values(input_list):
    # making a count
    count_even = 0
    # taking the elements and checking if they are above 0
    for num in input_list:
        if num > 0:
            count_even += 1
    print('This is the even count:',count_even)
# defining the negative values to count each negative elements
def number_of_negative_Values(input_list):
    # making a count
    count_odd = 0
    # taking the elements and checking if they are below 0
    for num in input_list:
        if num < 0:
            count_odd += 1
    print('This is the odd count:',count_odd)
# defining the zero values to count each zero elements
def number_of_zero_Values(input_list):
    # making a count
    count_zero = 0
    # taking the elements and checking if they are 0
    for num in input_list:
        if num == 0:
            count_zero += 1
    print('This is the zero count:',count_zero)
# defining the avg of the list
def avg_of_elements(input_list):
    # making 2 counters one that adds the elements and the other just counts the elements
    total = 0
    count_avg = 0
    for num in input_list:
        total += num
    # making it not count the zeros as a 1 for the average
        if num < 0 or num > 0:
            count_avg += 1
    avg = total / count_avg
    print('This is the avg of the elements:',avg)
# defining the l2-norm of the list
def l2_norm(input_list):
    sum_squared = 0
    for num in input_list:
        sum_squared += num**2
    print('The L2_norm of this list is:',format(sum_squared**0.5,'.2f'))