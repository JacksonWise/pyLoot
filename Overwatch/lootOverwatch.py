'''
To use program:

on line 16, set boxesToOpen to the desired number of loot boxes to open

within the game: navigate to "loot box"

run lootOverwatch.py
    IMPORTANT: the program registers the first position you click on.
    This should be the "open loot box" button

wait until all that loot rolls in!
'''

# enter number of boxes to open
boxesToOpen = 10

delayAfterOpening = 2 # time delay after boxes open (to look at loot)
timeToOpen = 6 # time before another box can be opened

import pyautogui # third-party module
import time
import pyLoot

posX = posY = 0 # location of "open loot box" button

# main
def manual():
    global boxesToOpen, delayAfterOpening, posX, posY

    # wait for user to click on "open loot box"
    pyLoot.checkClick()
    boxesToOpen = boxesToOpen-1

    # set position on "open loot box" button
    posX, posY = pyautogui.position()

    # wait for first box to fully open, then bring in the loot
    time.sleep(timeToOpen)

    # enjoy some loot
    openBoxes()

# open loot boxes with given positions
def openBoxes():
    global boxesToOpen, posX, posY
    global timeToOpen, delayAfterOpening

    # keep opening those boxes
    while boxesToOpen > 0:
        pyautogui.moveTo(posX, posY)
        pyautogui.click()
        time.sleep(timeToOpen) # wait for box to finish opening
        time.sleep(delayAfterOpening) # admire the glorious loot
        boxesToOpen = boxesToOpen - 1

manual()
