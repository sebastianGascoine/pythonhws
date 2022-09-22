# File Name:     hw5project2.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 21, 2022
#
# Problem Statement: Write a program that open the file input.txt reads each line into a list.
# Process each item of the list by converting the two number strings in list to numbers and summing them together. 
# Write this sum out to a file, output.txt.
#

def main():
    input = open('input.txt','r')
    output = open('output.txt',"w")
    for i in input:
        first, second = i.split()
        sum = int(first)+int(second)
        print(sum, file=output)

    input.close()
    output.close()
main()