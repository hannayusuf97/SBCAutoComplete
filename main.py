import tkinter as tk
import time
from tkinter import ttk

from pynput.keyboard import Key, Controller
import pyautogui

keyboard = Controller()
stop_execution = False  # Flag to indicate whether to stop execution


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


def fouronetwonetwo():
    # Goalkeeper
    get_current_card()
    # get right player
    move_right()
    get_current_card()
    # right again
    move_right()
    get_current_card()
    # two lefts
    move_left()
    move_left()
    get_current_card()
    # move left
    move_left()
    get_current_card()
    # move left
    move_left()
    get_current_card()
    # move up
    move_up()
    get_current_card()
    # move right
    move_right()
    get_current_card()
    # move right
    move_right()
    get_current_card()
    # move right
    move_right()
    get_current_card()
    # move two left
    move_left()
    move_left()
    get_current_card()


def fourfourtwo():
    # Goalkeeper
    get_current_card()
    move_left()
    get_current_card()
    move_left()
    get_current_card()
    move_up()
    get_current_card()
    move_up()
    get_current_card()
    move_right()
    get_current_card()
    move_right()
    get_current_card()
    move_down()
    get_current_card()
    move_left()
    get_current_card()
    move_up()
    get_current_card()
    move_left()
    get_current_card()


def fourtwotwotwo():
    get_current_card()
    move_left()
    get_current_card()
    move_left()
    get_current_card()
    move_up()
    get_current_card()
    move_up()
    get_current_card()
    move_right()
    get_current_card()
    move_right()
    get_current_card()
    move_right()
    get_current_card()
    move_left()
    get_current_card()
    move_up()
    move_left()
    get_current_card()
    move_left()
    get_current_card()


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


def stop():
    global stop_execution
    stop_execution = True


def fifaSBC():
    window_title = "FIFA 23"

    # Get the window's position and size

    window1 = pyautogui.getWindowsWithTitle(window_title)[0]

    # Access the window
    window1.activate()

    quality = quality_var.get()
    sortfilter = sort_var.get()
    formation = formation_var.get()
    league = league_var.get()

    if quality == 'Silver Common' and sortfilter == 'Low to High' and league == 'Serie A':
        # Perform actions for Silver Common and Low to High
        low_to_high()
        silver_common()
        seriea()

    elif quality == 'Bronze Common' and sortfilter == 'Low to High' and league == 'Serie A':
        # Perform actions for Bronze Common and Low to High
        low_to_high()
        bronze_common()
        seriea()

    elif quality == 'Gold Common' and sortfilter == 'Low to High' and league == 'Serie A':
        # Perform actions for Gold Common and Low to High
        low_to_high()
        seriea()
        gold_common()

    elif quality == 'Silver Common' and sortfilter == 'High to Low' and league == 'Serie A':
        # Perform actions for Silver Common and High to Low
        silver_common()
        seriea()

    elif quality == 'Gold Common' and sortfilter == 'High to Low' and league == 'Serie A':
        # Perform actions for Gold Common and Serie A
        seriea()
        gold_common()


    elif quality == 'Bronze Common' and sortfilter == 'High to Low' and league == 'Serie A':
        # Perform actions for Silver Common and High to Low
        bronze_common()
        seriea()

    elif quality == 'Bronze Common' and sortfilter == 'Low to High':
        # Perform actions for Bronze Common and Low to High
        low_to_high()
        bronze_common()

    elif quality == 'Gold Common' and sortfilter == 'Low to High':
        # Perform actions for Gold Common and Low to High
        low_to_high()
        gold_common()

    elif quality == 'Silver Common' and sortfilter == 'Low to High':
        # Perform actions for Silver Common and Low to High
        low_to_high()
        silver_common()

    elif quality == 'Silver Common':
        # Perform actions for Silver Common
        silver_common()

    elif quality == 'Gold Common':
        # Perform actions for Gold Common
        gold_common()

    elif quality == 'Bronze Common':
        bronze_common()

    elif sortfilter == 'Low to High':
        # Perform actions for Low to High
        low_to_high()

    elif league == 'Serie A':
        seriea()

    if formation == '41212':
        # Perform actions for formation 41212
        fouronetwonetwo()

    elif formation == '442':
        fourfourtwo()

    elif formation == '4222':
        fourfourtwo()


window = tk.Tk()
window.title("FIFA SBC by Hanna Yusuf")

# Checkboxes and Combobox
quality_var = tk.StringVar(value="Bronze Common")  # Set the default value for quality
sort_var = tk.StringVar(value="Low to High")  # Set the default value for sorting
formation_var = tk.StringVar(value="41212")  # Set the default value for formation
league_var = tk.StringVar(value="Any")

quality_label = tk.Label(window, text="Quality:")
quality_label.grid(row=0, column=0, padx=5, pady=5)

gold_checkbox = tk.Radiobutton(window, text="Gold Common", variable=quality_var, value="Gold Common")
gold_checkbox.grid(row=0, column=1, padx=5, pady=5)

silver_checkbox = tk.Radiobutton(window, text="Silver Common", variable=quality_var, value="Silver Common")
silver_checkbox.grid(row=0, column=2, padx=5, pady=5)

bronze_checkbox = tk.Radiobutton(window, text="Bronze Common", variable=quality_var, value="Bronze Common")
bronze_checkbox.grid(row=0, column=3, padx=5, pady=5)

sort_label = tk.Label(window, text="Sort:")
sort_label.grid(row=1, column=0, padx=5, pady=5)

low_to_high_checkbox = tk.Radiobutton(window, text="Low to High", variable=sort_var, value="Low to High")
low_to_high_checkbox.grid(row=1, column=1, padx=5, pady=5)

high_to_low_checkbox = tk.Radiobutton(window, text="High to Low", variable=sort_var, value="High to Low")
high_to_low_checkbox.grid(row=1, column=2, padx=5, pady=5)

formation_label = tk.Label(window, text="Formation:")
formation_label.grid(row=2, column=0, padx=5, pady=5)

formation_combobox = ttk.Combobox(window, textvariable=formation_var, values=["41212", "442", "4222"])
formation_combobox.grid(row=2, column=1, padx=5, pady=5)

league_label = tk.Label(window, text="League:")
league_label.grid(row=2, column=2, padx=5, pady=5)

league_combobox = ttk.Combobox(window, textvariable=league_var, values=["Any", "Serie A"])
league_combobox.grid(row=2, column=3, padx=5, pady=5)

# Start Button
start_button = tk.Button(window, text="Start", command=fifaSBC)
start_button.grid(row=3, column=0, padx=5, pady=5)

# Stop Button
stop_button = tk.Button(window, text="Stop", command=stop)
stop_button.grid(row=3, column=1, padx=5, pady=5)

window.mainloop()

if __name__ == '__main__':
    fifaSBC()
