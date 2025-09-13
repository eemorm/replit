import sys
import time
import os

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write(
            "%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size - x), j, count))
        file.flush()

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()


for i in progressbar(range(100), "Building World: ", 30):
    time.sleep(0.02)
os.system('clear')
for i in progressbar(range(100), "Getting Items: ", 30):
    time.sleep(0.09)
os.system('clear')
for i in progressbar(range(100), "Spawning Enemies: ", 20):
    time.sleep(0.04)
os.system('clear')
for i in progressbar(range(100), "Loading: ", 20):
    time.sleep(0.01)
print("\n\nOperations Complete.")
time.sleep(3)
os.system('clear')

import csv
import sys

def main():
   menu()


def menu():
    print("Holo")
    print()

    choice = input("""
                      A: New Game
                      B: Save Slots

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        new_game()
    elif choice == "B" or choice =="b":
        save_slots()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def new_game():
   choice = input ('1: Save Slot 1')
  
   if choice == "1":
      import holo

    
def save_slots():
   pass

main()
