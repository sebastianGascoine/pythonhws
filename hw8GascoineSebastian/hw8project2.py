# File Name:     hw8project2.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 19, 2022
#
# Problem Statement: Write a program that converts a color image to grayscale
from math import floor
from graphics import *


def main():
    win = GraphWin("", 569, 569)
    win.setCoords(0, 0, 569, 569) #draws the monkeys center to the window
    image = Image(Point((568/2),(568/2)), 'C:/Users/MCCLAB560WD12/Desktop/hw8GascoineSebastian/monkey.gif')
    imagegray = Image(Point((568/2),(568/2)), 'C:/Users/MCCLAB560WD12/Desktop/hw8GascoineSebastian/monkey.gif')
    image.draw(win)
    win.getMouse() #wait for mouse click and send imagegray
    imagegray = grayCalc(imagegray)
    imagegray.draw(win)
    message = Text(Point((568/2),500), "Enter name for grayscale image in Terminal") #
    message.setSize(16) 
    message.setTextColor('white')
    message.draw(win)
    filename = input('Enter name for grayscale image (Ex: monnkeygray.gif)')
    imagegray.save('C:/Users/MCCLAB560WD12/Desktop/hw8GascoineSebastian/'+ filename)
    win.getMouse()
    win.close()

def grayCalc(image):
    width = image.getWidth()
    height = image.getHeight()
    for columns in range(width): # goes through each column and row and sets each pixel to an aver
        for rows in range(height):
            pixel = image.getPixel(columns, rows) #adds rgb together then divide by 3
            grayscale = int(pixel[0]) + int(pixel[1]) + int(pixel[2])
            grayscale = int(floor(float(grayscale)/3))
            # set all pixels to the grayscale
            pixel[0] = grayscale
            pixel[1] = grayscale
            pixel[2] = grayscale
            image.setPixel(columns, rows, color_rgb(pixel[0],pixel[1], pixel[2]))
    
    return image

main()