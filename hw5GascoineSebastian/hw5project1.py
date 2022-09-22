# File Name:     hw5project1.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 21, 2022
#
# Problem Statement: Make a program that allows the user to type in a phrase and then outputs the acronym for that phrase.

def main():
    phrase = input("Please enter a phrase to make into an acronym: ")
    phrase = phrase.replace('and ' ,'')
    spacebefore = True
    acronym = ''
    for ch in phrase:
        if(ch == ' '):
            spacebefore = True
        else:
            if(spacebefore):
                acronym += ch
                spacebefore = False

    print("The acronym to",phrase, 'is',acronym.upper())

main()