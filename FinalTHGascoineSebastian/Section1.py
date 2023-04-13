# File Name:     Section1.py
# Programmer:    Sebastian Gascoine
# Date:          Dec. 13, 2022
#
# Problem Statement: Write a program that checks for misspelt words using a file and a dictionary file
# if a word is potentially misspelt add to a message on the GUI


from graphics import *
from button import Button
from pathlib import Path
from bisect import *

def main():
    #### setup window ####
    win = GraphWin("", 500, 500)
    win.setCoords(0, 0, 500, 500)
    message = Text(Point(250,445),'Spell Checker')
    message.setSize(28)
    message.draw(win)
    r = Rectangle(Point(10,10),Point(490,490))
    r.setWidth(2)
    r.draw(win) 
    logButton = Button(win, Point(400,200), 100, 50, "read files")
    logButton.activate()  

    

    quitButton = Button(win, Point(400,100), 100, 50, "Quit")
    quitButton.activate()  
    
    #### user info & error msg ####
    filebox = Entry(Point(250,375), 25)
    filebox.setText("C:/Users/sebbi/Desktop/pythonhws/FinalTHGascoineSebastian/txtfiles/testfile.txt")
    filebox.draw(win)
    dictbox = Entry(Point(250,345), 25)
    dictbox.setText("C:/Users/sebbi/Desktop/pythonhws/FinalTHGascoineSebastian/txtfiles/english_win.txt")
    dictbox.draw(win)
##setup#########################################################################################
   
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if logButton.clicked(pt):
            pathfile = Path(filebox.getText())
            dictfile = Path(dictbox.getText()) #get text of each file location full path req
            if(pathfile.is_file() and dictfile.is_file()): #if the files exist
                flag = spellchecker(pathfile,dictfile)
                message2 = Text(Point(150,275),'') #add each word to a single string with \n to go down after each word
                words = ''
                message.setText('misspelt words:') 
                for out in flag:
                    words += out 
                    words += '\n'
                message2.setText(words)
                message2.draw(win)
            else:
                print('enter different files') #if the file doesnt exist or if it isnt supported it will not work
                       
            
            
        pt = win.getMouse()
    win.close()

def spellchecker(file,dict):
    flaggedwords = [] #list of misspelt words
     
    with open(dict, 'r') as outp: #gets full dictionary converts to array
        allword = outp.read()
    dictionary = allword.split()    
    
    #go through each word of file
    with open(file, 'r') as outp:
        for line in outp:
            for word in line.split(): 
                res = bisect_left(dictionary,word) #gets first mention of word in dictionary and flags non real words
                if word != dictionary[res]:
                    flaggedwords.append(word)
   
    return flaggedwords

main()