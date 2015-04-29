import os
from serial import Serial
import sys


script = '''osascript -e \
'tell application "System Events"
    key {} (key code {})
end tell'
'''

def send_key(key):
    cmd = script.format('down', key + 17)
    os.system(cmd)

def release_key(key):
    cmd = script.format('up', key + 17)
    os.system(cmd)

def main(tty):
    mbed = Serial(tty)
    while True:
        val = ord(mbed.read())
        if (val < 10):
            send_key(val)
        else:
            release_key(val - 10)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: serial.py TTY')
        exit(1)

    main(sys.argv[1])
