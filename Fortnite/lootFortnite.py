'''
To use program:

on line 27, set llamasToOpen to the desired number of mini llamas to open

within the game:
    1) Navigate to "llama shop" -> "loot"
    2) Hover mouse over mini llama
    3) Click on the magnifying glass

run lootFortnite.py
    IMPORTANT: the program registers the first two positions you click on.
    These should be the right arrow (increase llamas) followed by the
    "claim" button after the program finishes adding the number of
    boxes to open.

click on the right arrow  for program to increase llamas
    (Wait until program is done increasing the amount of llamas to open)

click on the "claim" button

wait until all that loot rolls in!

'''

# enter number of llamas to open
llamasToOpen = 10

# enter time between clicks on right arrow to increase llamas
increaseLootDelay = 0.1

import pyautogui #third-party module
import time
import pyLoot
from pynput import mouse

# main
def manual():
    global llamasToOpen, increaseLootDelay

    # wait for first user click on right arrow
    pyLoot.checkClick()

    # program continually clicks on right-arrow button
    width, height = pyautogui.position()
    pyLoot.setCoords(width, height)

    # first user click sets on-screen llamas to 2, reduce from total
    llamasToOpen = llamasToOpen - 2 
    pyLoot.increaseLoot(llamasToOpen, increaseLootDelay)

    # wait for second click on claim button
    pyLoot.checkClick()

    # wait for first llama to appear, then bring in the loot
    time.sleep(2)
    #hitLlamas()

# move to center of screen, hit llama
def hitLlamas():
    global llamasToOpen

    # default to clicking on center of screen
    width, height = pyautogui.size()
    midX = width/2
    midY = height/2

    # keep hitting those llamas
    while llamasToOpen > 0:
        pyautogui.moveTo(midX, midY)
        whackLlama(3) # first whack
        pyautogui.moveTo(midX, midY)
        whackLlama(6) # second whack in case llama turns silver  
        llamasToOpen = llamasToOpen - 1
        time.sleep(2) # wait for next llama to appear

# hits llama, holds left mouse button down for specified time
def whackLlama(mouseDownTime):
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(mouseDownTime)
    pyautogui.mouseUp()

manual()
