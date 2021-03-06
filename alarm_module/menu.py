"""This module contains functions related to the main menu. 

Functions
---------
menu()
    Initializes the main menu
menu_text()
    Prints the main menu options
menu_selection(option)
    Chooses the function for the selected menu option

References
----------
switch statements: 
    https://jaxenter.com/implement-switch-case-statement-python-138315.html
"""

import alarm_module.alarm_mgmt as am
import alarm_module.time_check as tc
import alarm_module.api as api


def menu():
    """Initializes the main menu.
    
    Creates the main menu, takes in an option as input,
    executes the selected option, then restarts the menu.
    """

    print("")
    menu_text()
    print("")

    choice = int(input("Enter Number Selection: ")) 

    menu_selection(choice)
    print("")

    menu() 


def menu_text():
    """Prints the main menu options."""

    print (30 * "-" , "MENU" , 30 * "-")
    print ("1 : Turn Light Off")
    print ("2 : Turn Light On")
    print ("3 : Get Alarm List")
    print ("4 : Add Alarm")
    print ("5 : Delete Alarm")
    print ("6 : Bother Boyfriend")
    print ("0 : Exit")
    print (67 * "-")

    # Want to add:
    # Update Alarm
    # Add Timer (self deletes after turning off)
    # Colors Key List
    # Color Name (to alarm text file)
    

def menu_selection(option):
    """Chooses the function for the selected menu option.

    If an option isn't one of the listed keys,
    it will be invalid and user can try again.
    
    Parameters
    ----------
    option : integer
        Integer choice for switch statement.

    Returns
    -------
    menu_selection() : function
        Function that executes choice option.
    """
    
    print("")

    switch = {
        1: lambda : api.light_off(),
        2: lambda : api.light_on(),
        3: lambda : am.get_alarms(),
        4: lambda : am.add_alarm(),
        5: lambda : am.delete_alarm(),
        6: lambda : api.light_on_notice_me(),
        0: lambda : exit()
    }
    
    invalid_select = "Invalid selection. Press Enter to try again."
    menu_selection = switch.get(option, lambda: input(invalid_select))

    return menu_selection()
