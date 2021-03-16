"""This script runs the modules to use the notification light.

Functions
---------
tc.init_time_check_thread()
    Initializes a new thread to check the time in the background
menu.menu()
    Initializes the main menu to be used
"""

import menu
import time_check as tc


tc.init_time_check_thread()

menu.menu()
