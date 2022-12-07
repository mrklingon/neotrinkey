import time
import random
import neopixel
import board
import touchio


pause = 2
run = 1
state = pause

grn = (0,20,0)
red = (20,0,0)
blue = (0,0,20)

blank = (0,0,0)

USize = 30

Rule = [0,0,0,1,0,1,1,0]

SRule = [0,0,0,1,0,1,1,0]

Rule30 = [0,0,0,1,1,1,1,0]

Rule110 = [00,1,1,0,1,1,1,0]

RuleSets = [SRule,Rule30,Rule110]

Rpower = [7,6,5,4,3,2,1,0]

cells = [0, 0, 0, 0, 1, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0]

ncells = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0, 0, 0, 0, 0 ,0]

colors = [(25,0,0), (25,25,0), (0,25,0), (0,25, 25), (0,0,25), (25,0,25)]

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)


REPL = True

            
def doBlue():
    

    pixels[0] = blue
    pixels[1]=  blue
    pixels[2] = blue 
    pixels[3] = blue
    
    pixels.show()
    time.sleep(.25)

    pixels[0] = blank
    pixels[1]= blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()



def doRed():
    
    
    pixels[0] = red
    pixels[1]=  red
    pixels[2] = red
    pixels[3] = red
    
    pixels.show()
    time.sleep(.25)

    pixels[0] = blank
    pixels[1]= blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()




def green():
    
    
    pixels[0] = grn
    pixels[1]=  grn
    pixels[2] = grn
    pixels[3] = grn
    
    pixels.show()
    time.sleep(.25)

    pixels[0] = blank
    pixels[1]= blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()


def showCells(colour):
    txtshow   = ""
    for i in range(4):
        if cells[i] ==1:
            pixels[i] = colour
        else:
            pixels[i] = blank
    
    pixels.show()
    
    for i in range(USize):
        if cells[i] ==1:
            txtshow = txtshow + "*"
        else:
            txtshow = txtshow + " "
        
    
    print (txtshow)

def blankCells():
    for i in range(4):
        pixels[i] = (0,0,0)
    pixels.show()
    
def nRight(x):
    if x == USize-1:
        x=0
    return cells[x+1]
        
def nLeft(x):
    if x == 0:
        x=USize-1
    return cells[x-1]*4

def showUni(x):
    #number of gens, to show the whole Universe
    blankCells()
    for g in range(x):
        nGen()
        txtshow = ""
        for i in range(USize):
            if cells[i] == 1:
                pixels[i % 4] = (0,15,0)
                pixels.show()
                txtshow = txtshow + "*"
            else:
                pixels[i % 10] = (0,0,0)
                pixels.show()
                txtshow = txtshow + " "
            time.sleep(.05)
        print(txtshow)
        time.sleep(.5)
    Extinct()
    showCells((0,0,15))
              
def Extinct():
    tot = 0
    for i in range(USize):
        tot = tot + cells[i]
    
    if tot == 0: #extinct!
        doRed()
        doRed()
        doRed()
        print ("Extinction reached!!")
        fixRule()
        doRand() #regenerate!
        showCells(colors[0])
        
    

def nGen():
    for i in range(USize):
        tot = (2 * cells[i])+ nRight(i) + nLeft(i)
        ncells[i] = Rule[7-tot]
        
    for i in range(USize):
        cells[i] = ncells[i]
            

def doGen(x):
    showCells(colors[random.randrange(6)])
    for i in range(x):
        nGen()
        showCells(colors[random.randrange(6)])
        time.sleep(.35)
    
    Extinct() #check for extinction
            
def changeRule():
    for i in range(8):
        if random.randrange(10) >7:
            Rule[i] = 1
        else:
            Rule[i] = 0
              

def fixRule():
    for i in range(8):
        Rule[i] = SRule[i]

def setRule(rn):
    doBlue()
    doBlue()
    for i in range(8):
        Rule[i] = RuleSets[rn][i]




def doRand():
    for i in range(USize):
        if random.randrange(20) <  6:
            cells[i] = 1
        else:
            cells[i] = 0
            
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
ruleNum=0

touched = time.monotonic()
Val = 0

doRed()
green()
doBlue()
doRed()
doBlue()
green()

while True:

    
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()
    
    touched = time.monotonic()
    if state == run:
        doGen(1)
        Extinct()
        
    if Val == 1:
        if state == run:
            state = pause
            ruleNum = ruleNum+1
            if ruleNum > 3:
                ruleNum = 0
            if ruleNum == 3:
                green()
                green()
                changeRule()
                print(Rule)
            else:
                setRule(ruleNum)
    
            print("rulenum: "+str(ruleNum))
            print("pause")
        else:
            state = run
            print("run")
            
        Val = 0
        touched = time.monotonic()

    if Val == 2:
        doRed()
        doRand()
        print("RANDOM!!")
        doGen(1)
        touched = time.monotonic()
        Val = 0
        
    Val = 0


