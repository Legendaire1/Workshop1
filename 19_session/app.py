"""QR CODE GENERATORS: JEFFREY ZOU, JULIA LEE, WILLIAM V.
SoftDEV
K12 flask-forms
10-17-2022
time spent: 1 hr
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import session
username = 'qrcode'

'''app = Flask(__name__)    #create Flask object
@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth" , methods=['GET', 'POST'])
def authenticate():
    if(request.form['username']) == username:
        return render_template('response.html', username = request.form['username']) #response to a form submission using user as an argument
    return render_template('login.html')
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
'''


# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
        return render_template('response.html')
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
