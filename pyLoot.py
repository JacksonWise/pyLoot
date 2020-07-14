'''
view README file for using programs and installing third-party modules
'''

import pyautogui, pynput #third-party modules
import os, time
from pynput import mouse

resX = resY = 0 # resolution for naming image files
xPos = yPos = 0 # x/y positions for mouse movement and image locating


'''
----- COORDINATES FUNCTIONS -----
'''

# clicks on specified loaction set number of times
def increaseLoot(clicksLeft, timeDelay):
    global xPos, yPos
    
    pyautogui.moveTo(xPos, yPos)
    pyautogui.click(clicks=clicksLeft, interval=timeDelay)

# set position to click on
def setCoords(x, y):
    global xPos, yPos
    xPos, yPos = x, y
    

'''
----- IMAGE RECOGNITION FUNCTIONS -----
'''

# check if current resolution is supported with available pics
# supported resolutions are stored in arrays from calling scripts
def setResolution(resXArray, resYArray):
    global resX, resY

    resPos = 0    
    width, height = pyautogui.size() # current resolution

    # if resolution used is supported, set resX/resY to width/height 
    while resPos < len(resXArray):
        if resXArray[resPos] == width and resYArray[resPos] == height:
            resX, resY = resXArray[resPos], resYArray[resPos]
            return

    # resolution not found, exit program
    print('Resolution not supported')
    sys.exit()

# find and move to pic specified over set time of movement
def findPic(image, moveTime):
    time.sleep(0.5)
    coords = pyautogui.locateCenterOnScreen(image)
    pyautogui.moveTo(coords[0], coords[1], moveTime)
    return coords

# sets directory, filename and resolution as strings for pics
def setPicNames(picNames, resX, resY):

    # 'scriptFolder\pics\examplePic_2560x1440.png'
    picResolution = '_' + str(resX) + 'x' + str(resY) + '.png'

    # location of pics with 'pics' folder placed in script parent folder
    picLocation = os.path.join(os.getcwd() + '\\pics\\')

    namePos = 0
    while namePos < len(picNames):
        picNames[namePos] = os.path.join(picLocation + picNames[namePos] + picResolution)
        namePos = namePos + 1

    return picNames


''' 
 ----- PYNPUT FUNCTIONS -----
'''

# on mouse click, set xPos and yPos to current coordinates
def on_click(x, y, button, pressed):
    if pressed:
        setCoords(x, y)
    if not pressed:
        # Stop listener
        return False

# wait until mouse button is clicked
def checkClick():
    # Collect events until released
    with mouse.Listener(
            on_move=0,
            on_click=on_click,
            on_scroll=0) as listener:
        listener.join()
