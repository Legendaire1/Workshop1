from flask import flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/image')
def image():
    