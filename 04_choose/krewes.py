"""
Jeffrey Zou Ivan Yeung
SoftDev
K01
Krewes/Python dictionary/We are trying to write a python program that randomly selects a devo from a dictionary
9/22/2022
Time spent:
BlOCK SUMMARY:
DISCO:
QCC:
OPS SUMMARY:"""
 
import random as rng
krewes = {2:["devo1","devo2","devo3"], 7:["devo1","devo2","devo3"], 8:["devo1","devo2","devo3"]}
list = [2,7,8]
key = rng.choice(list)
dictionarylist = krewes[key]
 
 
 
