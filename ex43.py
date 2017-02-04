# while-and-if-else /guess
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



# if-elif-else /guess
from sys import exit
def guess():
    print "give me a word, 1 will be bad and 1 good, else is back"

    action = raw_input(">")

    if action == "yes": #good
        print "you win"
        exit()

    elif action == "no": #bad
        print "you loss"
        exit()

    else:
        print "back again"
        return guess()

guess()



# randint
from random import randint

a = [1,2,3,5,3,6,2,8]
#print len(a)
print a[randint(0, len(a)-1)]
