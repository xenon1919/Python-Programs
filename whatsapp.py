import pyautogui
import time
time.sleep(2)
count=0
while count <=50:
    pyautogui.typewrite("You are good, Miss Swi")
    pyautogui.press("Enter")
    count=count+1