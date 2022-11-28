#File name: reconstructSEntance.py
#CPE 422 HW11 Rachel Durland

import sys

def checkline():
    global i
    global wordcount
    global w
    w = i.split()
    wordcount += len(w)
        

wordcount = 0
f = open(sys.argv[1])
flines = f.readlines()
linecount = len(flines)
list1 = []
for i in flines:
    checkline()
    list1 += w
f1count = wordcount
print("list one is:",list1)
wordcount = 0

f = open(sys.argv[2])
flines = f.readlines()
linecount = len(flines)
list2 = []
for i in flines:
    checkline()
    list2 += w
f2count = wordcount
print("list 2 is:",list2)


f3 = open("output.txt","w")
out = []

while(list1 != []) and (list2 != []):
    if (list1 != []):
        x = list1.pop()
        out.append(x)
        f1count = f1count - 1
    if (list2 != []):
        y = list2.pop()
        out.append(y)
        f2count = f2count - 1

print("list out is:",out)

z = len(out)
i = 0
for i in range(0,z):
    f3.write(out[i])

