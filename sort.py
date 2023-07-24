import time

from pynput.keyboard import Key, Controller
from movement import move_right, move_down, get_current_card

keyboard = Controller()


def low_to_high():
    time.sleep(1)
    keyboard.press('c')
    time.sleep(1)
    keyboard.release('c')
    time.sleep(1)
    keyboard.press('d')
    time.sleep(2)
    keyboard.release('d')
    move_down()
    get_current_card()
    move_down()
    move_down()
    move_right()
    keyboard.press(Key.esc)
    time.sleep(0.7)
    keyboard.release(Key.esc)
    # set back
    keyboard.press('x')
    time.sleep(1)
    keyboard.release('x')
