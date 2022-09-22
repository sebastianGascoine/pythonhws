# hw3project1.py
#     A program that calculates the cost per square inch 
#     of a circular pizza, given its diameter and price
# by: Sebastian Gascoine

import math #


def main():
    print("This is a program that calculates the cost per square inch of a circular pizza, given its diameter and price")
    cost = eval(input("What is the cost? "))
    diameter = eval(input("What is the diameter? "))
    diameter /= 2
    area = diameter*diameter
    area *= math.pi
    costper = cost/area
    print("The cost per square inch is", costper)

main()