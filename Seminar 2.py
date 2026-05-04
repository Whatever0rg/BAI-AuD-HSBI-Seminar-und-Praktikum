import random
# Augabe 1
print("--------- Aufgabe 1: ---------")

liste = [x for x in range(0,random.randint(0,20))]
print(liste)

for i in range(len(liste)):
    rand = random.randint(0,len(liste)-1)
    liste[i], liste[rand] = liste[rand], liste[i]
print(liste)

# Augabe 2
print("--------- Aufgabe 2: ---------")