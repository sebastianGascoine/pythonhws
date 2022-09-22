# File Name:     hw4project2.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 14, 2022
#
# Problem Statement: write a program that allows the user to draw a simple house using five mouse-clicks 
# The first two clicks will be the opposite corners of the rectangular frame of the house.  The third click will indicate the center of the top edge of a rectangular door.
# The fourth click will indicate the center of a square window and the last click will indicate the peak of the roof.

from contextlib import nullcontext
from queue import Empty
import string
from graphics import *

def main():
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)

    r = Rectangle(Point(20,20),Point(480,480))
    r.setWidth(2)    
    r.draw(win)
    msg ='place 2 dots at opposite edges of house'
    message = Text(Point(250,465),msg)
    message.draw(win)

#HOUSE######################################################
    p1 = win.getMouse() # pause for click in window 
    p2 = win.getMouse() # pause for click in window

    p1x= p1.getX() 
    p1y= p1.getY()
    p2x= p2.getX()
    p2y= p1.getY()

    house1 = Rectangle(p1,p2)
    house1.draw(win)
#DOOR#######################################################
    msg = 'place a dot where the center of the top of the door will be' 
    message.setText(msg)   
    p3 = win.getMouse() # pause for click in window
    p3y = p3.getY()
    p3x = p3.getX()
    doortopx = 0
    doorbottomx = 0
# made so you can do either LR or RL to create the house frame
    if(p1x < p2x):
        i = (p2x - p1x)/10
        doortopx = p3x - i
        doorbottomx = p3x + i
        door = Rectangle(Point(doortopx,p3y),Point(doorbottomx,p1y))
    else:
        i = (p1x - p2x)/10
        doortopx = p3x - i
        doorbottomx = p3x + i
        door = Rectangle(Point(doortopx,p3y),Point(doorbottomx,p2y))   

    door.draw(win)
#WINDOW#####################################################
    msg = 'place a dot where the center of the window will be' 
    message.setText(msg)    
    p4 = win.getMouse() # pause for click in window
    p4y = p4.getY()
    p4x = p4.getX()
    windowtopx = (p4x - (i/2))
    windowbottomx = (p4x + (i/2))
    window =  Rectangle(Point(windowtopx,(p4y + (i/2))),Point(windowbottomx,(p4y - (i/2)))) 
    window.draw(win)
#ROOF#######################################################
    msg = 'place a dot where the top of the roof will be' 
    message.setText(msg)  
    p5 = win.getMouse() # pause for click in window
    p5y = p5.getY()
    p5x = p5.getX()

    if(p1x < p2x):
        if(p1y < p2y): #p1 bottom left p2 top right
            L1 = Line(p5,Point(p1x,p1y))
            L2 = Line(p5,p2)
        else: #p1 top left p2 bottom right
            L1 = Line(p5,p1)
            L2 = Line(p5,Point(p2x,p2y))
    else: 
        if(p1y < p2y): #p1 bottom right p2 top left
            L1 = Line(p5,p2)
            L2 = Line(p5,Point(p1x,p2y))
        else: # p1 top right p2 bottom left
            L1 = Line(p5,Point(p2x,p1y))
            L2 = Line(p5,p1)
    

    L1.draw(win)
    L2.draw(win)
    win.getMouse()
    win.close()
    
main()