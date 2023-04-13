# File Name:     hw10project1.py
# Programmer:    Sebastian Gascoine
# Date:          Nov. 14, 2022
#
# Problem Statement: Create a program that counts the reserved words in a python file.
#Reserved Words: 
# False, None, True, and, as, assert, break, class, continue, def, del, elif, else, 
# except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, 
# pass, raise, return, try, while, with, yield
def state4(input): #loop through each line of file and add to amt each time its a revserve word
    amt = 0 
    outline = ''
    ResWord = ['False', 'None', 'True', ' and', ' as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
    'for', 'from', 'global', 'if', 'import', ' in', ' is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    
    for line in input: #go through each line
        if(line.startswith('#') == False):
            outline = line  # The comma to suppress the extra new line char
            if any(word in outline for word in ResWord):
                print(outline)
                amt+=1

    return amt
def main():
    input = open('C:/Users/sebbi/Desktop/pythonhws/hw10GascoineSebastian/testfile.py',"r")    
    output = state4(input)
    print('The number of reserved words in the document is ' + str(output))
main()