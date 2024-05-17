import pyautogui as pg
import webbrowser
import time

webbrowser.open('https://www.google.com')
time.sleep(1)
#pg.write('japan',interval=0.25)
travel = ('china')
pg.write(travel,interval=0.25)
pg.hotkey('enter')
time.sleep(3)
pg.screenshot(travel+'.png')

for i in range(1,3):
    pg.scroll(-300 * i)
    pg.screenshot(travel+ str(i)+'.png')
    time.sleep(1)