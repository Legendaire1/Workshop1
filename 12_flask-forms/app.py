"""QR CODE GENERATORS: JEFFREY ZOU, JULIA LEE
SoftDEV
K12 flask-forms
10-17-2022
time spent: 1 hr
"""

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

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***") 
    print(app) # prints name of flask module
    print("***DIAG: request obj ***") 
    print(request) # prints the page link
    print("***DIAG: request.args ***") 
    print(request.args) # prints a dictionary with the user's input
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***") 
    print(request.headers) # prints the user's system and browser
    return render_template( 'login.html' )


@app.route("/auth" , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***") 
    print(app) # prints name of flask module
    print("***DIAG: request obj ***")
    print(request) # prints the page link
    print("***DIAG: request.form.args ***")
    print(request.form) # prints a dictionary with the user's input using post method
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers) # prints the user's system and browser
    return render_template('response.html', username = request.form['username']) #response to a form submission using user as an argument


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
