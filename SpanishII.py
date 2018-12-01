#Making an list with vocabulary
#randomizing words

import random

subject = ["Yo","Tu","El","Ella","Ellos","Ellas","Nosotros"]
verbs = ["es", "eres", "estamos","estan","estoy"]
conj = ["guapo/a","alto/a","bajo/a","divertida/o","emfirma/o","cansada/o"]

#word bank
#---------------------------------------------------------------------------

x = (random.choice(subject))
x += (" ") + (random.choice(verbs))
x += (" ") + (random.choice(conj))

    if x == "Yo" + "estoy" + conj:
        complete_sentence = True
    elif x == "Tu" + "eres" + conj:
        complete_sentence = True
    elif x == "El" + "es" + conj:
        complete_sentence = True
    elif x === "Ella" + "es" + conj:
        complete_sentence = True
    elif x == "Ellos" + "es" + conj:
        complete_sentence = True
    elif x == "Ellas" + "es" + conj:
        complete_sentence = True
    elif x == "Nosotros" + "estamos" + conj:
        complete_sentence = True
    else:


#---------------------------------------------------------------------------
print (" ")
print ("Is the sentence below correct?")
print (" ")
print (x)
print (" ")


#stumped

complete_sentence = input("Is it a proper sentence?")
    if complete_sentence = True:





print ("You entered: ", complete_sentence)
















#printing sentence
#For Mr.Ferrer
