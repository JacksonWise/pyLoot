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

firstWhackHold = 3 # hold left button down
secondWhackHold = 9 # hold again in case of silver llama
delayAfterOpening = 3 # wait for next llama to appear

import pyautogui #third-party module
import time
import pyLoot
from pynput import mouse

# main
def manual():
    global llamasToOpen, increaseLootDelay, delayAfterOpening

    increaseLoot(llamasToOpen)
    claimLoot(delayAfterOpening)
    hitLlamas()

# delay before first llama appears after clicking on "claim" button
def claimLoot(delayAfterOpening):
    print('Click on "CLAIM" button')
    pyLoot.checkClick()
    time.sleep(delayAfterOpening)

# move to center of screen, hit llamas until finished
def hitLlamas():
    global llamasToOpen, firstWhackHold, secondWhackHold, delayAfterOpening

    # default to clicking on center of screen
    pyLoot.centerCoords()

    pyLoot.clickWaitHoldDouble(firstWhackHold, secondWhackHold,
                               delayAfterOpening, llamasToOpen)
    
# clicks on right arrow set number of times
def increaseLoot(numToOpen):
    print('Click on right arrow next to "CLAIM" button')

    # wait for first user click on right arrow
    pyLoot.checkClick()

    # first user click sets on-screen llamas to 2, reduce from total
    numToOpen = numToOpen - 2
    pyLoot.clickMultiple(numToOpen, increaseLootDelay)
    
manual()
