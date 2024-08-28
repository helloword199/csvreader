import pandas as pd
from enum import Enum
from colorama import Fore, Back, Style,init
import os
import random

init(autoreset=True)

colors=foreground_colors =  [
    Fore.BLACK,
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE
]



rand= random.choice(colors)

def Clear():
    os.system('cls')


class SelectionCvs(Enum):
    carsCsv = 1
    animalsCsv = 2
    cakesCsv = 3
    EXIT = 4

class OptionOfRead(Enum):
    INFO = 1
    HEAD = 2
    TAILL = 3



def ReadAndPrint(file):
    while True:
        Clear()
        for i in OptionOfRead:
            print(rand + f"[{i.value}] - {i.name}")
        selection = int(input(rand + "Enter Your Choice: "))

        df = pd.read_csv(file)

        if selection == OptionOfRead.INFO.value:
            df.info()
        elif selection == OptionOfRead.HEAD.value:
            print(df.head(2))
        elif selection == OptionOfRead.TAILL.value:
            print(df.tail(2))
        else:
            print(rand +"Invalid option. Please try again.")
            continue

        user_continue = input(rand + "[1] to stay in this file, [2] back to menu: ")

        if user_continue == "1":
            continue  
        elif user_continue == "2":
            Manu()
            break  
            
        else:
            print(rand +"Invalid input. Returning to menu.")
            continue





def Manu():
    while True:
        Clear()
        for i in SelectionCvs: print(rand + f"[{i.value}] - {i.name}")

        user_input = int(input(rand + "Enter Your Choice: "))

        if user_input == SelectionCvs.carsCsv.value:ReadAndPrint('cars.csv') 

        elif user_input == SelectionCvs.cakesCsv.value: ReadAndPrint('cakes.csv')

        elif user_input == SelectionCvs.animalsCsv.value: ReadAndPrint('animals.csv')

        elif user_input == SelectionCvs.EXIT.value:  exit()  
        else:
            print(rand + "Invalid selection. Please try again.")
            continue



Manu()

