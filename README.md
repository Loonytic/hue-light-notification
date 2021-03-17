# hue-light-notification

# STILL EDITING:
### Still need to: 
- Update this README to match master (currently just copied from Final-Modified's Jupyter notebook)

### Copy submitted for COGS 18 Final Project:
- Under branch: Final-Modified


# Philips Hue Light Notification Alarm

My project is a light notification alarm. The script opens a menu where the user can **set an alarm**, along **with a corresponding light color**. When it's time for the alarm to go off, it turns the light on to the specific choosen color, which **stays on until the user turns it off**. 

The **script and modules utilize the Philips Hue API**, using a **Philips Hue white and color smart bulb** and a **Philips bridge**. 

All **smart bulbs need to connect to a bridge** to access their "smart" capabilities.


## Demonstration Video
https://youtu.be/vLPcNovONdw

**Side Note:** "Turn Light On" and "Bother Boyfriend" are new menu options ones that I added to my 'master' app, they weren't included in my original COGS 18 project submission.



## Background:
The inspiration for this project came from my tendency to forget about my alarms after turning them off. I set a lot of alarms throughout the day to keep myself on track, but I turn them off immediately when they start ringing because they can be noisy and disturbing. I usually end up forgetting about them for hours and end up not following through on whatever it was I set the alarm for. Using a colored light instead of a sound would allow me leave the alarm on until I complete the intended task. 



## Notes About the API, related to Project Submission:
- In order to use the Philips Hue API to send commands to the lights, the **bridge creates an IP address** that is then **used to create an API key**. 
    - **Both** the bridge's IP address and the API key are **needed to make the API call**. 
- The bridge can only receive http requests from inside our network, so the **code will only run properly inside our home network**.
    - To remedy this, **I'm commenting out my API call** and **setting a print statement instead**. 
    - The **master I upload to GitHub will be the correct version** that runs the code properly from my home computer.
    - I'll also upload my **project submission copy as a branch** of my master on GitHub (**inal-Modified**)
    - I'll also include a **video to demonstrate** my code working with **my lights in my room**. 
- For security purposes, the **copies I upload to GitHub will not have my API credentials**. I saved the actual bridge IP address and API key to variables in a separate, hidden module (called secret). I will not be uploading that file to GitHub, but maybe I'll upload an example file, for reference.



# To run the script, execute main.py




# File Organization:

### main.py
Script that runs the modules to use the notification light alarm.

- **tc.init_time_check_thread()**
    - Initializes a new thread to check the time in the background
- **menu.menu()**
    - Initializes the main menu to be used

### menu.py
Module that contains functions related to the main menu.

- **menu()**
    - Initializes the main menu
- **menu_text()**
    - Prints the main menu options
- **menu_selection(option)**
    - Chooses the function for the selected menu option

### alarm_mgmt.py
Module that contains functions related to managing the data for the alarms.

- **get_alarms()**
    - Gets and displays all alarms from the alarms text file
- **add_alarm()**
    - Askes for alarm info and adds an alarm
- **delete_alarm()**
    - Asks for name of alarm to delete and deletes chosen alarm
- **get_alarm_time()**
    - Asks for the time to set the alarm to and checks if it's valid
- **validate_time(timestr)**
    - Validates the time entered when setting an alarm
- **get_hex_color()**
    - Asks for the hex color to set the alarm to and checks if valid
- **validate_hex_color(color)**
    - Validates the hex color entered when setting an alarm

### time_check.py
Module that contains functions related to checking the current time.

- **thread_check_time()**
    - Checks the current time and creates an alarms text file
- **init_time_check_thread()**
    - Initializes a new thread for checking the time

### api.py
Module that contains functions related to handling the Philips Hue API.

- **set_light_color(color_hex)**
    - Converts hex to xy, then sets color & turns on light
- **light_off()**
    - Turns off the light

### tests.py
Module that contains unit test functions for hex and time validations.

- **test_hex_validation()**
    - Tests for hex color validation
- **test_validate_time()**
    - Tests for time validation

### requirements.txt
Required Python modules from pip
- **pytest**
- **requests**

Philips Hue rgbxy converter library from benknight:
- https://github.com/benknight/hue-python-rgb-converter



# Future Plans:
(ran out of time to finish)
- Add timer option and preset timers
- Add "bother boyfriend" preset option
    - Immediately turns on/sends API call to designated light
- Include template version and instructions for other people to also use, if they want to
- Clean up code style/documentation
- Enable quick access options via keypress on macropad/keyboard
    - My end goal is to press keys to start preset timers
- See if possible for colors to alternate when alarms are activate simultaneously



# Extra Credit (*optional*)

No coding backgroud prior to this quarter. However, I'm taking COGS 18 and CSE 11 (Java) simultaneously, so I'm familiar with the basic programming topics covered in that class as well (but in the context of Java instead of Python). Other than that, the closet thing I had to coding familiarity was my fondness for excel spreadsheets.


- **docstrings/code style**
    - Researched docstrings further to try implementing as as much good code style as I can in my code. I'm still a little unsure about my implementation and I wasn't comletely sure how to incorporate my references, but I tried to make it look nice and understandable. 
    (Feedback on this part would be really appreciated, I'm still not compeltely comfortable with code style)

- **APIs**
    - Researched how to do API calls in a Python environment.
    - Research **requests library** while learning to do API calls.
    - Reseached how the Philips Hue API functions. 
    - Executed API calls in my modules to interact with/update my light's settings

- **threading**
    - Researched and learned how to use threading to launch/run concurrent processes.
    - Learned the difference between standard thread and daemon threads.
    - Incorporated threading in my code.

- **libraries**
    - Researched the **os library** and how to use the os file structure, while learning threading. 
    - Researched the **datatime library** to learn how to how to use the current time in my code.
    - Researched the **time library** to learn how to count by seconds, so I could wait 1 second before checking the current time and continue checking the time every second.
    - Researched and learned how to use the **json library** to import and export json data to and from files, in order to save my alarms.

- **f strings**
    - Learned how f strings work and incorporated them into my modules.

- **switch**
    - Learned how to implement an equivalent to switch statements in Python. 
    (I was already aware of switch statements from Java)

