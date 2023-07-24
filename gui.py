from pynput.keyboard import Controller

from gui_input import quality_label, gold_checkbox, silver_checkbox, bronze_checkbox, sort_label, low_to_high_checkbox, \
    high_to_low_checkbox, formation_label, formation_combobox, league_label, league_combobox, start_button, stop_button, \
    window


def gui():
    keyboard = Controller()
    # Graphic User Interface (GUI)
    window.title("FIFA SBC by Hanna Yusuf")

    # Checkboxes and Combobox

    quality_label.grid(row=0, column=0, padx=5, pady=5)

    gold_checkbox.grid(row=0, column=1, padx=5, pady=5)

    silver_checkbox.grid(row=0, column=2, padx=5, pady=5)

    bronze_checkbox.grid(row=0, column=3, padx=5, pady=5)

    sort_label.grid(row=1, column=0, padx=5, pady=5)

    low_to_high_checkbox.grid(row=1, column=1, padx=5, pady=5)

    high_to_low_checkbox.grid(row=1, column=2, padx=5, pady=5)

    formation_label.grid(row=2, column=0, padx=5, pady=5)

    formation_combobox.grid(row=2, column=1, padx=5, pady=5)

    league_label.grid(row=2, column=2, padx=5, pady=5)

    league_combobox.grid(row=2, column=3, padx=5, pady=5)

    # Start Button
    start_button.grid(row=3, column=0, padx=5, pady=5)

    # Stop Button
    stop_button.grid(row=3, column=1, padx=5, pady=5)

    window.mainloop()
