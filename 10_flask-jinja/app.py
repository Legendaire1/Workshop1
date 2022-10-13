# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
#q0: We know it will return anything
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
#q1: 127:0.0.0/5000/my_foist_template
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.
#q2: first parameter looks for the file name, foo is the content of the file, collection is a list of the content of the website
if __name__ == "__main__":
    app.debug = True
    app.run()
