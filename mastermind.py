import time
import board
import random
import touchio
import neopixel



touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
paleblue = (0,0,1)
white = (20,20,20)
purple = (20,0,30)

colors = [pink,gold,blue,orange,green,red,paleblue,white,purple]

mcolors = [red, green, blue, gold]

code=[]

guess = []

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)

pixels.fill((0,0,50))
pixels.show()

def compthink():
    for clr in colors:
       pixels.fill(clr)
       pixels.show()
       time.sleep(.25)
    pixels.fill(blank)
    pixels.show()

def mkcode():
    for i in range(4):
        code.append(random.choice(mcolors))

def showcode(carray):
    for i in range(4):
        pixels[i] = carray[i]
    pixels.show()

def showscore(exact,off):
    pixels.fill(blank)
    pixels.show()
    if exact>0:
        for i in range(exact):
            pixels[i]=white
    if off>0:
        for i in range(off):
            pixels[i+exact] = purple
    pixels.show()

def testit(carray,test):
    exact = 0 #number of correct cells
    off = 0 #number of correct colors
    sample = []
    csamp = []    

    for i in range(4):
        sample.append(test[i])
        csamp.append(carray[i])

    for i in range(4):
        if sample[i] == csamp[i]:
            exact = exact +1
            sample[i]=blank                
            csamp[i]=blank     

    for i in range(4):
        if sample[i] != blank:
            for j in range(4):
                if sample[i] == csamp[j]:
                    if sample[i] != blank:
                        sample[i]=blank                
                        csamp[j]=blank     
                        off = off + 1


    showcode(testarray)
    time.sleep(3)
    showscore(exact,off)
    time.sleep(3)
#    showcode(carray)
#    time.sleep(3)
    if exact == 4:
        return(True)
    else:
        return(False)

compthink()
mkcode()

guess = 1 #creating code guess
testing = 2  #compare code to guess
test = 3  
ind = 0 #guess pixel index
clr = 0 #guess color

states = [guess, testing, test]
Done = False
state = guess
cnt = 0
while not Done:
    val = 0
    
    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2

    if state == guess:
        pixels[ind] = mcolors[clr]
        pixels.show()

        if val == 1:
            clr = 3 & (clr+1)
        pixels[ind] = mcolors[clr]
        pixels.show()

        if val == 2:
            ind = ind + 1
            if ind == 4:
                state = testing
            testarray = []
            for cell in pixels:
                testarray.append(cell)

    if state == test:
        Done = testit(code,testarray)
        cnt = cnt +1
        if cnt > 4:
            state = guess
            ind = 0
            clr = 0
            pixels.fill(blank)
            pixels.show()

    if state == testing:
        showcode(testarray)
        Done = testit(code,testarray)
        state = test
        cnt = 0
    time.sleep(.25)        

    
