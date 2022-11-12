# File Name:     hw9project1.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 7, 2022
#
# Problem Statement: Write a program that takes as input the gender of the child, the height of the mother in inches and the height of the father in inches. 
# Output the estimated adult height of the child in feet and inches
# Problem Statement: Use the Button class to create GUI for Homework 7 Project 2
from math import floor
from graphics import *
from button import Button

# Hmale-child = ((Hmother * 13/12) + Hfather ) / 2
# Hfemale-child = ((Hfather * 12/13) + Hmother ) / 2
def main():
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)
    message = Text(Point(250,465),'List gender of kid and the height of both parents in inches')
    message.draw(win)
    r = Rectangle(Point(20,20),Point(480,480))
    r.setWidth(2)
    r.draw(win) 
    

    #boxes for inputs gender mom & dad height
    genBox = Entry(Point(100,375), 10)
    genBox.setText("male")
    genBox.draw(win)

    momBox = Entry(Point(250,375), 10)
    momBox.setText("60")
    momBox.draw(win)

    dadBox = Entry(Point(400,375), 10)
    dadBox.setText("65")
    dadBox.draw(win)
    
    #setup quit and calcbutton
    calcButton = Button(win, Point(250,275), 100, 50, "Calculate")
    calcButton.activate()  
    quitButton = Button(win, Point(250,100), 100, 50, "Quit")
    quitButton.activate()  

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if calcButton.clicked(pt):
            kidheightFeet, kidheight = heightCalc(genBox.getText(),momBox.getText(),dadBox.getText())
            disptext = "The height of the kid is "+ str(kidheight)+" inches or "+ str(kidheightFeet)
            message2 = Text(Point(250,165),disptext)
            message2.draw(win)
        pt = win.getMouse()
    win.close()


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