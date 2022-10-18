
import time
import random
import board
import neopixel
import random
import touchio

# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

#define dash, dot, blank and "space" for Morse code
dc = (0,0,40) #dash is blue
dtc= (0,40,0) #dot is green
blank = (0,0,0)
space = (10,0,15) #space is purple

#set up pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)


# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ',':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}
def encryption(message): #recode text message in morse code
   my_cipher = ''
   for myletter in message:
       try:
           if myletter != ' ':
               my_cipher += MORSE_CODE_DICT[myletter] + '  '
           else:
              my_cipher += ' '
       except:
            my_cipher += ' '

   return my_cipher



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

def docolor(color): #show a color  briefly
    for i in range(4):
        pixels[i] = color


    pixels.show()
    time.sleep(.25)

    for i in range(4):
        pixels[i] = blank

    pixels.show()


def blinknum(num,color): #count out a number in a color
    for i in range(num):
        docolor(color)
        time.sleep(.25)



#dospace
def dospace(): # show space for Morse text
   pixels[0] = space
   pixels[1]= space
   pixels[2] = blank


   pixels[3] = blank
   pixels.show()
   time.sleep(.25)

   pixels[0] = blank
   pixels[1]= blank
   pixels.show()
   time.sleep(.25)

#dot
def dot(): # show dot for Morse
   pixels[0] = blank
   pixels[1]= blank
   pixels[2] = blank


   pixels[3] = dtc
   pixels.show()
   time.sleep(.25)

   pixels[3] = blank
   pixels.show()
   time.sleep(.25)

#dash
def dash(): # show dash for Morse

   pixels[0] = blank
   pixels[1]= blank

   pixels[2] = dc
   pixels[3]= dc
   pixels.show()
   time.sleep(.5)

   pixels[2] = blank
   pixels[3]= blank
   time.sleep(.25)
   pixels.show()

def blinkcode(code): #blink out morse code 
    for chr in code:
        if (chr == "-"):
            dash()
        if (chr =="."):
            dot()
        if (chr ==" "):
            dospace()
        else:
            time.sleep(.25)

def docode(text): # display given text in Morse code
    print (text.upper())
    print (encryption(text.upper()))
    blinkcode(encryption(text.upper()))


def compthink(): #blink out all the colors when computer "thinking"
    for clr in colors:
        blinknum(1,clr)

