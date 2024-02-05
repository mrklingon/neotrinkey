import time
import random
import board
import random
from morse import *
from prt import *

REPL = True


Planets = ["Senvouter", "Kacanope", "Olryke", "Cungade", "Aorilia", "Zoawei", "Gnocehiri", "Gnetarus", "Trion V49V", "Broria KBO6"]
ships = ["The Trident", "Kryptoria", "Black Sparrow", "The Tortoise", "Lavanda", "BS Slayer", "ISS Fate", "SC Determination", "LWSS Shade", "SSE Wish Upon a Star"]
travel = ["travels to", "returns from","orbits","lands at","lifts off from"]
purpose = ["with supplies", "carrying passengers", "with ancient artifacts", "escaping a battle", "pursuing an enemy"]
problem = ["and is damaged in an explosion", "and loses power", "and runs out of fuel"]
solution =  ["and is repaired by automated systems.", " and tumbles out of control till emergency crews reach them", "and just barely reaches destination stardock."]
twist = ["And then a mysterious message arrives from {alien} {place}.",
         "Suddenly a ship appears from {place} warning of imminent {alien} attack.",
         "An urgent emergency message from {place} arrives. The {alien} planet is experiencing an epidemic.",
         "Word comes that the {alien} ambassador has just died on {place}."]

aliens = ["Stezets",
    "Scuns",
    "Cuds",
    "Vrucuins",
    "Bhisih",
    "Ahleath",
    "Dandaeds",
    "Qat'iet",
    "Gad",
    "Nahrins"]

planets = ["Mageinope",
    "Thotreatune",
    "Zolinda",
    "Nilreron",
    "Uclite",
    "Notania",
    "Guapra",
    "Brozalea",
    "Gerth NYV",
    "Strilia Q5OV"]

Done = False

def compthink():
    for i in range(3):
        ind = random.randrange(10)
        pixels.fill((random.randrange(20),random.randrange(50),random.randrange(20)))
        pixels.show()
        time.sleep(.25)
        pixels.fill((0,0,0))
        pixels.show()
ind = 0
pixels.fill((0,0,50))
pixels.show()
place = random.choice(Planets)

while not Done:
    val = 0

    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 1:
        compthink()
        place = random.choice(Planets)
        prt(place,REPL)

    if val == 2:
        compthink()
        prt(random.choice(ships),REPL)
        prt(random.choice(travel),REPL)
        prt(place,REPL)
        prt(random.choice(purpose),REPL)
        prt(random.choice(problem),REPL)
        prt(random.choice(solution),REPL)
        prt(random.choice(twist).format(place=random.choice(planets), alien = random.choice(aliens)),REPL)

    if val ==3:
        Done = True

