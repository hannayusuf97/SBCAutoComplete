import time

from pynput.keyboard import Key, Controller
from movement import move_right

keyboard = Controller()


def silver_common():
    time.sleep(1)
    keyboard.press('c')
    time.sleep(0.3)
    keyboard.release('c')
    time.sleep(1)
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    move_right()
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)
    time.sleep(1)
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


def bronze_common():
    time.sleep(1)
    keyboard.press('c')
    time.sleep(0.3)
    keyboard.release('c')
    time.sleep(1)
    keyboard.press('d')
    time.sleep(1)
    keyboard.release('d')
    move_right()
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)
    time.sleep(1)
    # set back
    keyboard.press('x')
    time.sleep(1)
    keyboard.release('x')


def gold_common():
    time.sleep(1)
    keyboard.press('c')
    time.sleep(0.7)
    keyboard.release('c')
    time.sleep(1)
    keyboard.press('d')
    time.sleep(1)
    keyboard.release('d')
    move_right()
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)
    move_right()
    time.sleep(1)
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
