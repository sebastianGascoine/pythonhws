# File Name:     hw8project1.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 19, 2022
#
# Problem Statement: Write a program that computes and outputs the nth Fibonacci number, where n is a value entered by the user. 

def main():
    nth = eval(input("what nth of the fibonacci sequence do you want to go to:"))
    # fib can return either str (when nth <= 0) or list (when nth <= 1)
    fib = Fibonacci(int(nth))
    print("The sequence is",fib)
# 1,1,2,3,5,8,13 seq 1 - 7 nth
def Fibonacci(nth):
    fbnseq = []
    if(nth <= 0): # returns an error if nth is 
        return 'nth must be more than 0'
    if(nth <= 1): # just returns the first number (1)
        fbnseq.append(int(1))
        return fbnseq
    else: # returns fib seq to the nth power
        numseq = 1   
        nthloop = nth -1 
        #nth loop used to get rid of array starting at 0 and fib seq starting at 1 and append 1st and 2nd to start seq
        fbnseq.append(int(1))
        fbnseq.append(int(1))
        while(numseq < nthloop): # add the 2 most recent to the variable and append to the end of fbnseq
            currentfib = fbnseq[numseq-1] + fbnseq[numseq]
            fbnseq.append(currentfib)
            numseq += 1
    
    return fbnseq

main()