#!/usr/bin/env python3
# conditionals
a = 5 == 4
a = 5 > 3
a = 5 != 0
print("ksldkldkdldk")
print(str(a))
print("Thanks")

# --
if a < 10:
    print("Still under 10")
elif a == 10:
    print("justo es 10")
else:
    print("arriba de 10")

# --
while True:
    entrada = input("> ")
    if entrada == "adios":
        break
    else:
        print(str(entrada))

# --
words = [ "a1", ]

while True:
    a += 1
    print(str(a))
    if a == 10: break
else:
    print("ya paso de 10")