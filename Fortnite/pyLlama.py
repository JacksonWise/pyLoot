'''
To exit program early: move mouse to very upper-left of screen (position 0,0)

Must import pyautogui to function correctly
    - https://pyautogui.readthedocs.io/en/latest/install.html

Enter the following line into IDLE (without indent):
    exec(open('pyLlama.py').read())

Then, enter the number of mini llamas to open:
    manual(10)
'''

import pyautogui, sys, time

# find screen resolution
width, height = pyautogui.size()

def test(numToOpen = 5):
    while numToOpen > 0:
        print(numToOpen)
        numToOpen = numToOpen-1

# user brings up first llama, program opens set amount after
def manual(numToOpen = 5):
    # move cursor to middle of screen
    pyautogui.moveTo(width/2, height/2, duration = 0.5)
    
    while numToOpen > 0:
        firstWhack()
        secondWhack()        
        numToOpen = numToOpen - 1

# first whack in case the llama goes silver
def firstWhack():
    pyautogui.moveTo(width/2, height/2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()

# second Whack and speeds up waiting process
def secondWhack():
    pyautogui.moveTo(width/2, height/2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(6)
    pyautogui.mouseUp()

# TO-DO: add image recognition, make the whole thing automatic
def auto():
    pass


    
