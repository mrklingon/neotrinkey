from morse import *

alphabet = "abcdefghijklmnopqrstuvwxyz"
message1 = "Live long and prosper!"
message2 = "May the force be with you!"
message3 = "Never give up, never surrender!"

texts = [alphabet,message1,message2,message3]

Done  = False

count = 0

compthink() #computer thinking
docode("hello") #say hello
blinknum(1,blue)

while not Done:
    val = 0

    if touch1.value: 
        val = val + 1

    if touch2.value:
        val = val + 2


    if val == 1: #advance through messages touching "1"
        count = count+1
        if count == 4:
            count = 0
        blinknum (count+1,blue) #display index+1

    if val == 2: #display message in Morse when touching "2"
        docode(texts[count])

    time.sleep(.2)

