import time
import random
import board
import neopixel
import random
import touchio

from ncount import *

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

repl = True
debug = False


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

vowels = ""
consonants = ""
rules = []

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

def outPut(text):
    if repl:
        print (text)
    else:
        keyboard_layout.write(text + "\n")


def setWookie():
    outPut("Wookie")
    blinknum(1,green)
    global vowels
    global consonants
    global rules

    vowels = "OUA"
    consonants = "WWRRRHHHWWWRR"
    rules = ["CvvvvC", "CVC", "VVCV", "VCVVVVC","VCVVC"]

def setKlin():
    outPut("Klingon")
    blinknum(2,red)
    global vowels
    global consonants
    global rules

    vowels = "aeiouy"
    consonants = "bcDghjlmnpqQStvwy'"
    rules = ["CVVC", "CVC", "CCVVC", "CVVC","CV"]

def setVul():
    outPut("Vulcan")
    blinknum(3,gold)
    global vowels
    global consonants
    global rules

    vowels = "'iaei'uaiyaoia"
    consonants = "whltrkltkt'khthtrvttsnzh"
    rules = ["CVcvcv", "Cvcv", "Ccv", "Cvvcv","CvVccvcv"]


def setMando():
    outPut("Mando'a")
    blinknum(4,blue)
    global vowels
    global consonants
    global rules

    vowels = "ouaaoaaaaeaeeeauiueaaeaeeaeoaeeaoaeooeaeaaeaeeeaeueeaieaaaoeeieiioaiaiaiae"
    consonants = "slstryshlntryshlntddthnhntcrcrtryshshtryshlnsh'''''''rslrl't'tdtd'tsh'hnshhn'tsh'cshk'tlsr'chkrvrrsrmsrmrdsnrrnrnrmjycrmjyc"

    rules = ["Cvvc", "CvCvC", "vCCvc", "cvVvCv","cvCCvc"]

def setRom():
    outPut("Romulan")
    blinknum(5,orange)
    global vowels
    global consonants
    global rules

    vowels = "'eiueeeiia''"
    consonants = "skfhvhlnvhdhmnhl'rh"

    rules = ["cvCCv", "cvVCv", "cVvCC", "cvVvCv","cVvCCv"]


def mkword():
    rule = rules[random.randrange(len(rules))]
    if debug: print(rule)
    word = ""
    for i in range(len(rule)):
        r=rule[i]
        if debug: print(rule[i])
        if r == "V":
            word = word + pickChar(vowels)
        if r == "v":
            if (random.randrange(100)>49):
                word = word + pickChar(vowels)
        if r == "C":
            word = word + pickChar(consonants)
        if r == "c":
            if (random.randrange(100)>49):
                word = word + pickChar(consonants)

    return word

def pickChar(inp):
    return (inp[random.randrange(len(inp))])

def mkPhrase():
    sent = ""
    for i in range(random.randrange(10)+1):
        sent = sent + " " + mkword()
    return sent


setWookie()

lang = 1
done = False

while not done:
    Val = 0

    if touch1.value:
        blinknum(1,pink)
        Val = Val + 1

    if touch2.value:
        blinknum(2,gold)
        Val = Val + 2

    if Val == 3:
        done = True
        time.sleep(.25)

    if Val == 1:
        lang = lang + 1
        if lang > 5:
            lang = 1

        if lang == 1:
            setWookie()

        if lang == 2:
            setKlin()

        if lang == 3:
            setVul()

        if lang == 4:
            setMando()

        if lang == 5:
            setRom()

        time.sleep(.25)

    if Val == 2:
        phr = mkPhrase()
        if debug: print(phr)
        outPut(phr)
        time.sleep(.25)


