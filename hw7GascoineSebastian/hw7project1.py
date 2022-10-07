# File Name:     hw7project1.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 7, 2022
#
# Problem Statement: Write a program that calculates and prints your grade. Input is the percentage of points that you received, the output is the letter grade.


def main():
    prcnt = eval(input("What is the percentage:"))
    # prcntcalc returns a grade value which i assign to grade
    grade = prcntcalc(prcnt)
    print("The grade is an",grade)

def prcntcalc(percent):
    # 90% -100%      A
    #80% - 89.99%    B
    #70% - 79.99%    C
    #60% - 69.99%    D
    #0%   - 59.99%   F
    # create grd for the grade 
    if(percent >= 90.00):
        grd = 'A'
    elif(percent >= 80.00):
        grd = 'B'
    elif(percent >= 70.00):
        grd = 'C'
    elif(percent >= 60.00):
        grd = 'D'
    else:
        grd = 'F'
    
    return grd

main()