#pi= 3.1416

#print ("este es pi: ", pi)

#npi= math.floor(pi)
#print("este es pi redondeado para abajo", npi)

#upi= math.ceil(pi)
#print("Este es pi redondeado para arriba", upi)
###--------import---------####
import random
import math



####-------Funciones-------####
def rng( a,b):
    return random.randint(0,100)
def maximocomoundivisor(a,b):
    return math.floor(a/b)
def maxicomodiv(a, b):
    return math.gcd(a,b)
def factorial(n):
    producto= 1
    for i in range(1, n + 1):
        producto = producto* i
    return producto 

####------Practica 1-------####
nr = rng(1,100)
print (nr)
####------Practica 2-------####





####------Practica 3-------####