from morse import *
from prt import *


def intpt(chars):
    Done = False
    blinknum(1,blue)
    ind = 0 #char to return
    print(chars[ind]+"!")      

    while not Done:
        Val = 0
        if touch1.value:
            Val = Val + 1
        if touch2.value:
            Val = Val + 2

            
        if Val == 1:
            ind = ind +1
            if ind == len(chars):
                ind = 0
                blinknum(1,gold)
            blinknum(ind,green)
            print(chars[ind]+"!")      
                        
        if Val == 2:
            Done = True
        time.sleep(.2)
        
    return (chars[ind])