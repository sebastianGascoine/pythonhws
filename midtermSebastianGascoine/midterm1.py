# File Name:     midterm1.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 12, 2022
#
# Problem Statement: Write a program that finds the mean, 
# median, and standard deviation of a list of numbers which you read from a file.  
# 1 number per line and should support both positive and negative number. 


import math
from re import T


def main():
    #open up the input file
    input = open('C:/Users/sebbi/Desktop/pythonhws/midtermSebastianGascoine/input.txt')
    file = input.read()
    list = file.split('\n')
    text1 = mean(list)
    text2 = ''
    text3 = StdDev(list)
    print("mean is: " + str(text1)+ ' '+ str(text3))
    
    input.close()

def mean(list):
    means = 0
    #add all the values together
    for i in list:
        means+= int(i) 
    # amount of lines in file over added values get mean
    lines_in_file = open('C:/Users/sebbi/Desktop/pythonhws/midtermSebastianGascoine/input.txt').readlines()
    number_of_lines = len(lines_in_file)   
    means = means/number_of_lines

    return means
def median(list):
    #mean = mean(list)
    medians = 0
    for i in list:
        pass
    return medians
def StdDev(list): #doesnt work StdDev doesnt call for loop
    print('here1')
    deviation = 0
    retDev = 'The Standard Deviation is:'
    differs = []
    total = 0
    means = mean(list)

    for i in list:
        retDev += str(i)
        pass
    #deviation = deviation/(means-1)
    #retDev += str(math.sqrt(deviation))
    return retDev
main()