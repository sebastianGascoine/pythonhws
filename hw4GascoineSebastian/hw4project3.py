# File Name:     hw4project2.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 14, 2022
#
# Problem Statement: Create a simple GUI for MyFirstProgram.py using the techniques from the chapter. 
# Your GUI should include both the input of numbers and the output of the answers
#

import string
from graphics import *

def main():
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)

    message = Text(Point(250,465),'place 2 dots to make a line')
    message.draw(win)
    r = Rectangle(Point(20,20),Point(480,480))
    r.setWidth(2)

    
    r.draw(win)
    p1 = win.getMouse() # pause for click in window
    p2 = win.getMouse() # pause for click in window
    x2= p2.getX()
    x1= p1.getX()
    y2= p2.getY()
    y1= p1.getY()
    l = Line(p1,p2)
    l.draw(win)
    dx = x2 + x1
    dy = y2 + y1
    c = Circle(Point(dx/2,dy/2), 5)
    c.draw(win)
    c.setFill('cyan')
    len = (dx*dx)+(dy*dy)
    len /= len
    length = 'lenght of line '
    sl = dy/dx
    slope = 'slope of line '
    message1 = Text(Point(250,445),length+str(len))
    message2 = Text(Point(250,425),slope+str(sl))
    message1.draw(win)
    message2.draw(win)
    win.getMouse()
    win.close()
    
main()