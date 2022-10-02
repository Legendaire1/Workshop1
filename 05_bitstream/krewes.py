"""
Jasmine Yuen & Jeffrey Zou (Temporary Ducks)
SoftDev
K05 -- Writing a Python program to read a .txt file and populate
a dictionary. Then randomly select a Devo and print the information.
2022-09-29
time spent: 1

DISCO: We learned how to append to a dictionary and read from a .txt file.
QCC: NONE

PROCESS:
1. import random library
2. initialize a krewes dictionary
3. read the .txt file into a string format
4. split the string into each person by .split("@@@")
5. split the string into each person's attributes by .split("$$$")
6. initialize each distinct period as a dictionary key
7. append the elements of each person into their respective dictionary lists
8. choose random person
9. print 
"""

import random

krewes = {}

f = open("test.txt", "r")
s = f.read()
f.close()

ary = s.split("@@@")

# grabbing all the different periods from the array and putting the key into krewes
for i in range(len(ary)):
    ary[i] = ary[i].split("$$$")
    if ary[i][0] not in krewes:
        krewes[ary[i][0]] = []

# appending each person to their specified key
for i in ary:
    krewes[i[0]].append([i[1], i[2]])

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol}")
