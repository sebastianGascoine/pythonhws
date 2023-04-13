# File Name:     hw12project3.py
# Programmer:    Sebastian Gascoine
# Date:          Dec. 6, 2022
#
import re
#keep caling itself until input length = 0/1

def palin(input):
    print(str(len(input)) + 'len')
    if(len(input) <= 1): #if last input is empty or just has one letter return is a palindrome
        return ('is a palindrome')
    
    outp = re.sub(r'[^a-zA-Z0-9]', '', input) # remove all non alphabet/numbers
    outp = outp.lower() #make all lowercase

    if(outp[-1] == outp[0]): #check last with first and if == then strip them out and call palin again
        print(outp[-1] + ' palin check' + outp[0])
        outp= outp.lstrip(outp[0]).rstrip(outp[-1]) # remove the 2 outside letters ex: racecar ==> aceca
        return palin(outp)
    else:
        return ('is not a palindrome')

    

def main():
    pal = input('enter a phrase to check if it is a palindrome:')
    out = palin(pal)
    print(out)

    print('The phrase ' + str(pal) + ' '+  str(out))
main()