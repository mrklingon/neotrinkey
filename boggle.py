import time
import random
import neopixel
import random
from morse import *
from prt import *

REPL = False


letters ="abcdefghijklQQETmnoprstuvwxyzeeeeeeooooossssttttnnnQET"

def rl(n):
    o = ""
    for i in range(n):
        z = random.randrange(len(letters))
        l =letters[z]
        if (l == "Q"):
            o = o + " qu"
        else:
            if (l=="E"):
                o =  o +   " er"
            else:
                if (l=="T"):
                    o = o+ " th"
                else:
                    o = o+ "  "+l

    prt (o,REPL)


Done = True
pixels.fill((0, 0, 50))
pixels.show()
while not Done:
    val = 0

    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 1:
        rl(6)
        for i in range(3):
            pixels.fill(
                (random.randrange(20), random.randrange(50), random.randrange(20))
            )
            pixels.show()
            time.sleep(0.25)
            pixels.fill((0, 0, 0))
            pixels.show()
            prt("-------------------------",REPL)

    if val == 2:
        for i in range(3):
            pixels.fill(
                (random.randrange(20), random.randrange(50), random.randrange(20))
            )
            pixels.show()
            time.sleep(0.25)
            pixels.fill((0, 0, 0))
            pixels.show()
            for i in range(3):
                pixels.fill(
                (random.randrange(20), random.randrange(50), random.randrange(20))
            )
                pixels.show()
                time.sleep(0.25)
            pixels.fill((0, 0, 0))
            pixels.show()
        for x in range(6):
            rl(6)
        prt("-------------------------",REPL)

    if val == 3:
        Done = True
