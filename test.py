import pyautogui as pg
import webbrowser
import time

webbrowser.open('https://www.google.com')
time.sleep(1)
#pg.write('japan',interval=0.25)
travel = ('china')
pg.write(travel,interval=0.25)
pg.hotkey('enter')
time.sleep(5)
pg.scroll(-500)
pg.screenshot(travel+'.png')

