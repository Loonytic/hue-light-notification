"""Module contains functions related to handling the Philips Hue API.

Turns lights on/off and sets alarm colors.
Imports variables from secret file, for security purposes. 

Functions
---------
set_light_color(color_hex)
    Converts hex to xy, then sets color & turns on light
light_off()
    Turns off the light

References
----------
APIs: 
    https://realpython.com/python-api/
Philips Hue API: 
    https://developers.meethue.com/develop/get-started-2/
Philips Hue CLIP API Debugger: 
    https://192.168.86.32/debug/clip.html
Philips Hue rgbxy converter library from benknight: 
    https://github.com/benknight/hue-python-rgb-converter
requests library: 
    https://realpython.com/python-requests/
f strings: 
    https://realpython.com/python-f-strings/
import variables: 
    https://codeburst.io/importing-variables-from-other-files-in-python-96a200f410da
"""

import json

import requests
from rgbxy import Converter

from alarm_module.secret import bridge_ip
from alarm_module.secret import api_key

base_url = f"http://{bridge_ip}/api/{api_key}"
light5_state = f"{base_url}/lights/5/state"


def set_light_color(color_hex):
    """Converts hex to xy, then sets color & turns on light.
    
    Converts a hex color number to a xy color number,
    then sets the color and turns the light on.
    
    Parameters
    ----------
    color_hex : string
        String to convert to tuple.
    """

    convert = Converter()
    color_xy = convert.hex_to_xy(color_hex)

    color_param = {'xy': color_xy, "on": True}
    response = requests.put(light5_state, data = json.dumps(color_param))


def light_off():
    """Turns off the light."""

    off_param = {"on": False}
    response = requests.put(light5_state, data = json.dumps(off_param))
