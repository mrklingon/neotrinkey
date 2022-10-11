import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

REPL = False

def prt(text, REPL):
    if REPL:
        print(text + "\n")
    else:
        keyboard_layout.write(text + "\n")
    time.sleep(.25)
