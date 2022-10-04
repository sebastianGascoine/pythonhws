# File Name:     hw6project1.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 28, 2022
#
# Problem Statement: Write a program to print the lyrics for ten verses of "The Ants Go Marching." This function should be called ten times.

def main():
    # I want to make a for loop 10 times for each verse and add it to lyrics
    lyrics = ''
    for i in range(10):
        #two variables for amount of ants marching and action of the ants I use split to seperate each variable
        numants, actionlit = input('List how many ants there are and the action of them and the action of the little one Ex:(one, sucks his thumb)').split(', ')
        # I call the function ants to take care of all the work
        lyrics += functionAnts(numants,actionlit)
        #clean up the lines by putting each function call on its own line and pass since I wont be using 'i'
        lyrics += '\n'
        pass
    
    # since I am returning values from the function I am declaring from the function to call in print statement
    print(lyrics)

#the function has the two variables which go through the first two lines in march to write less code then at the end of the function i return the line
def functionAnts(num,lit):
    lyric = ''
#I create lyric and pass the i since I wont use it
    for i in range(2):
        lyric += march(num)
        lyric+= ' '
        pass
#finishing the line
    lyric += 'The little one stops to ' + lit + ' '
    lyric += 'And they all go marching down to the ground '
    lyric += 'To get out of the rain, BOOM! BOOM! BOOM!'
 
    return lyric
#used to reduce code written more than once    
def march(num):
    return 'The ants go marching '+ num + ' by ' + num + ', hurrah, hurra'
main()