#Making an list with vocabulary
#randomizing words

import random

subject = ["Yo","Tu","El","Ella","Ellos","Ellas","Nosotros"]
verbs = ["es", "eres", "estamos","eres","estan"]
conj = ["guapo","blanco","negro","divertida","feo","cansada"]

#word bank

x = (random.choice(subject))
x += (" ") + (random.choice(verbs))
x += (" ") + (random.choice(conj))

#making sentence

print (" ")
print ("Is the sentence below correct?")
print (" ")
print (x)

#printing sentence
#For Mr.Ferrer

print ("I'm not able to make it say yes or no yet.")
