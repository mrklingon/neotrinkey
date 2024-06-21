import time
import random


USize = 10
universe = []
newU = []
for i in range(USize*USize):
    universe.append(0)
    newU.append(0)
    
def compthink():
    print("=-=-=-=-=-")
def randU():
    for i in range(USize*USize):
        if random.randrange(100)>60:
            universe[i]=1
        else:
            universe[i]=0
            
def cell(x,y):
    return (y*USize)+x

def showU():
    print("==========")
    for y in range(USize):
        row = ""
        for x in range(USize):
            if universe[cell(x,y)]==1:
                row = row+"*"
            else:
                row = row + " "
        print(row)

hood = [-1,1,-10,10,-11,-9,9,11]

bar = [42,43,44,45,46,47] #bar
glider = [41,42,43,33,22]
rpent = [44,45,35,55,56]
def dopat(pat):
    for i in range(100):
        universe[i] = 0
    for i in pat:
        universe[i] = 1
        

def nbr(s):
    nc = 0
    for delta in hood:
        ss = s + delta
#        print(delta)
        if ss < 0:
            ss = ss + (USize*USize)
        if ss >= (USize*USize):
            ss = ss - (1+ (USize*USize))
#            print("x"+str(ss))
        nc = nc + universe[ss]
        
    return nc

def gen():
    for i in range(USize*USize):
#        print (i)
        nc = nbr(i)
        if nc < 2:
            newU[i]=0
        if nc == 2:
            newU[i]=universe[i]
        if nc == 3:
            newU[i]=1
        if nc > 3:
            newU[i]=0
    for i in range(USize*USize):
        universe[i]=newU[i]


def rungens(num):
    showU()
    for i in range (num):
        time.sleep(1)
        gen()
        showU()
    compthink()

compthink()
for p in [bar,glider,rpent]:
    dopat(p)
    showU()
    rungens(20)
randU()
showU()
rungens(20)
compthink()



