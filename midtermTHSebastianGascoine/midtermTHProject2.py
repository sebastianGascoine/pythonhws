# File Name:     midtermTHProject2.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 15, 2022
#
# Problem Statement: Draw a simple picture with at least 3 graphical objects
#

from graphics import *

def main():
    canx, cany = input('Set canvas size (Ex: 600x600)').split('x')  
    #set up graphics window
    win = GraphWin("", int(canx), int(cany))
    win.setCoords(0, 0, int(canx), int(cany))
    #clicks to track amt to max & to get at list of point/line obj
    clicks = 0
    point = []
    lines = []
    #if you press enter you exit program 
    while(clicks <100):
        if(win.checkKey() == 'Return'):
            print('should break now')
            break
        mouses = win.getMouse() # waits for click in window
        if(mouses != None): #draws point & saves mouse pos to point[]
            mouses.draw(win)
            print('dot placed at',mouses.getX(),mouses.getY())
        point.append(mouses)
        if(len(point)>=2): #waits for 2 dots then draws a line saves line lines[]
            lines.append(Line(point[clicks-1], point[clicks]))
            lines[clicks-1].draw(win)
        
        clicks += 1
    
    #after 10 clicks the program will end the while loop and the next click will close the program
    win.getMouse()
    win.close()

main()