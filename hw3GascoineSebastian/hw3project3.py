# hw3project3.py
#     A program to determine the length of a ladder required to reach a given height when leaned against a house
# by: Sebastian Gascoine

import math #


def main():
    print("This is a program to determine the length of a ladder required to reach a given height when leaned against a house")
    angle = float(eval(input("What is the angle ? ")))
    if angle%90 == 0:
      print('the ladder will not reach the wall at that angle')
      exit() 
    
    radian = angle* (math.pi/180)

    height = float(eval(input("What is the height of the house ? ")))
    length = height/(math.sin(radian))    
    print("The length of a ladder required to reach the wall will be", length)

main()