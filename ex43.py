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


# only while
a = '3'
action = raw_input(">")
while a != action:
    print "try a gain"
    action = raw_input(">")

print "goodbye!"

# get data from class to class by using variable as a parameter.
from random import randint
class Cat(object):
    def __init__(self, name):
        self.name = name

    def copy(self):
        waht_it_has = self.name.guess()  # some parameter/variable gets other's function.

class Dog(object):

    senten = [
        "It has four leg.",
        "It has two eyes.",
        "It has fur.",
    ]
    def __init__(self, name):
        self.name = name

    def guess(self):
        print Dog.senten[randint(0, len(self.senten)-1)]

name1 = Dog("Nancy")
name2 = Cat(name1)
name2.copy()
