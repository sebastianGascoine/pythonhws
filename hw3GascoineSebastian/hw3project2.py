# hw3project2.py
#     A program that divides two number and outputs the results using whole numbers and the remainder
# by: Sebastian Gascoine

import math #


def main():
    print("This is a program that divides two number and outputs the results using whole numbers and the remainder")
    numerator = float(eval(input("What is the numerator ? ")))
    denominator = float(eval(input("What is the denominator ? ")))
    numr = round(numerator%denominator ,2)
    num = round(numerator/denominator)
    
    print("The denominator can go into the numerator", num,'times with a remainder of',numr)

main()