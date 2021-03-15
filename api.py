
# APIs: https://realpython.com/python-api/
# Philips Hue API: https://developers.meethue.com/develop/get-started-2/
# Philips Hue CLIP API Debugger: https://192.168.86.32/debug/clip.html
# Philips Hue rgbxy converter library from benknight: https://github.com/benknight/hue-python-rgb-converter
# Requests library: https://realpython.com/python-requests/
# f strings: https://realpython.com/python-f-strings/


from rgbxy import Converter
import requests
import json
from secret import bridge_ip, api_key

base_url = f"http://{bridge_ip}/api/{api_key}"
light5_state = f"{base_url}/lights/5/state"

# Turn on light
def light_on():
    
    on_param = {"on": True}
    response = requests.put(light5_state, data = json.dumps(on_param))


# Turn off light
def light_off():
    
    off_param = {"on": False}
    response = requests.put(light5_state, data = json.dumps(off_param))



