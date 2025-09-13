import time
import os
import random

algorithm = "10936"
ai = "38744"

character = input ("Character Code: ")

if character in algorithm:
  print ("\nAlgorithm: Ready for Battle!")
  time.sleep(3)
  os.system('clear')
elif character in ai:
  print ("\nAI: Ready for Battle!")
  time.sleep(3)
  os.system('clear')
else:
  print ("\nAlgorithm: There is no other choice!")
