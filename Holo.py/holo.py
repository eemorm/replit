import os

done = False
state = 'WCP1'
while not done:
    if state == "WCP1":
      question = 'You look around and see that you are on a sheer cliff and a sign says The Overlook.'
      answers = ['look at the sign']
      results = [
        'You look at the sign and it says in small letters at the bottom: Get to the Safe.'
      ]
      next_states = ['WCP2']
