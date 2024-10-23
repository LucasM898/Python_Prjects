import sys
import os
import subprocess
import time
import pyautogui
import random
import string
import threading
if len(sys.argv) > 1:
    if sys.argv[1] == 'google':
        os.system('start https://www.google.com')
    elif sys.argv[1] == 'nitrotype':
        os.system('start https://nitrotype.com/race')
        time.sleep(.5)
        pyautogui.click(843, 733)
    elif sys.argv[1] == 'calculator':
        subprocess.run('calc.exe')
    elif sys.argv[1] == 'newwindow':
        time.sleep(3)
        for x in range(5):
            pyautogui.hotkey('ctrl', 'n')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(0.5)
    elif sys.argv[1] == 'spam':
        time.sleep(3)
        repeat = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        for x in range(repeat):
            randomchar = random.choice(string.printable)
            pyautogui.write(randomchar, interval=0.01)
    elif sys.argv[1] == 'autoclicker':
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'n')
        time.sleep(1)
        pyautogui.click(208, 62)
        pyautogui.write('hello')
        time.sleep(3)
        for x in range(10):
            pyautogui.press('backspace')
        pyautogui.write('https://www.rapidtables.com/tools/click-counter.html')
        pyautogui.hotkey('enter')
        time.sleep(2)
        for x in range(100):
            pyautogui.click(701, 466)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('bye')
        time.sleep(3)
        for x in range(10):
            pyautogui.press('backspace')
        pyautogui.click(1897,  16)
    elif sys.argv[1] == 'mouse':
        time.sleep(3)
        repeat = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        for _ in range(repeat):
            x, y = pyautogui.position()
            pyautogui.click(x, y, clicks=1, interval=0.01)
    elif sys.argv[1] == 'shutdown':
        pyautogui.click(691, 1056, clicks=1)
        time.sleep(.5)
        pyautogui.click(1208, 988, clicks=1)
        time.sleep(.5)
        pyautogui.click(1218, 914, clicks=1)
