#Files
import settings as s
import utils
# Libraries
import pyautogui as gui
from time import sleep

def error(message):
    print(message)
    gui.alert(message, "Error")
    raise Exception(message)
