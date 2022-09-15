# File Name:     hw4project2.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 14, 2022
#
# Problem Statement: Create a simple GUI for MyFirstProgram.py using the techniques from the chapter. 
# Your GUI should include both the input of numbers and the output of the answers
#

from graphics import *

def main():
    num1, num2, num3 = eval(input("Enter one whole numbers(Ex. 52 , 68 , 41):"))
    sum = num1 + num2 + num3
    messagebutton = Text(Point(250,250),'press button for sum')
    message1 = Text(Point(100,350), num1)
    message2 = Text(Point(250,350), num2)
    message3 = Text(Point(400,350), num3)
    messagesum = Text(Point(250,150), sum)
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)

    r = Rectangle(Point(20,20),Point(480,480))
    r.setWidth(2)

    
    b = Rectangle(Point(100,200),Point(400,300))
    
    
    message1.draw(win)
    message2.draw(win)
    message3.draw(win)
    messagebutton.draw(win)

    r.draw(win)
    b.draw(win)
    mouses = win.getMouse() # pause for click in window
    messagesum.draw(win)

    win.getMouse()
    win.close()
    
main()