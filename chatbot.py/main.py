chatme1 = "hi"
chatme2 = "hello"
chatme3 = "how are you"
chatme4 = "good"
chatme5 = "can we play minecraft"
chatme6 = "can we play fortnite"
chatme7 = "bye"
chatme8 = "hey"
chatme9 = "what is your name"
chatme10 = "how old are you"
chatme11 = "can we play a game"
chatme12 = "should i fix lunch"
chatme13 = "should i go to the store"
chatme14 = "should i watch tv"
chatme15 = "dont forget to charge yourself"
chatme16 = "im tired"
chatme17 = "i need help"
 
for i in range(1000000):
  chatask = input ("")

  if chatask in chatme1:
    print ("Hi!")
  elif chatask in chatme2:
    print ("Hello!")
  elif chatask in chatme3:
    print ("I am fine. How are you?")
  elif chatask in chatme4:
    print ("Great!")
  elif chatask in chatme5:
    print ("Ok! But maybe later we can play Fornite.")
  elif chatask in chatme6:
    print ("Ok! But maybe later we can play Minecraft.")
  elif chatask in chatme7:
    print ("Bye! See you tomorrow!")
  elif chatask in chatme8:
    print ("Hey!")
  elif chatask in chatme9:
    print ("My name is Lexa.")
  elif chatask in chatme10:
    print ("I am 20 years old.")
  elif chatask in chatme11:
    print ("I can't play a game with you. Sorry!")
  elif chatask in chatme12:
    print ("Certaintly!")
  elif chatask in chatme13:
    print ("If you need to!")
  elif chatask in chatme14:
    print ("If you want to. Well, you are you...")
  elif chatask in chatme15:
    print ("I won't!")
  elif chatask in chatme16:
    print ("Go drink water, go eat a Tylenol, go take a nap, go to bed!")
  elif chatask in chatme17:
    print ("Umm, I don't know how to help you with what you need help with. For more help, go to Counseler.")
  else:
    print ("I do not know how to respond.")
