import pyautogui  as pg
import time
import pyperclip

def autotype():
    time.sleep(3)  #หน่วงเวลาก่อนเริ่มต้น Program ไว้ 5 วินาที
    #pg.click('np.PNG')
    pg.click(3208,172)
    time.sleep(0.5) 
    pg.write('Hello World',interval=0.25)

    time.sleep(1)
    pg.click(3335,494)
    time.sleep(0.5)
    pyperclip.copy('สวัสดีชาวโลก')
    pg.hotkey('ctrl','v',interval=0.25)

autotype()


'''
box1=(3208,172)
box2=(3335,494)
'''

