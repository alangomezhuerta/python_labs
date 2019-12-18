#!/usr/bin/env python3

a = 0
b = 1
c = 0
while c < 100:
    c = a + b
    print(c)
    a = b
    b = c
