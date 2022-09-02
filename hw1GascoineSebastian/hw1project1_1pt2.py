
#! /usr/bin/python
# Exercise No.   1
# File Name:     MyFirstProgram.py
# Programmer:    Sebastian Gascoine
# Date:          Aug. 24, 2022
#
# Problem Statement: Ask the user to enter three numbers, calculate the sum of 
# these three numbers, and display the sum to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for three integers
# 3. Calculate the sum of the integers
# 4. Print the sum of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed
def main():
    # Print a message to the screen
    print("Hello!")
    print("I can add three number for you")
    # Variables are declared dynamically no need to pre-define
    num1  = eval(input("Enter one whole numbers to multiply(Ex. 52):"))
    num2  = eval(input("Enter one whole numbers to multiply(Ex. 43):"))
    num3  = eval(input("Enter one whole numbers to multiply(Ex. 67):"))
    #Here is the processing that is needed
    sum = num1 * num2 * num3
    # Output the results
    print("The sum of the three numbers is", sum)
main()
