import sys
import time

message = "\nHello, world. This message can run at different speeds and you can see which one you like the best."

choice = input("Which speed do you want? \n\n 1. 0.1 second \n 2. 0.05 second \n 3. 0.02 second \n 4. 0.01 \n\n>>>")

if choice == "1":
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
if choice == "2":
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
if choice == "3":
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)
if choice == "4":
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
