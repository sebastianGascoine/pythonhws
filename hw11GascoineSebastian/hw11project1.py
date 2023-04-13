# File Name:     hw11project1.py
# Programmer:    Sebastian Gascoine
# Date:          Nov. 30, 2022
#
# Problem Statement: Write a program that simulates an automatic teller machine (ATM)
from graphics import *
from button import Button
import pickle
from pathlib import Path
class user:
    def __init__(self, user, pin, bal, savings):
        self.user = user
        self.pin = pin
        self.bal = bal
        self.savings = savings


def main():
    #### setup window ####
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)
    message = Text(Point(250,445),'Secure ATM')
    message.setSize(28)
    message.draw(win)
    r = Rectangle(Point(20,20),Point(480,480))
    r.setWidth(2)
    r.draw(win) 

    logButton = Button(win, Point(400,200), 100, 50, "login")
    logButton.activate()  
    withButton = Button(win, Point(140,100), 155, 50, "withdraw checking")
    with2Button = Button(win, Point(140,170), 155, 50, "withdraw saving")

    quitButton = Button(win, Point(400,100), 100, 50, "Quit")
    quitButton.activate()  
    #### setup quit and calcbutton ####
    
    #### user info & error msg ####
    userbox = Entry(Point(400,375), 10)
    userbox.setText("USER")
    userbox.draw(win)
    pinbox = Entry(Point(400,345), 10)
    pinbox.setText("PIN")
    pinbox.draw(win)
    errormsg = Text(Point(400,315),'no error')
    errormsg.draw(win)
    balbox = Text(Point(140,385),'$0')
    balbox.setSize(22)
    savbox = Text(Point(140,345),'$0')
    savbox.setSize(22)
    withbox = Entry(Point(140,255), 20)
    withbox.setText("withdraw amount")

    balbox.draw(win)
    savbox.draw(win)
    #### user info & error msg ####
    path = Path('C:/Users/sebbi/Desktop/pythonhws/hw11GascoineSebastian/test.pkl')
    if(path.is_file() == False):
        user1 = user('user1',1234,100.00,1000.00)
        user2 = user('user2',1000,150.00,1500.00)
        user3 = user('user3',3333,100.00,1000.00)
        users = [user1, user2,user3]
        #### set user and pin
        with open('C:/Users/sebbi/Desktop/pythonhws/hw11GascoineSebastian/test.pkl', 'wb') as outp:
            pickle.dump(users, outp)
            #pickle.dump(user2, outp)

    
    #lets you quit and also make card
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if logButton.clicked(pt):
            print('hello')
            accvalid = checkpin(userbox.getText(),pinbox.getText(),message,balbox,savbox,errormsg)
    #### activates withdraw button if login successful ####
            if(errormsg != "no error" or "login error"): 
                withButton.activate()  
                with2Button.activate() 
                withbox.draw(win)
        if withButton.clicked(pt):
           withdrawcheck(accvalid,balbox,withbox.getText(),errormsg)
        if with2Button.clicked(pt):
           withdrawsave(accvalid,savbox,withbox.getText(),errormsg)
        pt = win.getMouse()
    win.close()

####checking withdraw    
def withdrawcheck(acc,baln,amt,err):
    with open('C:/Users/sebbi/Desktop/pythonhws/hw11GascoineSebastian/test.pkl', 'rb') as outp:
        obj = pickle.load(outp)
    if(acc == -1 or float(amt) < 0.0):
        err.setText('withdraw error')
        return
    
    obj[acc].bal = obj[acc].bal - float(amt)
    baln.setText('Checking: $' + str(obj[acc].bal))

    print('cwithdraw')

####saving withdraw    
def withdrawsave(acc,savn,amt,err):
    with open('C:/Users/sebbi/Desktop/pythonhws/hw11GascoineSebastian/test.pkl', 'rb') as outp:
        obj = pickle.load(outp)
    if(acc == -1 or float(amt) < 0.0):
        err.setText('withdraw error')
        return
    
    obj[acc].savings = obj[acc].savings - float(amt)
    savn.setText('Savings: $' + str(obj[acc].savings))
    print('swithdraw')

def checkpin(user,pin,uname,baln,savn,err):
    
    with open('C:/Users/sebbi/Desktop/pythonhws/hw11GascoineSebastian/test.pkl', 'rb') as outp:
        obj = pickle.load(outp)

    #### loops through array of users ####
    for i in range(len(obj)):
        if(str(obj[i].user) == str(user)):
            if(str(obj[i].pin) == str(pin)): #compares user & pin and changes text to your account if logged in
                err.setText('login')
                uname.setText('User ' + str(obj[i].user))
                baln.setText('Checking: $' + str(obj[i].bal))
                savn.setText('Savings: $' + str(obj[i].savings))
                return i
        else: #hides your account details if another incorrect pin is put in
            err.setText('login error')
            uname.setText('login error')
            baln.setText('login error')
            savn.setText('login error')
            return -1


main()