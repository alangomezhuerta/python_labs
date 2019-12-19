#!/usr/bin/env python3
# and now the turn of some collections

# Tuples
# Tuples are inmutable once they are created
T = (2, 3, "hola", 3)
print(T[2:])

# Lists
# They can be modified after created

# L = [ 2, 3, "uno", x for x in range(100,200,10), "adios"]
L1 = [ 2, 3, 5, "hola"]
L2 = [ x for x in range(5)]
print(L1)
print(L2)

# L3 = L1.extend(L2.extend(x for x in range(10,15)))
L3 = L1.extend(L2)
print(L3)
print(L1)
L4 = L1
print(L4)

L4.extend([x for x in range(500,100,-100)])
print(L4)

# --
TN = 1, 5, 6, "salud"
print(TN.index(5))

a, b, c = 2, 5, 6
print(a)
a, b, c, d = TN
print(a)

# --
# The very powerful slicing
print("Pruebas con slicing")
L5 = [ "a1", "a2", "a3", "a4", "a5", "a6"  ]
L4 = []
L4 = [ 33, 32, 31, 30 ]
L4A= L4B = L4

# Para el siguiente ejemplo:  L4A[2:3] = L5   Se debería explicar como sigue:
# " lo que antes se encontraba desde la casilla 2 y hasta antes de llegar a la 3"
# " reemplazarlo todo e insertar ahí los elementos de la lista L5"
L4A[2:3] = L5
L4B[2:6] = L5

print("This is L4", L4)
print("This is L5", L5)

print("This is L4A", L4A )
print("This is L4B", L4B )

# -- "
# Dictionaries
# There0s a very useful function ( dict() ), that you can use to generate dictionaries
d1 = dict(one=1,dos=2,tres=3)
d2 = { "lunes":10, "martes":11, "miercoles":23}
# print(d1["dos"])
# print(d2["martes"])

print("hola mundo")
d3 = dict(enero=1,febrero=2)

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)

d1.pop("dos")
print(d1)

d1["docientos"] = 200
print(d1)


# -- Strings
S = "hola Mundo de python"
print(S.find("p"))
print(S.split(" "))

# --
# Sets

a = set([1,2,3,4,2,3,4,2,3,1,5,3,6,4])
print(a)

a = set(S)
print(a)
print(len(a))

a = (1,1,1,1,0)
c = all(a)
print(c)

zip