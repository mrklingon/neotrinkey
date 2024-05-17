import time
import random
import board
import neopixel
import random
import touchio
from ncount import * 

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
# diamonds are gold, clubs are blue, hearts are red, and spades are green
suits = ["diamonds","clubs","hearts","spades"]
scolor = [gold,blue,red,green]
faces =["","ace","deuce", "three","four","five","six","seven","eight","nine","ten", "jack","queen","king"]

deck = []

def draw(ncards):
    for i in range(ncards):
        showcard(0)
        crd = deck[0]
        del deck[0]
        deck.append(crd)

def initdeck():
    card = 0
    for suit in range (4):
        for face in range (13):
            deck.append([suit,(face+1)])
            card = card +1
            
def showcard(crd):
    print (faces[deck[crd][1]] + " of " + suits[deck[crd][0]])
    binnum(deck[crd][1],scolor[deck[crd][0]])
    
def shuffle(dck):
    
    for i in range(3):
        pixels[0] = green
        pixels[1] = red
        pixels[2] = gold
        pixels[3] = blue
        pixels.show()
        time.sleep(.15)
        pixels[0] = gold
        pixels[1] = blue
        pixels[2] = green
        pixels[3] = red
        pixels.show()
        time.sleep(.15)
        
    for i in range (100):
        for x in range(51):
            if random.randrange(50) > 24:
                sv = dck[x + 1 ]
                dck[x+1] = dck[x]
                dck[x] = sv
    
        pixels[0] = blank
        pixels[1] = blank
        pixels[2] = blank
        pixels[3] = blank
        pixels.show()                

initdeck()

while True:
    Val = 0
    
    if touch1.value:
        Val = Val + 1
        
    
    if touch2.value:
        Val = Val + 2
        
    if Val == 1:
        shuffle(deck)
        
    if Val == 2:
        draw(1)
     
    if Val == 3:
         docolor((5,0,10))
         shuffle(deck)
         shuffle(deck)
         draw(3)
         time.sleep(.5)
         docolor(blank)
