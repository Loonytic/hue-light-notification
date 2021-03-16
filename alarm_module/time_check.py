"""Module contains functions related to checking the time.

Functions
---------
thread_check_time()
    Checks the current time and creates an alarms text file
init_time_check_thread()
    Initializes a new thread for checking the time

References
----------
threading: 
    https://realpython.com/intro-to-python-threading/
"""

import datetime
import time
import threading
import json 
import os

import alarm_module.api as api


def thread_check_time():
    """Checks the current time and creates an alarms text file.

    Only creates a file if one doesn't already exist.
    """

    check_time = True
    
    # Check to see if there's an alarms text file already, if not create it
    if not os.path.exists("alarms.txt"): 
        data = {}
        alarmfile = open("alarms.txt", "x")
        with open("alarms.txt", "w") as outfile:
            json.dump(data, outfile, indent = 4)

    with open("alarms.txt") as json_file:
        data = json.load(json_file)

    # Compares the current time with the alarm list, every second
    while check_time is True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")

        # At alarm time, set the alarm's color and turn on the light
        for item in data:
            if data[item]["time"] == now:
                api.set_light_color(data[item]["color"])


def init_time_check_thread():
    """Initializes/refreshes a new thread for checking the time.

    This thread runs in the background. 
    """

    check_time = False
    time_thread = threading.Thread(target = thread_check_time, daemon = True)
    time_thread.start()
    