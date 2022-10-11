from morse import *

alphabet = "abcdefghijklmnopqrstuvwxyz"
John316 = "For God so loved the world"
Isaiah263 = "Thou wilt keep him in perfect peace"
Psalm231 = "The LORD is my shepherd, I shall not want."

texts = [alphabet,John316,Isaiah263,Psalm231]

Done  = False

count = 0

docode("hello")
blinknum(1,blue)

while not Done:
    val = 0

    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2


    if val == 1:
        count = count+1
        if count == 4:
            count = 0
        blinknum (count+1,blue)

    if val == 2:
        docode(texts[count])

    time.sleep(.2)

