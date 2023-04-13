# File Name:     hw10project2.py
# Programmer:    Sebastian Gascoine
# Date:          Nov. 15, 2022
#
# Problem Statement: Write a program that takes as input the gender of the child, the height of the mother in inches and the height of the father in inches. 
# Output the estimated adult height of the child in feet and inches
# Problem Statement: Use the Button class to create GUI for Homework 7 Project 2
from graphics import *
from button import Button

# Hmale-child = ((Hmother * 13/12) + Hfather ) / 2
# Hfemale-child = ((Hfather * 12/13) + Hmother ) / 2
def main():
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)
    message = Text(Point(250,465),'List suit and number')
    message.draw(win)
    r = Rectangle(Point(20,20),Point(480,480))
    r.setWidth(2)
    r.draw(win) 
    
    r = Rectangle(Point(30,40),Point(280,420))
    r.setWidth(2)
    r.draw(win) 
    
    #numbers in card
    message1 = Text(Point(50,390),'')
    message1.setSize(18)
    message2 = Text(Point(260,70),'')
    message2.setSize(18)
    message1.draw(win)
    message2.draw(win)

    #boxes for inputs suit and number
    suitbox = Entry(Point(400,375), 10)
    suitbox.setText("hearts")
    suitbox.draw(win)

    number = Entry(Point(400,345), 10)
    number.setText("5")
    number.draw(win)
    
    #setup quit and calcbutton
    calcButton = Button(win, Point(400,200), 100, 50, "change card")
    calcButton.activate()  
    quitButton = Button(win, Point(400,100), 100, 50, "Quit")
    quitButton.activate()  
    #lets you quit and also make card
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if calcButton.clicked(pt):
            draw1 = None
            draw2 = None
            draw3 = None
            draw4 = None
            draw1, draw2, draw3, draw4 = drawsuit(suitbox.getText(),number.getText(),message1,message2)
            if(draw1 != None):
                draw1.undraw() 
                draw1.draw(win) 
            if(draw2 != None):
                draw2.undraw() 
                draw2.draw(win) 
            if(draw3 != None):
                draw3.undraw() 
                draw3.draw(win) 
            if(draw4 != None):
                draw4.undraw() 
                draw4.draw(win)  
        pt = win.getMouse()
    win.close()


def drawsuit(suit,number,m1,m2):
    d1 = None
    d2 = None
    d3 = None
    d4 = None
    if(suit == 'hearts'):
        d1 = Circle(Point(150,250), 20)
        d2 = Circle(Point(170,250), 20)
        d3 = Polygon(Point(135,237),Point(185,237),Point(160,206))
        d1.setFill('red') 
        d2.setFill('red')
        d3.setFill('red')
        d1.setOutline('red') 
        d2.setOutline('red')
        d3.setOutline('red')
    elif(suit == 'clubs'):   
        d1 = Circle(Point(145,240), 20)
        d2 = Circle(Point(175,240), 20)
        d3 = Circle(Point(160,265), 20)
        d4 = Polygon(Point(145,206),Point(175,206),Point(160,235))

        d1.setFill('red') 
        d2.setFill('red')
        d3.setFill('red')
        d4.setFill('red')

        d1.setOutline('red') 
        d2.setOutline('red')
        d3.setOutline('red')
        d4.setOutline('red')

    elif(suit == 'spade'):  
        d1 = Circle(Point(150,230), 15)
        d2 = Circle(Point(170,230), 15)
        d3 = Polygon(Point(137,237),Point(183,237),Point(160,276))

        d4 = Polygon(Point(155,196),Point(165,196),Point(160,235))

        d1.setFill('red') 
        d2.setFill('red')
        d4.setFill('red')
        d3.setFill('red')

        d1.setOutline('red') 
        d2.setOutline('red')
        d4.setOutline('red')
        d3.setOutline('red')

    elif(suit == 'diamond'):   
        d1 = Polygon(Point(160,285),Point(190,245),Point(160,205),Point(130,245))
        d1.setFill('red')
        d1.setOutline('red')
    
    m1.setText(str(number))
    m2.setText(str(number))


    return d1,d2,d3,d4 

main()