'''
To exit program early: move mouse to very upper-left of screen (position 0,0)

Must import pyautogui to function correctly
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

Enter the following line into IDLE (without indent):
    exec(open('pyLlama.py').read())

Then, enter the number of mini llamas to open:
    manual(10)
'''

# Enter number of llamas to open if running directly from this script
llamasToOpen = 4

import pyautogui, sys, os, time

# 'pics' folder placed in script parent folder
picMiniLlama = os.path.join(picLocation + '\\miniLlama_2560x1440.png')
picMiniLens = os.path.join(picLocation + '\\miniLlamaLens_2560x1440.png')
picArrow = os.path.join(picLocation + '\\rightArrow_2560_1440.png')
picClaim = os.path.join(picLocation + '\\claim_2560x1440.png')

print(picLocation)

# user brings up the mini llama selection screen
#def manual(numToOpen = llamasToOpen):
def manual(numToOpen=llamasToOpen):
    global llamasToOpen
    llamasToOpen = numToOpen

    time.sleep(4)
    
    # move cursor to right arrow (increase llamas), program does the rest
    pos = pyautogui.position()
    increaseLoot(pos)
    hitLlamas()
    

# clicks on right arrow, increasing llamas to open
def increaseLoot(pos):
    clicksLeft = llamasToOpen
    while clicksLeft > 0:
        pyautogui.click()
        time.sleep(0.01)
        clicksLeft = clicksLeft - 1

def hitLlamas():
    # set mouse to center of screen
    width, height = pyautogui.size()
    midX = width/2
    midY = height/2

    # move to center of screen, hit llama
    while llamasToOpen > 0:
        pyautogui.moveTo(midX, midY)
        firstWhack()
        pyautogui.moveTo(midX, midY)
        secondWhack()        
        llamasToOpen = llamasToOpen - 1

# first of two whacks in case the llama goes silver
def firstWhack():
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()

# second Whack and speeds up waiting process
def secondWhack():
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(6)
    pyautogui.mouseUp()

# TO-DO: add image recognition, make the whole thing automatic
def auto(numToOpen = llamasToOpen):
    global llamasToOpen
    llamasToOpen = numToOpen

    # move to llama, then lens
    coords = findPic(picMiniLlama, 0.5)
    coords = findPic(picMiniLens, 0.5)
    pyautogui.click(coords[0], coords[1])

    # find and click on increase arrow
    coords = findPic(picArrow, 0.5)
    increaseLoot(coords)

    # click on "open" button
    coords = findPic(picClaim, 0.5)

    '''
    pyautogui.click(coords[0], coords[1])

    hitLlamas(coords)
    '''

# move to pic specified
def findPic(image, moveTime):
    time.sleep(0.5)
    coords = pyautogui.locateCenterOnScreen(image)
    pyautogui.moveTo(coords[0], coords[1], moveTime)
    return coords


    
