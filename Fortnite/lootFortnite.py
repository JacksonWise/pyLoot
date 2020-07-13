'''
To exit program early perform either of the following:
    1) move mouse to very upper-left of screen (position 0,0)
    2) press 'ctrl-c' in Python Shell

Program import pyautogui to function correctly
    - https://pyautogui.readthedocs.io/en/latest/install.html
'''

'''
To use program:

Open mini llama number selection (the magnifying glass after hovering over llama)

Run pyLlama.py

Move the mouse cursor over the right arrow (increase llamas to open)
After a four second delay, the program will begin

** Mouse must be positioned over the right arrow before program begins **

'''

'''
If running from IDLE:

Remove manual() or auto() function call on the last line of the script

Enter the following line into IDLE (without indent):
    exec(open('pyLlama.py').read())

Then, in IDLE enter the number of mini llamas to open:
    ex: "manual(10)" -or- "auto(4)"
'''

#TO-DO: set first click position - wait for click: use for manual()
# https://pypi.org/project/pynput/ may work

# Enter number of llamas to open if running directly from this script
llamasToOpen = 10

# resolutions supported currently
resX = [2560, 1920, 1280]
resY = [1440, 1080, 720]
width = height = None

import pyautogui, sys, os, time

# pics used for image recognition
picNames = ['miniLlama', 'miniLlamaLens', 'rightArrow', 'claim']

# user chooses number to open or defaults to 10
def manual(numToOpen=llamasToOpen):
    global llamasToOpen
    llamasToOpen = numToOpen

    # user has 4 seconds to move over right-arrow button
    time.sleep(4)
    
    # program clicks on right-arrow button
    pos = pyautogui.position()
    increaseLoot(pos)

    # user has 4 seconds to click on "open loot" button
    time.sleep(4)
    
    '''
    hitLlamas()
    '''
    
# clicks on right arrow, increasing llamas to open
def increaseLoot(pos):
    clicksLeft = llamasToOpen
    while clicksLeft > 0:
        pyautogui.click()
        time.sleep(0.01)
        clicksLeft = clicksLeft - 1

# move to center of screen, hit llama
def hitLlamas():
    width, height = pyautogui.size()
    midX = width/2
    midY = height/2
    
    while llamasToOpen > 0:
        pyautogui.moveTo(midX, midY)
        whackLlama(3) # first whack
        pyautogui.moveTo(midX, midY)
        whackLlama(6) # second whack in case llama turns silver  
        llamasToOpen = llamasToOpen - 1

# hits llama, holds left mouse button down for specified time
def whackLlama(mouseDownTime):
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()

# auto image recognition, does everything except laundry
def auto(numToOpen = llamasToOpen):
    global llamasToOpen, picNames
    llamasToOpen = numToOpen

    getResolution()
    setPics()

    # move to llama, then lens
    coords = findPic(picNames[0], 0.5)
    coords = findPic(picNames[1], 0.5)
    pyautogui.click(coords[0], coords[1])

    # find and click on increase arrow
    coords = findPic(picNames[2], 0.5)
    increaseLoot(coords)

    # click on "open loot" button
    coords = findPic(picNames[3], 0.5)

    '''
    pyautogui.click(coords[0], coords[1])

    hitLlamas(coords)
    '''

# check if current resolution is supported with available pics
def getResolution():
    global width, height, resX, resY

    resPos = 0
    
    width, height = pyautogui.size()

    while resPos < len(resX):
        if resX[resPos] == width and resY[resPos] == height:
            width = height = resPos
            return

    # resolution not found, exit program
    print('Resolution not supported')
    sys.exit()

# sets directory, filename and resolution as strings for pics
def setPics():
    global picNames
    global width, height, resX, resY

    picResolution = '_' + str(resX[width]) + 'x' + str(resY[height]) + '.png'

    # location of pics, 'pics' folder placed in script parent folder
    picLocation = os.path.join(os.getcwd() + '\\pics\\')

    namePos = 0
    while namePos <len(picNames):
        picNames[namePos] = os.path.join(picLocation + picNames[namePos] + picResolution)
        namePos = namePos + 1
                                      
# move to pic specified over set time of movement
def findPic(image, moveTime):
    time.sleep(0.5)
    coords = pyautogui.locateCenterOnScreen(image)
    pyautogui.moveTo(coords[0], coords[1], moveTime)
    return coords

manual(3)
#auto(3)
