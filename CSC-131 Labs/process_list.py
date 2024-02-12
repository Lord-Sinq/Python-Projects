# this cell will be the processing cell used to take the information done in list_function
# this will be used to call each function from the list_function()
import list_functions
# making a main function to call the others in the other file
def main():
    my_list = list_functions.get_user_list()
    list_functions.number_of_positive_Values(my_list)
    list_functions.number_of_negative_Values(my_list)
    list_functions.number_of_zero_Values(my_list)
    list_functions.avg_of_elements(my_list)
    list_functions.l2_norm(my_list)
# used to call the main function
main()
