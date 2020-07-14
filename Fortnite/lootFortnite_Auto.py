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
llamasToOpen = 2

# enter time between clicks on right arrow to increase llamas
increaseLootDelay = 0.1

# resolutions currently supported
resX = [2560]
resY = [1440]

import pyautogui, time
import pyLoot

# pics used for image recognition
picNames = ['miniLlama', 'miniLlamaLens', 'rightArrow', 'claim']

firstWhackHold = 3 # hold left button down
secondWhackHold = 9 # hold again in case of silver llama
delayAfterOpening = 3 # wait for next llama to appear

# auto image recognition, does everything except laundry
def auto():
    global llamasToOpen, increaseLootDelay, picNames, delayAfterOpening
    numToOpen = llamasToOpen - 1

    # check if resolution used is currently supported
    width, height = pyautogui.size()
    pyLoot.setResolution(resX, resY)

    # set pic names with current resolution
    picNames = pyLoot.setPicNames(picNames, width, height)

    # move to llama, then lens
    coords = pyLoot.findPic(picNames[0], 0.5)
    coords = pyLoot.findPic(picNames[1], 0.5)
    pyautogui.click(coords[0], coords[1])

    # move to and click on right arrow
    coords = pyLoot.findPic(picNames[2], 0.5)
    
    pyLoot.setCoords(coords[0], coords[1])
    pyLoot.increaseLoot(numToOpen, increaseLootDelay)
    
    # move to and click on "claim" button
    coords = pyLoot.findPic(picNames[3], 0.5)

    # bring in the loot
    pyautogui.click(coords[0], coords[1])
    
    time.sleep(delayAfterOpening)
    hitLlamas()

# move to center of screen, hit llama
def hitLlamas():
    global llamasToOpen, firstWhackHold, secondWhackHold, delayAfterOpening

    # default to clicking on center of screen
    width, height = pyautogui.size()
    midX = width/2
    midY = height/2

    # keep hitting those llamas
    while llamasToOpen > 0:
        pyautogui.moveTo(midX, midY)
        whackLlama(firstWhackHold) # first whack
        pyautogui.moveTo(midX, midY)
        whackLlama(secondWhackHold) # second whack in case llama turns silver  
        llamasToOpen = llamasToOpen - 1
        time.sleep(delayAfterOpening) # wait for next llama to appear

# hits llama, holds left mouse button down for specified time
def whackLlama(mouseDownTime):
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(mouseDownTime)
    pyautogui.mouseUp()

auto()
