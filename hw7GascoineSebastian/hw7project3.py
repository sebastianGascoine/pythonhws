# File Name:     hw7project2.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 7, 2022
#
# Problem Statement: Write a program that accepts a speed limit and a clocked speed and either prints a message 
# indicating the speed was legal or prints the amount of the fine, if the speed is illegal.

def main():
    #get speed of car & function will return string if it is legal or not and how much it is
    speed, limit = input('List speed traveled & speed limit Ex:(60, 65)').split(', ')    
    ticket = ticketCalc(int(speed),int(limit))
    print(ticket)

#the function has the two variables which go through the first two lines in march to write less code then at the end of the function i return the line
def ticketCalc(speed,limit):
    fine = 0
    ticketRet = ''
    #safe driving limit is greater than speed
    if(limit >= speed):
        ticketRet = 'Speed Legal'
        return ticketRet
    else:
        #if speed is greater than limit and limit less than 90 with possible extra 200 fine
        if(speed > 90 and limit < 90):
            fine += 200
        # extra 200 fine if speed over 90 and limit under 90
        fine += (speed-limit)*5 + 50 
    ticketRet += 'Driving Over Speed limit Fine:' + str(fine)
    return ticketRet
main()