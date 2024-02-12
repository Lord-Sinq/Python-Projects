# a function for getting user info and returing multiple values
def get_user_info():
    # read the user info
    full_name = input('Enter your full name:')
    user_weight = input('Enter your weight in lbs:')
    user_height = input('Enter your height in inches:')
    # return the obtained info
    return full_name, user_weight, user_height

# call the function here
def show_user_info(name, weight, height):
    print('\n', name, 'is', weight, 'lbs and', height, 'inches')

