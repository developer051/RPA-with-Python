import pyautogui as pg
import webbrowser
import time

webbrowser.open('https://www.google.com')
time.sleep(1)
#pg.write('japan',interval=0.25)
pg.write('jamaica',interval=0.25)
pg.hotkey('enter')
time.sleep(3)
pg.screenshot('jamaica.png')