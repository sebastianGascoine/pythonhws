# File Name:     hw7project2.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 7, 2022
#
# Problem Statement: Write a program that takes as input the gender of the child, the height of the mother in inches and the height of the father in inches. 
# Output the estimated adult height of the child in 
from math import floor


def main():
    # Hmale-child = ((Hmother * 13/12) + Hfather ) / 2
    # Hfemale-child = ((Hfather * 12/13) + Hmother ) / 2
    gnd, momheight, dadheight = input('List gender of kid and the height of both parents in inches Ex:(male, 60, 65)').split(', ')
    # since I am returning values from the function i am declaring from the function to call in print statement
    kidheightFeet, kidheight = heightCalc(gnd,momheight,dadheight)
    print("The height of the kid is",kidheight,"inches or",kidheightFeet)


def heightCalc(gen,mom,dad):
    #do calculations by pemdas
    height = 0.00
    heightFeet = ''
    #if statement since calculation is different by gender then go from inside out starting with the double parenthesis
    if(gen == 'male'):
        #convert to float to multiply by 13/12
        height = (13/12)*float(mom)
        height += float(dad)
        height /= 2
    else:
        height = (12/13)*float(dad)
        height += float(mom)
        height /= 2
    #convert inches to feet 
    heightFeet += str(floor(height/12)) + "'"
    heightFeet += str(floor(height % 12)) + '"'
    return heightFeet,height

main()