#!/usr/bin/env python3
# some loops

counter = 0
element = ""
mylist = [ "element01", "element02", "element03", "element04", "element05", "element06"  ]
for i in mylist[1::]:
   counter += 1
   element = i + "_" + str(counter)
   print(element)


# --
for x in range(2, 15, 2):
   print(x)

# --
for i in mylist[:]:
   # print(mylist[i])
   print(i)
   mylist.pop()
   print(mylist)
