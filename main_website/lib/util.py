import random
import datetime
import string
import colorama
import json
import platform
import os
import re
import time
from os import system,name
from colorama import Fore


# region global variables
colorama.init(autoreset=True)


# for the coloring the console for debugging
success = Fore.GREEN
warning = Fore.YELLOW
error   = Fore.RED


COMMANDS = {
    "pip-linux"      : "python3 -m pip install --upgrade pip",
    "pip-windows"    : "python -m pip install --upgrade pip",
    "update-package" : "pip-review --auto", #<=======================> this is an external package for updating the packages
    "check-package"  : "pip-check", #<===============================> this is an external package for checking what needs to be updated
    "windows-cls"    : "cls",
    "linux-cls"      : "clear",
}


OS_SUPPORTED = {
    "mac"     : "Darwin",
    "linux"   : "Linux",
    "windows" : "Windows"
}


def get_time():  # * get full 12 hour time
    return f'{datetime.datetime.now().strftime("%I")} : {datetime.datetime.now().strftime("%M")} {datetime.datetime.now().strftime("%p")}'


def get_Date():  # * get full date
    return datetime.datetime.now().strftime("%x")


def getMonth(): # * full name of month
    return datetime.datetime.now().strftime("%B")


def getMonthDay(): # * get the day of the month
    return datetime.datetime.now().strftime("%d")


def getWeekDay(): # * get fullname of the weekday
    return datetime.datetime.now().strftime("%A")


def generateAPIKey(Size):  # * generating the random api key and saving it with each user
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(Size))


def log(title, data, writeType="w"): #  loging the errors in a text file
    f = open(f"../logs/{title} - {get_Date()}.txt", writeType)
    f.write(f"\n\n{data}\n * {get_time()} - {getWeekDay()}\n\n")
    f.close()


def openJson(title, json_usage='r'): # * opening json file
    with open(f'{title}.json', json_usage) as f:
        return json.load(f)


def writeJson(title, data={}, writeType='w', indents=4):
    # w for write. a whole new file,
    # a for appending to the end
    with open(f'{title}.json', writeType) as f:
        json.dump(data, f, indent=indents)


def rnd(max):  # * random number generator default min = 1
    return random.randint(1, max)


def rnd(min, max):  # * random number generator between min and max
    return random.randint(min, max)


def evenRnd(min, max, step=2): # generating random even numbers
    return random.randint(min, max, step)


def oddRnd(min, max, step=3): # generating random odd numbers
    return random.randint(min, max, step)


def cls():  # * clear the console
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def getPcDevOs(): # getting the os that the pythong script is run_terminal_command on 
    return platform.system()


def run_terminal_command(command): # runTerminalCommand terminal commands
    os.system(command)


def update_packages(): # auto updater to be used in development
    """
        TODO: delete this if it's not needed in a near future
        # run_terminal_command("clear")
        # run_terminal_command("ipconfig getifaddr en0")
        # run_terminal_command(commands["act-mac-linux"])
        # run_terminal_command("cls")
        # run_terminal_command("ipconfig")
        # run_terminal_command(commands["act-windows"])
    """
    try:
        if getPcDevOs() == OS_SUPPORTED['linux'] or getPcDevOs() == OS_SUPPORTED['mac']:
            run_terminal_command(COMMANDS["pip-linux"])
            run_terminal_command(COMMANDS["check-package"]) # checking first what needs to be updated
            print(f"These packages need to be updated, to cancel press\n{getPcDevOs()} --> CTRL + C")
            time.sleep(1000) 
            run_terminal_command(COMMANDS["update-package"])

        elif getPcDevOs() == OS_SUPPORTED['windows']:
            run_terminal_command(COMMANDS["pip-windows"])
            run_terminal_command(COMMANDS["check-package"]) # checking first what needs to be updated
            print(f"These packages need to be updated, to cancel press\n{getPcDevOs()} --> CTRL + C")
            time.sleep(1000) 
            run_terminal_command(COMMANDS["update-package"])

        else:
            print("Unables to get os")
        
    except Exception as e:
        log("update-packages", str(e))
        print(f" * {error}error: {str(e)}")


def aboveBellow(compare, myList=[]): # get's how many numbers in the list are above and bellow the compare
    above   = 0
    bellow  = 0
      
    for i in myList:
      if i < compare:
        bellow += 1

      elif i > compare:
        above += 1

      else:
        return ("this else statement should not reach here.\nIn theory\nif it does. sorry")

    # wanted to get fancy. un coment this for it to be written in a file
    # self.write(      
    #   {
    #     "above": above,
    #     "bellow": bellow
    #   }
    # )

    return json.dumps(
      {
        "above": above,
        "bellow": bellow
      }
    )


def rotateRight(data, rotateTimes): # rotate string char to the right rotateTimes times
    return data[-rotateTimes:] + data[:-rotateTimes]


def addStrings(string_A, string_B): # adding 2 strings and returning it
    return str(string_A + ' + ' + string_B)

def split(str_A): # spliting a string and returning the list
    return str_A.split(' + ')


def sort(arr=[]): # returns sorted list or aka array
    return sorted(arr)


def search(Search,arr=[]): # returning true or false if Search is found in arr
    return Search in arr


def search(Search,In): # returning true or false if Search is found in In
    return Search in In


def valEmail(email): # validating if the email is valid or not
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False