import datetime
import time
import threading
import json 
import api


# Check current time
def thread_check_time():
    
    check_time = True
    alarms = []

    with open("alarms.txt") as json_file:
        data = json.load(json_file)

    for item in data:
        alarms.append(data[item]["time"])

    while check_time is True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        
        for item in alarms:
            if item == now:
                api.light_on()
                # API call goes here in new thread


# Initiates new thread for time check
def init_time_check_thread():

    check_time = False
    time_thread = threading.Thread(target = thread_check_time, daemon = True)
    time_thread.start()
    
