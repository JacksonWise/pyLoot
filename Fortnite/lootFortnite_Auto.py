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
resX = [2560, 1920, 1280]
resY = [1440, 1080, 720]

import pyautogui, time
import pyLoot

# pics used for image recognition
picNames = ['miniLlama', 'miniLlamaLens', 'rightArrow', 'claim']

# auto image recognition, does everything except laundry
def auto():
    global llamasToOpen, increaseLootDelay, picNames
    llamasToOpen = llamasToOpen - 1

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
    pyLoot.increaseLoot(llamasToOpen, increaseLootDelay)
    
    # move to and click on "claim" button
    coords = pyLoot.findPic(picNames[3], 0.5)

    # bring in the loot
    '''
    pyautogui.click(coords[0], coords[1])
    time.sleep(3)
    lootFortnite.hitLlamas(coords)
    '''

auto()
