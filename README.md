# pyLoot
 Auto lootbox openers

Feel free to use and modify this code with attribution to Jackson "TatoPuppy" Wise.
I'd love to see anything you make with this!

---------- To use pyLoot ----------

1) Move any game scripts (ex. lootOverwatch.py) into the same folder as pyLoot.py
2) Use pip to install the pynput and pyautogui third party modules to Python
    - From Python folder using command line prompt: "python -m pip install pyautogui
    - From Python folder using command line prompt: "python -m pip install pynput"
3) Run your game script
 
Modules documentation:
    - pyautogui docs: https://pyautogui.readthedocs.io/en/latest/
    - pynput docs: https://pypi.org/project/pynput/


---------- To use with image recognition ("...Auto".py" scripts) ----------

- Place the "pics" folder into the scripts folder
   ex. "c:\python\pyLoot\pics"
- Place any pics from games you want in the "pics" folder
- Use pip to install the pyautogui third party module to Python


---------- Exiting a running program ----------

To exit a program early perform either of the following:
    1) Press 'ctrl-c' in Python Shell
    2) If using pyautogui: move mouse to very upper-left of screen (position 0,0)
