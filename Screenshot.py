from PIL import ImageGrab
import time
import keyboard

def fScreenShot():
    img=ImageGrab.grab()
    img.save('./img/image_{}.jpg'.format(time.strftime('%Y%m%d%H%M%S')))

keyboard.add_hotkey("F9",fScreenShot)
keyboard.wait('esc') # 'esc'가 눌릴때까지 프로그램실행..

