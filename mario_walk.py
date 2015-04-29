from pykeyboard import PyKeyboard
import time


delay = .01
k = PyKeyboard()

while True:
    k.press_key('l')
    time.sleep(.1)
    k.release_key('l')
    time.sleep(delay)
