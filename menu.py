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

import alarm_mgmt as am
import time_check as tc
#import api


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
    print ("2 : Get Alarm List")
    print ("3 : Add Alarm")
    print ("4 : Delete Alarm")
    print ("5 : Exit")
    print (67 * "-")
    

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
        1: lambda : print("Pretend my light turned off!"), 
        #1: lambda : api.light_off(),
        2: lambda : am.get_alarms(),
        3: lambda : am.add_alarm(),
        4: lambda : am.delete_alarm(),
        5: lambda : exit()
    }
    
    invalid_select = "Invalid selection. Press Enter to try again."
    menu_selection = switch.get(option, lambda: input(invalid_select))

    return menu_selection()
