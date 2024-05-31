import time
import random
import board
import random
import neopixel
import random
import touchio

# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)

from prt import *
REPL = True

travel = ["travels to", "returns from","orbits","lands at","lifts off from"]
purpose = ["with supplies", "carrying passengers", "with ancient artifacts", "escaping a battle", "pursuing an enemy"]
problem = ["and is damaged in an explosion", "and loses power", "and runs out of fuel"]
solution =  ["and is repaired by automated systems.", " and tumbles out of control till emergency crews reach them", "and just barely reaches destination stardock."]
twist = ["And then a mysterious message arrives from {alien} {place}.",
         "Suddenly a ship appears from {place} warning of imminent {alien} attack.",
         "An urgent emergency message from {place} arrives. The {alien} planet is experiencing an epidemic.",
         "Word comes that the {alien} ambassador has just died on {place}."]

Done = False
def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def wisdom(filename):
    
    qs = open(filename)
    for i in range(random.randrange(file_len(filename))+1):
        quote = qs.readline()
        quote = quote.rstrip()
    compthink()
    qs.close()
    return (quote.rstrip())

def compthink():
    for i in range(3):
        ind = random.randrange(10)
        pixels.fill((random.randrange(20),random.randrange(50),random.randrange(20)))
        time.sleep(.25)
        pixels.fill((0,0,0))
ind = 0
pixels.fill((0,0,50))
place = wisdom("planets.sf")

while not Done:
    val = 0

    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 1:
        compthink()
        place = wisdom("planets.sf")
        prt(place,REPL)

    if val == 2:
        compthink()
        prt(wisdom("ships.sf"),REPL)
        prt(random.choice(travel),REPL)
        prt(place,REPL)
        prt(random.choice(purpose),REPL)
        prt(random.choice(problem),REPL)
        prt(random.choice(solution),REPL)
        prt(random.choice(twist).format(place=wisdom("planets.sf"), alien = wisdom("aliens.sf")),REPL)

    if val ==3:
        Done = True
    
    
