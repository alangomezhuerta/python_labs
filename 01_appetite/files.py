#!/usr/bin/env python3

f = open("/pantheon/workspace/python_labs/01_appetite/text.txt","r")
while True:
    linea = f.readline()
    if not linea: break
    print(linea)

