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
llamasToOpen = 5

import pyautogui, sys, time

# user brings up the mini llama selection screen
def manual(numToOpen = llamasToOpen):
    time.sleep(4)
    
    # move cursor to right arrow (increase llamas), program does the rest
    pos = pyautogui.position()
    increaseLoot()
    
    while numToOpen > 0:
        pyautogui.moveTo(pos)
        firstWhack()
        pyautogui.moveTo(pos)
        secondWhack()        
        numToOpen = numToOpen - 1

# clicks on right arrow, increasing llamas to open
def increaseLoot():
    clicksLeft = numToOpen
    while clicksLeft > 0:
        pyautogui.click()
        time.sleep(0.05)
        clicksLeft = clicksLeft - 1

# first whack in case the llama goes silver
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
def auto():
    findMiniLlama()

def findMiniLlama():
    # move to llama
    coords = pyautogui.locateOnScreen('c:\\python\\python38\\pics\\miniLlama.png'))
    pyautogui.moveTo(coords[0], coords[1], duration=.5)

    # move to magnifying lens
    coords = pyautogui.locateOnScreen('c:\\python\\python38\\pics\\magLens.png'))
    pyautogui.moveTo(coords[0], coords[1], duration=.5)
    pyautogui.click(coords[0], coords[1])

    # move to right arrow and click on it set number of times
    coords = pyautogui.locateOnScreen('c:\\python\\python38\\pics\\rightArrow.png'))
    pyautogui.moveTo(coords[0], coords[1], duration=.5)

    numClicks = numToOpen
    while numClicks > 0:
        pyautogui.click(coords[0], coords[1])
        numClicks = numClicks - 1
