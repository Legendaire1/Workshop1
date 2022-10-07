# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

# Version 1: added random element to printing message on website, once app.py is called
# within the terminal, it designates a specific element the website stays the same even with reloads
# Next goal: Can we update the website with just reloading instead of calling the file within the terminal?

from flask import Flask
import random

app = Flask(__name__) #create instance of class Flask

list = ["Jeffrey", "Kevin", "Vivian"]

occupation = random.choice(list)

@app.route("/")       #assign fxn to route
def hello_world():
    return occupation

app.run()

