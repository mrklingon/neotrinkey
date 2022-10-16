import time
import random
import board
import neopixel
import random
import touchio
from ncount import * 

from prt import *

from words import *
from mwords import *
from kwords import *

REPL = True



def dcode():
    codew = ""

    for i in range(6):
        codew = codew + " " + words[random.randrange(len(words))]
    return (codew)
def trans(galactic):
    file_one = open("trans", "r")

    for word in file_one:
        try:
            (gal,eng) = word.split(":")
            eng = eng.strip("\n")
            gal = gal.strip(" ")
            if (gal == galactic):
                return(eng)
            if (word.find(galactic+":") == 0 ):
                return(eng+"*")
                
            #print ("Gal: "+gal+" English: " + eng)
        except:
            galactic = galactic
            
def kcode():
    code = ""
    tword = ""
    for i in range(6):
        kword =  kwords[random.randrange(len(kwords))]
        code = code + " " +kword
#        print(kword)
        trns = trans(kword)
        tword = tword + " " + trns
#        print(tword)
    return (code+"\n"+tword)


def mcode():
    codew = ""
    tword = ""

    for i in range(6):
        mword = mwords[random.randrange(len(mwords))]
        codew = codew + " " + mword
        trns = trans(mword)
        tword = tword + " " + trns
    return (codew+"\n"+tword)


code = dcode()

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

done = False

blinknum(1,blue)
blinknum(2,red)
blinknum(3,green)

while not done:
    Val = 0
    
    if touch1.value:
        blinknum(1,pink)
        Val = Val + 1
        
    if touch2.value:
        blinknum(2,gold)
        Val = Val + 2
    
    if Val == 1:
        code = mcode()
        prt (code,REPL)
        time.sleep(.25)
    
    if Val == 2:
        code = kcode()
        prt (code,REPL)
        time.sleep(.25)
    if Val == 3:
        blinknum(1,blue)
        blinknum(2,red)
        blinknum(3,green)
        code = dcode()
        prt (code,REPL)
        time.sleep(.25)
        