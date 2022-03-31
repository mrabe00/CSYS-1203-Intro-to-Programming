# Program Name:  Project 0.1
# Date:          3-29-2022
# Programmer:    Matthew Rabe
# Purpose:       Convert Farenheit to Celsius
# Celsius = (Farenheit - 32) x 5/9

# get fahrenheit from our user (type convert to float because we know our result will be float)
farenheit = float(input('Please enter the current temperature in degree Fahrenheit Please include the decimal (example 99.9): '))
# here's our expression.  Takes the well known formula and makes it into an expression
celsius = (farenheit - 32) * (5/9)
# print the output, i'm using an fstring (you shouldn't know what this is at this point but you can use this example to make a number two decimal places)
print(f'{farenheit},Degrees Fahrenheit is {celsius:.2f} Degrees Celsius')
