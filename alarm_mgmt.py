import json
import os

# Python if path exists: https://www.geeksforgeeks.org/python-os-path-exists-method/
# JSON referencing: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
# splitting strings: https://www.w3schools.com/python/ref_string_split.asp
# string methods: https://www.w3schools.com/python/python_ref_string.asp
# iterate thorugh dictionary: https://realpython.com/iterate-through-dictionary-python/
# nested dictionaries: https://www.geeksforgeeks.org/python-nested-dictionary/


# Gets and displays alarms from 'alarms.txt' file
def get_alarms():
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


# Function for adding an alarm. Takes in a name, time, and color
def add_alarm():
    
    # Prompts user for input for name, time, and color
    name = input("Enter alarm name: ")

    # Check time inputs are valid for hours and minutes
    timevalid = False
    while timevalid is False:
        timestr = input("Enter alarm time in 24hr format (HH:mm): ")
        timestr = timestr + ":00"
        print(timestr)
        time = timestr.split(":")
        print(len(time[0]))

        # Adds '0' before number, if only one digit is entered in hours
        if len(time[0]) == 1:
            timestr = "0" + timestr
        # Checks for time range for hours and minutes
        if int(time[0]) > 23 or int(time[0]) < 0:
            print("Please input a valid time.")
            continue
        if int(time[1]) > 59 or int(time[1]) < 0:
            print("Please input a valid time.")
            continue
        else:
            timevalid = True

    color = input("enter Hex color value: ")

    # TODO: add check for hex number parameters

    # Check to see if there's an 'alarms' text file already, if not create it
    if not os.path.exists("alarms.txt"): 
        data = {}
        alarmfile = open("alarms.txt", "x")
        with open("alarms.txt", "w") as outfile:
            json.dump(data, outfile, indent = 4)
    
    # Takes everything in 'alarms.txt' and turns the JSON into a python object
    with open("alarms.txt") as json_file:
        data = json.load(json_file)
    
    # Adds alarm to 'alarms.txt'
    data[name] = {
            "time": timestr,
            "color": color
        }
    # Resaves alarm data to 'alarms.txt'
    with open("alarms.txt", "w") as outfile:
        json.dump(data, outfile, indent = 4)


# Deletes alarms
def delete_alarm():
    if not os.path.exists("alarms.txt"):
        print("alarms.txt does not exist. Please Add an alarm first.")
        return

    with open("alarms.txt") as json_file:
        data = json.load(json_file)

    name = input("Enter name of alarm to delete: ")

    data.pop(name)

    with open("alarms.txt", "w") as outfile:
        json.dump(data, outfile, indent = 4)


