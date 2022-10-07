# GGG Rendition #2: Vivian Graeber, Jeffrey Zou, Kevin Xiao + Squishy, Like, FamousMrTable
# SoftDev
# Oct 2022

#version 2: we successfully added the occupations csv file and implemented it into our code,
# we are now able to randomly choose an occupation from the csv file and update it within our website

#Disco: With our build_dict fxn, we are able to update the website by reloading it, instead of having to call repeatedly within the terminal.


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
    return occupation  # ...

app.run()  # ...
                