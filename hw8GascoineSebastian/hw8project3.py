# File Name:     hw8project3.py
# Programmer:    Sebastian Gascoine
# Date:          Oct. 19, 2022
#
# Problem Statement: Give the truth table for each of the following Boolean expressions.
"""
 not (P or Q) 
 F F | T
 F T | F
 T F | F
 T T | F
 P and Q or R
 F F F | F    1 
 F F T | T    2
 F T F | F    3
 F T T | T    4
 T F F | F    5
 T F T | T    6
 T T F | T    7
 T T T | T    8
"""
"""
 (not P or not Q) and not R
 F F F | T    1 
 F F T | F    2
 F T F | T    3
 F T T | F    4
 T F F | T    5
 T F T | F    6
 T T F | F    7
 T T T | F    8
 (P and Q) or (R and S)
 F F F F | F  1
 F F F T | F  2
 F F T F | F  3
 F F T T | T  4
 F T F F | F  5
 F T F T | F  6
 F T T F | F  7
 F T T T | T  8
 T F F F | F  9
 T F F T | F  10
 T F T F | F  11
 T F T T | T  12
 T T F F | T  13
 T T F T | T  14
 T T T F | T  15
 T T T T | T  16
 
  Put the truth table in a text file called hw8project3.txt.
"""
def state1(output): #go thru range 1 2 3 4 and using mod get 0 & 1 = F & T
    P = False
    Q = False
    print('P Q |T', file=output)
    for i in range(1,5):
        #print(str(i))
        if(i % 2 == 0): # 
            Q = True
        else: 
            Q = False

        if(i % 3 ==0):
            P = True
        
        T = not (P or Q)
        print(str(P) +' '+ str(Q) +' |'+ str(T), file=output)
    return output 
def state2(output): #
    P = False
    Q = False
    R = False
    detQ = 0 # if detR > 1 R = true detR = 0
    print('P Q R |T', file=output)
    for i in range(1,9):
        #print(str(i))
        if(i % 2 == 0): # on off each loop
            R = True
        else: 
            R = False
        
        if(detQ > 1): 
            detQ = 0
            if(Q): # flips between False and True
                Q= False
            else:
                Q = True

        if(i % 5 ==0): # 4on 4off
            P = True
        
        #statement & adding to file 
        T = P and Q or R
        print(str(P) +' '+ str(Q) +' '+ str(R) +' |'+ str(T), file=output)
        detQ +=1
    return output
def state3(output):
    P = False
    Q = False
    R = False
    S = False
    detQ = 0 # if detQ > 1 Q = true detQ = 0
    print('P Q R|T', file=output)
    for i in range(1,9):
        #print(str(i))
        if(i % 2 == 0): # on off each loop
            S = True
        else: 
            S = False
        
        if(detQ > 1): # 2on 2 off
            detQ = 0
            if(Q): # flips between False and True
                Q= False
            else:
                Q = True

        if(i % 5 ==0): # 4on 4off
            P = True
        
        
        T = (not P or not Q) and not R
        print(str(P) +' '+ str(Q) +' '+ str(R) +' |'+ str(T), file=output)
        detQ +=1
    return output
def state4(output):
    P = False
    Q = False
    R = False
    S = False
    detQ = 0 # if detQ > 1 R = true detQ = 0
    detR = 0 # if detR > 1 R = true detR = 0
    print('P Q R S|T', file=output)
    for i in range(1,17):
        #print(str(i))
        if(i % 2 == 0): # on off each loop
            S = True
        else: 
            S = False
        
        if(detQ > 3): # 2on 2 off
            detQ = 0
            if(Q): # flips between False and True
                Q= False
            else:
                Q = True

        if(detR > 1): # 4 on 4 off
            detR = 0
            if(R): # flips between False and True
                R= False
            else:
                R = True

        if(i % 9 ==0): # 8on 8off
            P = True
        
        T = (P and Q) or (R and S)
        print(str(P) +' '+ str(Q) +' '+ str(R) +' '+ str(S) +' |'+ str(T), file=output)
        detQ +=1
        detR +=1
    return output
def main():
    output = open('C:/Users/sebbi/Desktop/pythonhws/hw8GascoineSebastian/hw8project3.txt',"w")
    S = False
    output = state1(output)
    output = state2(output)
    output = state3(output)
    output = state4(output)
    output.close()
main()