"""QR CODE GENERATORS: JEFFREY ZOU, JULIA LEE, WILLIAM V.
SoftDEV
K19 sessions
11-5-2022
time spent: 1 hr
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import session

username_key = 'qrcode' #hard coded login info
password_key = 'bbb'

# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session: #if username is in session then you are forwarded to response page
        return render_template('response.html', username = session['username'])
    return render_template('login.html') # if not, then you are directed to login page

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST': #after you press submit
        username = request.form['username'] #stores login info
        password = request.form['password']
        print(request.form['username'],request.form['password'])#testing login info
        if(username == username_key and password == password_key): #if login info is right, then you're directed to response
            session['username'] = username
            return render_template('response.html', username= username, password= password)
        else: #if login info isn't correct, displays appropriate error msg
            if username != username_key and password != password_key:
                return render_template('login.html', error_msg = 'wrong username and password!')
            if username != username_key:
                return render_template('login.html', error_msg = 'wrong username!')
            if password != password_key:
                return render_template('login.html', error_msg = 'wrong password!')

    

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('login.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
