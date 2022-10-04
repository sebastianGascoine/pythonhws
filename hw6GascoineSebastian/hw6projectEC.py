# File Name:     hw4project1.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 14, 2022
#
# Problem Statement: Draw a simple picture with at least 3 graphical objects
#

from graphics import *

def main():
    #set up graphics window
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)
    c = Circle(Point(0,0), 100)
    #set up clicks the while loop will wait for 10 clicks then the 11th will close the program
    clicks = 0
    while(clicks <10):
        mouses = win.checkMouse() # pause for click in window
        if(mouses != None):
            # undraw is used to remove the old circle (if possible) then circle is set to the mouses position and drawn and filled in
            c.undraw()
            c = Circle(mouses, 100)                    
            c.draw(win)
            c.setFill('red')
            print('circle placed at',mouses.getX(),mouses.getY())
            clicks += 1
    #after 10 clicks the program will end the while loop and the next click will close the program
    win.getMouse()
    win.close()

main()