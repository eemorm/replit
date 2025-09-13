print ("Priscilla\n")
input(">>>")

name = input ("What is your name? ")

print ("\nYou spot in a tree what looks like a carrier pigeon but you know it is extinct. You take out a pair of binoculars and see that it really is a carrier pigeon. You get a ladder out and climb up it to get in the tree and try to capture the bird to see if it is a carrier pigeon and to also see if it's hurt. You get up there and see that it is hurt so you take off your sweatshirt and carefully catch it with that. But as you go down the ladder with the bird, you notice a big gray circle in the sky. As you watch the circle, it gets smaller and smaller; and you begin to think it's closing! You begin to form a theory: Maybe the bird since it was extinct for a century; that that is a portal goes back a century and the bird came from that time through the portal. You grab your phone, take a picture of the bird, and post it on your bird classification app and it comes up as a carrier pigeon. You look up at the circle again and you watch it as it gets smaller and smaller and then it completely disappears. Every day you went outside and tried to find the circle but it wasn't there until 3 days later it appeared again.\n")
input(">>>")

print ("This is where your journey begins,", name + ("."))
input(">>>")



choices_dict = {
  "1":"Care for the Bird",
  "2":"Investigate the Circle"
}

results_dict = {
  "1":"\nYou get the bird and make it a living space. You also give it water and food bowls.",
  "2":"\nYou run into the forest and climb up the closest tree. You put your hand through the circle and your hand disappears. Weird..."
}

available_choices = ["1","2"]
def print_available_choices(available_choices, choices_dict):
  print("\nChoices:\n")
  for c in available_choices:
    print(f"     {c}) {choices_dict[c]}")

while available_choices:
  print_available_choices(available_choices, choices_dict)
  choice = input("")

  if choice in available_choices:
    print(results_dict[choice])
    #remove the option from the available
    available_choices.pop(available_choices.index(choice))
  else:
    continue

input(">>>")

print ("\nYou begin to wonder about the circle so you take off your sunglasses and throw them through the circle. You totally believe now that your theory is correct.\n")

input(">>>")

print ("You saw that the circle was there every 3 days so you think that you could go through the portal to the other time (or place) and explore for 3 days and then return.")

input(">>>")

choices_dict = {
  "1":"Water",
  "2":"Food",
  "3":"Knife",
  "4":"Lighter",
  "5":"Sleeping Bag",
}

results_dict = {
  "1":"\nYou get some water.",
  "2":"\nYou get some food.",
  "3":"\nYou get a knife.",
  "4":"\nYou get a lighter.",
  "5":"\nYou get a sleeping bag."
}

available_choices = ["1","2","3","4","5"]
def print_available_choices(available_choices, choices_dict):
  print("\nMaterial Choices:\n")
  for c in available_choices:
    print(f"     {c}) {choices_dict[c]}")

while available_choices:
  print_available_choices(available_choices, choices_dict)
  choice = input("")

  if choice in available_choices:
    print(results_dict[choice])
    #remove the option from the available
    available_choices.pop(available_choices.index(choice))
  else:
    continue

input(">>>")

print ("\nYou go into the forest, all ready, climb up the closest tree to the portal, and you grab onto a invisible tree through the portal and pull yourself through.\n")

input(">>>")

print("Your eyes flutter open, and the sky is dark and fluid. There is a sign up ahead that says 'The Gloomy Zone'. ")

