# pyLoot
 Auto lootbox openers

---------- To Use ----------

- move any game scripts (ex. lootOverwatch.py) into the same folder as pyLoot.py
- use pip to install the pynput third party module to Python
    - from Python folder using command line prompt: "python -m pip install pynput"
    - pynput docs: https://pypi.org/project/pynput/


---------- To use with image recognition ("...Auto".py" scripts) ----------

- place the "pics" folder into the scripts folder
   ex. "c:\python\pyLoot\pics"
- place any pics from games you want in the "pics" folder
- use pip to install the pyautogui third party module to Python
    - from Python folder using command line prompt: "python -m pip install pyautogui
    - pyautogui docs: https://pyautogui.readthedocs.io/en/latest/


---------- Exiting a running program ----------

To exit a program early perform either of the following:
    1) press 'ctrl-c' in Python Shell
    2) If using pyautogui: move mouse to very upper-left of screen (position 0,0)
