# GGG Rendition #2: Vivian Graeber, Jeffrey Zou, Kevin Xiao + Squishy, Like, FamousMrTable
# SoftDev
# Oct 2022

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''



def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***") # this will display the flask object itself
    print(app)
    print("***DIAG: request obj ***") # this will display the html template
    print(request)
    print("***DIAG: request.args ***") # this will sort any requests the html template requires (form)
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' ) # displays website


@app.route("/", methods=[ 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***") # this will display the flask object itself
    print(app)
    #print("***DIAG: request obj ***") # this will display the html template
    #print(request)
    #print("***DIAG: request.args ***") # this will sort any requests the html template requires (form)
    #print(request.args)

    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'test.html' ) # displays website




@app.route("/auth", methods=[ 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)]
    
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission

# this will probably be the resulting webpage after completing a form in the initial webpage
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
