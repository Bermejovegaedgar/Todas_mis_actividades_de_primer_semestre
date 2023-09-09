
#1. Crea un programa que lea un número del teclado e imprima la suma de 0 a ese numero.
def sumaLineal(n):
    acum = 0
    for i in range (n + 1):
        acum += i
número=float(input("Selecciona un número: "))
print(sumaLineal(número))
#2-----------------------------------------------------
Lista1 = []
while(True):
    nu = int(input())
    print("el usuario introdujo: ", nu)
    Lista1.append(nu)
    if (nu == 0):
        print("bye")
        break
print(sum(Lista1)/len(Lista1))

#6. Crea una función que reciba un número y regrese un booleano indicando si es divisible entre 243
n = float(input("Selecciona un número: "))
mulstr = (input("di algo: "))
print(mulstr*n)


#12(Challenge) Imprime una pirámide
ndecol = int(input("Selecciona el numero de filas: "))
if ndecol == 1:
    print(1)

elif ndecol ==2:
    print(1)
    print(1,2)

elif ndecol ==3:
    print(1)
    print(1,2)
    print(1,2,3)

elif ndecol ==4:
    print(1)
    print(1,2)
    print(1,2,3)
    print(1,2,3,4)

elif ndecol ==5:
    print(1)
    print(1,2)
    print(1,2,3)
    print(1,2,3,4)
    print(1,2,3,4,5)

elif ndecol >5:
    print("muchas columnas acomodadas y asi...")

#3. Crea un programa que cree una lista de compras. Primero le pide al usuario que ingrese 
#la cantidad n de artículos. Luego lee n artículos de la terminal. Una vez leídos todos,
#imprime la lista en orden alfabético.


na = int(input("Cantidad de articulos: "))
lista=[]
for i in range(na):
    super=(input("Ingresar tu lista: "))
lista.append(super)
lista.sort()
print(lista)

#-------------------------------------------
nd = int(input())

npares = []

for i in range(nd):
    valor = int(input())
    if valor % 2 ==0:
        npares.append
    print(npares)

#------------------------------------------
def esvocal(c):
    vocales = "aeiouAEIOU"

    return c in vocales
lectura = input("por favor da una letra")
for caracter in lectura:
    print(caracter)

#------------------------------------------
m = int(input("dame un vlor: "))
print(n % 243 == 0)

#------------------------------------------

def funcion(a,b,c):
    if (a > 100 or b > 100 or c > 100):
        print(a + b + c)
    else:
        print(a * b * c)
#------------------------------------------

def espalindromo(str):
    return str[::-1] == str
print(espalindromo("KayaK"))

#--------------Reto 12 bien hecho----------

ma = int(input())

for i in range (1,ma +1):

    for j in range (1,i +1):
        print(j, end=",")
#------------------matriz-------------------------

lista3 = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]]

#print(lista[2][3])

for d in range(len(lista3)):
    for e in range(len(lista3[i])):
        print(lista[i][j], end= ' ')
    print()