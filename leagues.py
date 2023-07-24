import time

from pynput.keyboard import Key, Controller

from movement import move_right, move_down

keyboard = Controller()


def seriea():
    time.sleep(1)
    keyboard.press('c')
    time.sleep(1)
    keyboard.release('c')
    time.sleep(1)
    keyboard.press('d')
    time.sleep(1)
    keyboard.release('d')
    move_right()
    move_right()
    move_down()
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)
    time.sleep(1)
    move_down()
    move_down()
    move_right()
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)
    time.sleep(1)
    # set back
    keyboard.press('x')
    time.sleep(1)
    keyboard.release('x')
