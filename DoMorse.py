from morse import *

message1 = "abcdefghijklmnopqrstuvwxyz"
message2 = "Live long and prosper!"
message3 = "May the force be with you!"
message4 = "Never give up, never surrender!"

texts = [message1,message2,message3,message4]

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
        compthink() #indicates end of message

    time.sleep(.2)

