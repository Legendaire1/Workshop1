# GGG Rendition #2: Vivian Graeber, Jeffrey Zou, Kevin Xiao + Squishy, Like, FamousMrTable
# SoftDev
# Oct 2022

# Version 0: made sure that the website can return things other than "no hablo queso"
from flask import Flask
app = Flask(__name__) #create instance of class Flask

occupation = "GGG"

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return occupation

app.run()

