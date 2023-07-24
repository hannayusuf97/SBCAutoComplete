import tkinter as tk
from tkinter import ttk

import pyautogui

from formations import fouronetwonetwo, fourfourtwo, fourthreeonetwo
from leagues import seriea
from quality import silver_common, bronze_common, gold_common
from sort import low_to_high

stop_execution = False


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

    elif formation == '4312':
        fourthreeonetwo()


window = tk.Tk()
quality_var = tk.StringVar(value="Bronze Common")  # Set the default value for quality
sort_var = tk.StringVar(value="Low to High")  # Set the default value for sorting
formation_var = tk.StringVar(value="41212")  # Set the default value for formation
league_var = tk.StringVar(value="Any")
quality_label = tk.Label(window, text="Quality:")
gold_checkbox = tk.Radiobutton(window, text="Gold Common", variable=quality_var, value="Gold Common")
silver_checkbox \
    = tk.Radiobutton(window, text="Silver Common", variable=quality_var, value="Silver Common")
bronze_checkbox = tk.Radiobutton(window, text="Bronze Common", variable=quality_var, value="Bronze Common")
sort_label = tk.Label(window, text="Sort:")
low_to_high_checkbox = tk.Radiobutton(window, text="Low to High", variable=sort_var, value="Low to High")
high_to_low_checkbox = tk.Radiobutton(window, text="High to Low", variable=sort_var, value="High to Low")
formation_label = tk.Label(window, text="Formation:")
formation_combobox = ttk.Combobox(window, textvariable=formation_var, values=["41212", "442", "4222", "4312"])
league_label = tk.Label(window, text="League:")
league_combobox = ttk.Combobox(window, textvariable=league_var, values=["Any", "Serie A"])
start_button = tk.Button(window, text="Start", command=fifaSBC)
stop_button = tk.Button(window, text="Stop", command=stop)
