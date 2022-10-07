# GGG Rendition #2: Vivian Graeber, Jeffrey Zou, Kevin Xiao + Squishy, Like, FamousMrTable
# SoftDev
# Oct 2022

# Version 3 : we are now testing

import random
from flask import Flask


def build_dict(input: str) -> dict[str, float]:
    temp_dict: dict[str] = {}
    with open(input, 'r') as f:
        lines: list[str] = f.readlines()

    for i in range(1, len(lines)-1):
        line: str = lines[i].strip() # strip the newline of the end of each line
        line: list[str] = line.rsplit(',', 1) 
        
        occupation: str = line[0].strip('\"')
        percentage: float = float(line[1])
        
        temp_dict[occupation] = percentage

    return temp_dict

def pick_rand_weighted(input: dict[str, float]) -> str:
    occupations: list[str] = list(input.keys())
    percentages: list[float] = list(input.values())
    occupation: str = random.choices(occupations, weights=percentages, k=1)[0] # weights are not correct
    return occupation


app = Flask(__name__) # ...

@app.route("/") # ...
def hello_world():
    print(__name__) # ...
    krewes: dict[str, float] = build_dict("occupations.csv")
    print(krewes)

    occupation: str = pick_rand_weighted(krewes)
    print(occupation)

    newstring = ''
    for i in krewes:
        newstring = newstring + i + " <br>"
    
    result = 'GGG Rendition #2: Kevin Xiao + FamousMrTable, Jeffrey Zou + Like, Vivian Graeber + Squishy <br> <br> ' + ' Random occupation: ' + occupation + ' <br> <br> ' + newstring
    return result # ...

app.run()  # ...
                
