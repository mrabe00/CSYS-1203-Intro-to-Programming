# Program Name: Days of the Week Converter
# Programmer:   Matthew Rabe
# Date:         04/28/2022
# Version:      0.1

#function definiton

def convert_num_to_day(p_day_number_in):
    if p_day_number_in == 1:
        day_name = 'Sunday'
    elif p_day_number_in == 2:
        day_name = 'Monday'
    elif p_day_number_in == 3:
        day_name = 'Tuesday'
    elif p_day_number_in == 4:
        day_name = 'Wednesday'
    elif p_day_number_in == 5:
        day_name = 'Thursday'
    elif p_day_number_in == 6:
        day_name = 'Friday'
    elif p_day_number_in == 7:
        day_name = 'Saturday'
    else: 
        day_name = 'Error Day must be between 1 and 7'
    return day_name # return statement

# main program
user_day_number = 0
while user_day_number >= 0:
    user_day_number = int(input("Please enter the number of the day to be converted to day name (Please enter a negative number to quite):"))
    if user_day_number < 0:
        break
    print(f'The day of the week is {convert_num_to_day(user_day_number)}') # function call with argument
print('Thank you for using the day number to day name converter')
