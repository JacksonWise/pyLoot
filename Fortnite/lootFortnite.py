'''
To use program:

1) on line 27, set llamasToOpen to the desired number of mini llamas to open

2) within the game:
    1) Navigate to "llama shop" -> "loot"
    2) Hover mouse over mini llama
    3) Click on the magnifying glass

3) run lootFortnite.py
    IMPORTANT: the program registers the first two positions you click on.
    These should be the right arrow (increase llamas) followed by the
    "claim" button after the program finishes adding the number of
    boxes to open.

4) click on the right arrow  for program to increase llamas
    (Wait until program is done increasing the amount of llamas to open)

5) click on the "claim" button

6) wait until all that loot rolls in!

'''

# enter number of llamas to open
llamasToOpen = 10

# enter time between clicks on right arrow to increase llamas
increaseLootDelay = 0.1

firstWhackHold = 4 # hold left button down
secondWhackHold = 11 # hold again in case of silver llama
delayAfterOpening = 1 # wait for next llama to appear
firstLlamaWait = 5 # Wait time after clicking on "claim" button

import pyautogui #third-party module
import time
import pyLoot
from pynput import mouse

# main
def manual():
    global llamasToOpen, increaseLootDelay, delayAfterOpening

    increaseLoot(llamasToOpen)
    claimLoot(firstLlamaWait)
    hitLlamas()

# delay before first llama appears after clicking on "claim" button
def claimLoot(firstLlamaWait):
    pyLoot.checkClick()
    time.sleep(firstLlamaWait)

# move to center of screen, hit llamas until finished
def hitLlamas():
    global llamasToOpen, firstWhackHold, secondWhackHold, delayAfterOpening

    # default to clicking on center of screen
    pyLoot.centerCoords()

    pyLoot.clickWaitHoldDouble(firstWhackHold, secondWhackHold,
                               delayAfterOpening, llamasToOpen)
    
# clicks on right arrow set number of times
def increaseLoot(numToOpen):
    # wait for first user click on right arrow
    pyLoot.checkClick()

    # first user click sets on-screen llamas to 2, reduce from total
    numToOpen = numToOpen - 2
    pyLoot.clickMultiple(numToOpen, increaseLootDelay)

# program directions for user
def printDirections():
    print('Click on right arrow next to "CLAIM" button')
    print('Wait for program to increase loot amount')
    print('Finally, click on "CLAIM" button')

manual()
