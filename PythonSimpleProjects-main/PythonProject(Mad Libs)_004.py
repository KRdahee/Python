#String concatenation (How to put Strings together)
#Suppose we want to create a string that says "subscribe to _____"

#youtuber = "" #문자열변수

#몇가지 방법

#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Abjective: ")
verb1 = input("Verb:")
verb2 = input("Verb:")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. something something {verb2} like something something {famous_person}!"

print(madlib)




#or random_madlibs

import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()