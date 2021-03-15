import alarm_mgmt as am
import time_check as tc

# Main menu
def menu():
    print("")
    menu_text()
    print("")
    choice = int(input("Enter Selection: ")) # Take input for option
    # Check for valid input
    menu_selection(choice)
    print("")
    menu() # restarts menu options


# Prints the menu options
def menu_text():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Reload Alarms")
    print ("2. Get Alarm List")
    print ("3. Add Alarm")
    print ("4. Delete Alarm")
    print ("5. Exit")
    print (67 * "-")
    

# Choose which menu option to run
def menu_selection(arg):
    print("")
    switch = {
        1: lambda : tc.init_time_check_thread(),
        2: lambda : am.get_alarms(),
        3: lambda : am.add_alarm(),
        4: lambda : am.delete_alarm(),
        5: lambda : exit()
    }

    return switch.get(arg, lambda: "Invalid Selection")()

