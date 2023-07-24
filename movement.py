import time
from pynput.keyboard import Key, Controller

keyboard = Controller()


def get_current_card():
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press('c')
    time.sleep(1)
    keyboard.release('c')
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.release(Key.enter)


def move_right():
    time.sleep(1)
    keyboard.press(Key.right)
    time.sleep(0.2)
    keyboard.release(Key.right)


def move_left():
    time.sleep(1)
    keyboard.press(Key.left)
    time.sleep(0.2)
    keyboard.release(Key.left)


def move_up():
    time.sleep(1)
    keyboard.press(Key.up)
    time.sleep(0.2)
    keyboard.release(Key.up)


def move_down():
    time.sleep(1)
    keyboard.press(Key.down)
    time.sleep(0.2)
    keyboard.release(Key.down)
