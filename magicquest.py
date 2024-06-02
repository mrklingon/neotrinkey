import time
import random
import neopixel
import random
import board
import neopixel
import touchio

# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)

from prt import *

REPL = True
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
        
races = ["human", "elf", "dwarf", "hobbit"]
classes = ["wizard", "burglar",  "healer", "warrior"]

travel = [" travels to", " returns from", " explores within", " gets lost at"]


problem = [
    "Suddenly out of {frst} appears a {monster}",
    "{name} is surprised when {monster} attacks from {frst}",
    "A battle begins. The deadly {monster} attacks {name} after leaping out of {frst}!",
    "Alarm! {monster} materializes from the edge of {frst}!",
]

solution = [
    "Stumbling badly, {name} somehow manages to find the {weapon} and dispatch them!",
    "Heroicly, {name} quickly banishes the creature to {forest} with the {weapon}.",
    "Even though {name} fails to find a weapon like {weapon}, the monster shuffles away to {forest}",
]


purpose = ["seeking", "discovering", "losing", "finding"]


def player():
    nm = wisdom("names.mq")
    rc = random.choice(races)
    cl = random.choice(classes)
    return [nm, rc, cl]


Done = False
Player = player()

ind = 0
compthink()
pixels.fill((0, 0, 50))
pixels.show()
while not Done:
    val = 0

    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 1:
        compthink()
        Player = player()
        prt("name: " + Player[0],REPL)
        prt("race: " + Player[1],REPL)
        prt("class: " + Player[2],REPL)

    if val == 2:
        compthink()
        prt("The " + Player[1] + " " + Player[2] + " " + Player[0],REPL)
        prt(random.choice(travel),REPL)
        prt(wisdom("destination.mq"),REPL)
        prt(random.choice(purpose) + " " + wisdom("treasure.mq"),REPL)
        prt(
            random.choice(problem).format(
                name=Player[0], frst=wisdom("forest.mq"), monster=wisdom("enemy.mq")
            )
        ,REPL)
        prt(
            random.choice(solution).format(
                name=Player[0],
                forest=wisdom("forest.mq"),
                monster=wisdom("enemy.mq"),
                weapon=wisdom("weapon.mq"),
            )
        ,REPL)

    if val == 3:
        Done = True
