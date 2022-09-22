# File Name:     hw4project1.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 14, 2022
#
# Problem Statement: Draw a simple picture with at least 3 graphical objects
#

from asyncio.windows_events import NULL
from graphics import *

def main():
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)
    c = Circle(Point(250,150), 100)
    r = Rectangle(Point(250,400),Point(380,300))
    t = Polygon(Point(10,10),Point(150,10),Point(35,160))
    c.draw(win)
    r.draw(win)
    t.draw(win)
    c.setFill('red')
    c.setOutline('black')
    r.setFill('peachpuff')
    c.setWidth(5)
    t.setWidth(20)
#    while(1==1):
#        mouses = win.checkMouse() # pause for click in window
#        if(mouses != None):
#            p1 = mouses
#            mouses.draw(win)
#            print('dot placed at',mouses.getX(),mouses.getY())
    win.getMouse()
    win.close()

main()