# File Name:     Section2.py
# Programmer:    Sebastian Gascoine
# Date:          Dec 14, 2022
#
# Problem Statement: Write a program that checks for misspelt words using a file and a dictionary file
# if a word is potentially misspelt add to a message on the GUI




def main():
    #create dictionaries and get inputs
    boydict = {}
    girldict = {}
    name = input("Put in a name to see if its the top 1000:") 
    #open files and add to dictionaries
    with open("C:/Users/sebbi/Desktop/pythonhws/FinalTHGascoineSebastian/txtfiles/boynames.txt") as f:
        for line in f:
            (key, val) = line.split()
            boydict.update({key:val})

    with open("C:/Users/sebbi/Desktop/pythonhws/FinalTHGascoineSebastian/txtfiles/girlnames.txt") as f:
        for line in f:
            (key, val) = line.split()
            girldict.update({key:val})

    #get index of when they show or dont   
    try:
        onlist = list(boydict.keys()).index(name.capitalize())
        onlist = int(onlist)+1
    except ValueError:
        onlist = -1     
    try:
        onlist2 = list(girldict.keys()).index(name.capitalize())
        onlist2= int(onlist2)+1
    except ValueError:
        onlist2 = -1     
    
    if(onlist >=0):
        print(f'{name} is {str(onlist)} in popularity among boys with {boydict.get(name.capitalize())} namings')
    else:
        print(f'{name} is not ranked among the 1000 boys names')
    
    if(onlist2 >=0):
        print(f'{name} is {str(onlist)} in popularity among girls with {girldict.get(name.capitalize())} namings')
    else:
        print(f'{name} is not ranked among the 1000 girls names')
    
    

main()