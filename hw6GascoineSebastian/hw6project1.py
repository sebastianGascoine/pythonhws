# File Name:     hw6project1.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 28, 2022
#
# Problem Statement: Write definitions to return the surface area and the volume of a sphere and print the results

from math import pi


def main():
    radius = eval(input("What is the radius of the sphere:"))
    # since I am returning values from the function i am declaring from the function to call in print statement
    area = sphereArea(radius)
    vol = sphereVolume(radius)
    print("The surface area of the sphere is",area,'and the volume is',vol)

def sphereArea(radius):
    # surface area is 4pi(radius)^2 
    # radius^2 * 4 and declare surfArea
    surfArea = radius**2 * 4
    # multiply by pi
    surfArea *= pi
    # return surface area
    return surfArea

def sphereVolume(radius):
    #volume of sphere is 4/3pi(radius)^3
    # setting volume as output and getting radius^3
    volume = radius**3
    # finishing volume by mult by 4 & pi
    volume *= (4/3)
    volume *= pi
    # return volume
    return volume

main()