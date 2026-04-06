import pyautogui
import time


pyautogui.press('win')
time.sleep(1)
pyautogui.write('Teams')
pyautogui.press('enter')

time.sleep(5) 
pyautogui.click(298, 225) 
time.sleep(2)
pyautogui.click(1080, 908) 


while True:
    pyautogui.write('oi')
    pyautogui.press('enter')
    time.sleep(1)
