import math

a = -10//3
b = -10%3
print(a)
print(b)

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
    
print("--------- Definition ---------")
print(f"Die Ganzahldivision ergibt: {ganz_zahldivision(-10,3)} \nDie Modulo-division ergibt: {modulo_division(-10,3)}")