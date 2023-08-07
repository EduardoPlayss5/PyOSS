import os
import time
import atexit
import colorama
from colorama import Fore, Back, Style

colorama.init()

def reset_style_on_exit():
    print(Style.RESET_ALL)

atexit.register(reset_style_on_exit)

def display(error):
    getted_err = str(error)
    print(Fore.LIGHTWHITE_EX + Back.RED)
    print("*********************************************")
    print("*                                           *")
    print("*                  ERROR                    *")
    print("*                                           *")
    print("*********************************************")
    print("\n")
    print(Fore.LIGHTRED_EX + Back.BLACK + "The PyOSS found a error and shutted down to prevent from")
    print('demage.')
    print()
    print(f"Error code: {getted_err}")
    print("We' will restart to you in 5 secs")
    print(Style.RESET_ALL)
    time.sleep(5)