import math
# Aufgabe 1
print("--------- Aufgabe 1: ---------")
a = -10//3
b = -10%3
print(a)
print(b)

# Aufgabe 2
print("--------- Aufgabe 2: ---------")
def betrag(a):
    if a < 0:
        a *= -1
    return(a)

def ganz_zahldivision(a,b):
    c = a / b
    if c < 0:
        c = math.ceil(c)
    else:
        c = math.floor(c)
    return c

def modulo_division(a,b):
    return(a-ganz_zahldivision(a,b)*b)
    
print(f"Die Ganzahldivision ergibt: {ganz_zahldivision(-10,3)} \nDie Modulo-division ergibt: {modulo_division(-10,3)}")

# Aufgabe 3
print("--------- Aufgabe 3: ---------")

for i in range(1,5):
    print("*" * i)

print("--------- Einzeiler ---------")

print("\n".join(["*"*i for i in range(1,5)]))


# Aufgabe 4
print("--------- Aufgabe 4: ---------")

liste = list(map(int, input("Nummern mit Leerzeichen getrennt eingeben: ").split()))
print(sum(liste) / len(liste))