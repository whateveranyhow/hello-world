from sys import exit

def guess():
  print "give me a word, you have ten times to guess, or you loss"

  action = raw_input(">")
  guesses = 0

  while action !="yes" and guesses < 9:
      print "try again"
      guesses += 1
      action = raw_input(">")

  if action == "yes": #good
     print "you win"
     exit()

  else:
      print "you loss"
      exit()

guess()
