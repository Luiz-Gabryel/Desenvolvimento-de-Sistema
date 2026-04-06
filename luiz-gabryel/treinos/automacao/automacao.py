import pyautogui
import time

pyautogui.press('win') #aperta uma tecla
pyautogui.write('Chorme', interval=0.25) #escreve na tela esse interval e para ele ir lento
pyautogui.press('enter') 

time.sleep(3)

pyautogui.write('https://saladofuturo.educacao.sp.gov.br/') #, interval=0.25)
pyautogui.press('enter')
time.sleep(8)
pyautogui.click(1553, 576)

#pyautogui.click(622, 425) #click