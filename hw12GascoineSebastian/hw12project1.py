# File Name:     hw12project1.py
# Programmer:    Sebastian Gascoine
# Date:          Dec. 5, 2022
#
import time
def binary_search(arr, x,start):
    
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            end = time.time()
            #print(end-start)
            return mid,(end)
 
    # If we reach here, then the element was not present
    #print(end-start)
    end = time.time()

    return -1,(end)
 

def linear_search(arr,x):
    start = time.time()
    for i in arr:
        if(arr[i] == x):
            end = time.time()
            #print(end-start)
            return 'inside array linear',(end-start)
    
    end = time.time()
    return 'not in array linear',(end-start)


def main():
    arr = list(range(1000))
    num = input('enter a number:')
    start = time.time()
    mid,end = binary_search(arr,int(num),start)
    print(str(end-start))
    if(mid != -1):
        print(num +' input inside of array binary time: '+ str(times) )
    else:
        print(num+' not inside array binary time: '+ str(times) )
    ret, times = linear_search(arr,int(num))
    print(ret+ ' ' +str(times))

main()