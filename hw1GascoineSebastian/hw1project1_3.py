#! /usr/bin/python
# Exercise No.   3
# File Name:     percentagesprogram.py
# Programmer:    Sebastian Gascoine
# Date:          Aug. 24, 2022
#
# Problem Statement: Write a program that computes the percentage for an exam score.  Your input will be correct answers and total questions.
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two integers
# 3. Calculate the sum of the integers
# 4. Print the sum of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed
def main():
    # Print a message to the screen
    print("Hello!")
    print("I can calculate your test score percentage")
    # Variables are declared dynamically no need to pre-define
    num1, num2 = eval(input("Enter test score (Ex. 70 , 100):"))
    #Here is the processing that is needed
    sum = (num1/num2)
    sum = sum*100
    # Output the results
    print("The test score is", sum)
main()