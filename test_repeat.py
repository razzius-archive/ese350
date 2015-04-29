import os

applescript = '''
tell application "System Events"
    delay 3
    key down "17"
    delay 3
    key up "17"
    delay 3
    key down 18
    delay 3
    key up 18
end tell
'''.strip()

cmd = "osascript -e '{}'".format(applescript)

os.system(cmd)
