# Program Name: Percent Change Calculator
# Programmer:   Matthew Rabe
# Date:         04/29/2022
# Version:      0.1

#function definiton

def f_calc_percentage_change(p_orig_numb_in,p_new_numb_in):
    percent_change = 0.0
    percent_change = ((p_new_numb_in - p_orig_numb_in) / p_orig_numb_in) * 100
    return percent_change # return statement

# main program
original_number = float(input("Please enter the ORIGINAL number:\n")) # get original number from our user
new_number = float(input("Please enter the NEW number:\n")) # get new number from our users
calculated_change = f_calc_percentage_change(original_number,new_number) # a variable is assigned the value from a function call with arguments
print(f'The percent change from {original_number} to {new_number} is {calculated_change:.2f}%') # nicely fomatted fstring with {} replacements