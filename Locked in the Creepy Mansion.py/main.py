import time

print ("Locked in the Creepy Mansion\n")
time.sleep(2)

name = input ("What is your name? ")

print (name + ("."), "That is a nice name.\n")
time.sleep(2)

print ("Emma and James were playing soccer in James' yard. James was")
print ("winning. So Emma thought: 'I need to kick it really hard.'")
print ("And then 'Bam!' Emma hit the ball into the woods. Now you have")
print ("to take over as James or Emma.\n")

player = ""
answers = ("Emma", "James")
while(True):
  if player in answers:
    break;
  player = input ("Who? ")

print ("Good choice,", name + (".\n"))

print ("With no other choice, you both run into the forest to try to")
print ("retrieve the ball.")
time.sleep(2)

print ("\nYou Find...")
time.sleep(2)
print ("...not the ball but a...")
time.sleep(3)
print ("...MANSION!!!\n")
time.sleep(2)

print ("You are persuaded to go in so you go in. Then you")
print ("hear a little 'click'...\n")
time.sleep(2)
print ("YOU HAVE BEEN LOCKED IN!!!\n")
time.sleep(2)

print ("You give the idea of checking the floors for open windows.\n")
time.sleep(2)

print ("You walk around the 1st floor and check all the windows but all of them are locked.\n")
time.sleep(3)

print ("You walk around the 2nd floor and check all the windows but all of them are locked.")
time.sleep(3)
