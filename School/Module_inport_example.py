import user_info_functions
print('Functions imported')
# this is the main function that calls other functions
def main():
    print('Using the message() function inside the main function')
    name, weight, height = user_info_functions.get_user_info()
    # show user info
    user_info_functions.show_user_info(name, weight, height)
main()
