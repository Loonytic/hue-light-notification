"""Module contains functions related to managing data for the alarms.

Functions
---------
get_alarms()
    Gets and displays all alarms from the alarms text file
add_alarm()
    Askes for alarm info and adds an alarm
delete_alarm()
    Asks for name of alarm to delete and deletes chosen alarm
get_alarm_time()
    Asks for the time to set the alarm to and checks if it's valid
validate_time(timestr)
    Validates the time entered when setting an alarm
get_hex_color()
    Asks for the hex color to set the alarm to and checks if valid
validate_hex_color(color)
    Validates the hex color entered when setting an alarm


References
----------
Python if path exists: 
    https://www.geeksforgeeks.org/python-os-path-exists-method/
JSON referencing: 
    https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
splitting strings: 
    https://www.w3schools.com/python/ref_string_split.asp
nested dictionaries: 
    https://www.geeksforgeeks.org/python-nested-dictionary/
check if string is hexadecimal: 
    https://stackoverflow.com/questions/11592261/check-if-a-string-is-hexadecimal

iterate thorugh dictionary: 
    https://realpython.com/iterate-through-dictionary-python/
string methods: 
    https://www.w3schools.com/python/python_ref_string.asp
"""

import os
import json

import alarm_module.time_check as tc
import string


def get_alarms():
    """Gets and displays all alarms from the alarms text file."""
    
    if not os.path.exists("alarms.txt"):
        print("alarms.txt does not exist. Please Add an alarm first.")
        return

    with open("alarms.txt") as json_file:
        data = json.load(json_file)

        for item in data:
            print("Name: " + item)
            print("Time: " + data[item]["time"])
            print("Color: " + data[item]["color"])
            print("")
        
        input("press Enter to continue: ")


def add_alarm():
    """Asks for alarm info and adds an alarm.
    
    Asks for the alarm name, time, and hex code color,
    then adds the given alarm to the alarm text file.

    Checks if input values are valid for hours and minutes.
    Checks if input values are valid hexadecimal
    """
    
    name = input("Enter alarm name: ")

    timestr = get_alarm_time()
    color = get_hex_color()
            
    # Takes alarms and turns the JSON into a python object
    with open("alarms.txt") as json_file:
        data = json.load(json_file)
    
    # Adds alarm to alarms file
    data[name] = {
            "time": timestr,
            "color": color
        }
    with open("alarms.txt", "w") as outfile:
        json.dump(data, outfile, indent = 4)

    # Refreshes time checking thread
    tc.init_time_check_thread()


def delete_alarm():
    """Asks for name of alarm to delete and deletes chosen alarm."""

    if not os.path.exists("alarms.txt"):
        print("alarms.txt does not exist. Please Add an alarm first.")
        return

    with open("alarms.txt") as json_file:
        data = json.load(json_file)

    name = input("Enter name of alarm to delete: ")

    data.pop(name)

    with open("alarms.txt", "w") as outfile:
        json.dump(data, outfile, indent = 4)

    # Refreshes time checking thread
    tc.init_time_check_thread()


def get_alarm_time():
    """Asks for the time to set the alarm to and checks if it's valid.

    Returns
    -------
    timestr : string
        String alarm time in the format of HH:mm:ss
    """
    
    time_valid = False

    while time_valid is False:
        timestr = input("Enter alarm time in 24hr format (HH:mm): ")
        timestr = timestr + ":00"
        time_valid = validate_time(timestr)
        
    return timestr


def validate_time(timestr):
    """Validates the time entered when setting an alarm.

    Adds '0' before the hours digit, if only one digit was entered.
    Checks hours and minutes are both valid time inputs.
    
    Parameters
    ----------
    timestr : string
        String of alarm time to validate.

    Returns
    -------
    output : boolean
        Boolean of whether time is valid or not.
    """

    time = timestr.split(":")
    output = False

    if len(time[0]) == 1:
        timestr = "0" + timestr

    if int(time[0]) > 23 or int(time[0]) < 0:
        print("Please input a valid time.")
        return output
    elif int(time[1]) > 59 or int(time[1]) < 0:
        print("Please input a valid time.")
        return output
    else:
        output = True
        return output


def get_hex_color():
    """Asks for the hex color to set the alarm to and checks if valid.
    
    Returns
    -------
    color : string
        String alarm color in hexadecimal
    """
    
    color_valid = False

    while color_valid is False:
        color = input("enter Hex color value: ")
        color_valid = validate_hex_color(color)

    return color
        

def validate_hex_color(color):
    """Validates the hex color entered when setting an alarm.
    
    Parameters
    ----------
    color : string
        String of hex color value to validate.

    Returns
    -------
    output : boolean
        Boolean of whether hex color value is valid or not.
    """

    output = False

    if len(color) != 6:
        print("Please only input 6 Hexadecimal characters (A-Z, 0-9)")
        return output
    elif all(c in string.hexdigits for c in color) is False:
        print("Please only input 6 Hexadecimal characters (A-Z, 0-9)")
        return output
    else:
        output = True
        return output
