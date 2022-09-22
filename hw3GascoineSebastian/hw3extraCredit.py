# hw3project3.py
#     A program that prompts the user for a 4-digit year and then outputs the value of the epact. 
# by: Sebastian Gascoine

import math #


def main():
    print("This is a program that prompts the user for a 4-digit year and then outputs the value of the epact. ")
    year = int(eval(input("What is the year ? ")))
    c = year//100
    epact = 8+(c//4)
    epact -= c 
    epact += ((8*c) + 13)//25 
    epact += 11*(year%19)
    epact = epact%30
    print("The Epact will be", epact)

main()