# Program Name:  Assignment #0 BMI Calculator
# Date:          03/28/2022
# Programmer:    Matthew Rabe

# BMI = Weight / height in inches squared * 703 
print('Welcome to the BMI Calculator Tool')
weight = float(input('Please enter your weight in pounds: '))
height_feet = float(input('Please enter your height in feet: '))
height_inches = float(input('Please enter height in inches: '))
height = (height_feet * 12) + height_inches
bmi = weight / (height*height) * 703
print('Your BMI is:',bmi)
