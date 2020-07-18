'''
To use program:

on line 19, set llamasToOpen to the desired number of mini llamas to open

IMPORTANT: make sure the mini llama, right arrow and "submit" button
are fully showing on the screen (not covered by any Python windows)

run lootFortnite.py

enjoy your goodies!

*** Image Recognition with pyautogui requires exact image matches.
    If the program isn't working, use lootFortnite.py instead. ***

'''

# Enter number of llamas to open
llamasToOpen = 10

# enter time between clicks on right arrow to increase llamas
increaseLootDelay = 0.1

# resolutions currently supported
resX = [1280, 1920, 2560]
resY = [1280, 1920, 1440]

import pyautogui, time
import pyLoot

# pics used for image recognition
picNames = ['miniLlama', 'miniLlamaLens', 'rightArrow', 'claim']

firstWhackHold = 4 # hold left button down
secondWhackHold = 9 # hold again in case of silver llama
delayAfterOpening = 3 # wait for next llama to appear

# main
def auto():
    global llamasToOpen, increaseLootDelay, picNames, delayAfterOpening

    setPics()
    findLlama()
    increaseLoot(llamasToOpen)
    claimLoot(delayAfterOpening) 

# move to and click on "claim" button
def claimLoot(delayAfterOpening):
    global picNames
    
    coords = pyLoot.findPic(picNames[3], 0.5)
    pyautogui.click(coords[0], coords[1])

    time.sleep(delayAfterOpening)
    hitLlamas() # bring in that sweet loot
    
# move to mini llama, then click on magnigying lens
def findLlama():
    global picNames
    
    coords = pyLoot.findPic(picNames[0], 0.5)
    coords = pyLoot.findPic(picNames[1], 0.5)
    pyautogui.click(coords[0], coords[1])
    
# move to center of screen, hit llama
def hitLlamas():
    global llamasToOpen, firstWhackHold, secondWhackHold, delayAfterOpening

    # default to clicking on center of screen
    pyLoot.centerCoords()

    pyLoot.clickWaitHoldDouble(firstWhackHold, secondWhackHold,
                               delayAfterOpening, llamasToOpen)

# move to and continually click on right arrow
def increaseLoot(numToOpen):
    global picNames, increaseLootDelay

    # "claim" button starts at 1
    numToOpen = numToOpen - 1
    
    coords = pyLoot.findPic(picNames[2], 0.5)
    pyLoot.setCoords(coords[0], coords[1])
    pyLoot.clickMultiple(numToOpen, increaseLootDelay)

# check if resolution used is currently supported, set pic names
def setPics():
    global picNames
    
    pyLoot.setResolution(resX, resY)
    picNames = pyLoot.setPicNames(picNames)
    
auto()
