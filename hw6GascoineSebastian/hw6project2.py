# File Name:     hw6project1.py
# Programmer:    Sebastian Gascoine
# Date:          Sep. 28, 2022
#
# Problem Statement: Write and test a function to returns the sum of the numbers in the nums 

def main():
    # I want to make nums an array to loop through each value of the array
    nums = []
    nums = eval(input("List your numbers sepererated by a comma Ex:(44 , 22, 12)"))
    # since I am returning values from the function i am declaring from the function to call in print statement
    sum = sumList(nums)
    print("The sum of nums is",sum)


def sumList(nums):
    #loop through each value of the nums[] by using a for in loop 
    #set sums to 0 and add each val of the array to sums and return
    sums = 0
    for i in nums:
        sums += i
 
    return sums

main()