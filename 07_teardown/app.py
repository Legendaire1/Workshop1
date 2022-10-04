'''
Rubber Duckies: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
SoftDev
K07 -- Teardown / Investigating Flask
2022-10-03
time spent: 0.5 hrs
'''

from flask import Flask

app = Flask("bob") # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print("bob") # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
* We don't have Flask installed on our personal computers, which was leading to the ModuleNotFound error. We needed to install it as a package in Thonny before attempting to import anything.
* The hello_world() function is defined but never called. However, we receive the output in the console and the message in the webpage - maybe this means hello_world() is called within the app.run() invocation.
* Changing the string in @app.route causes the provided webpage to lead to an unfound URL. So it appears that this @app.route line indicates where the web page lives and how to properly get there. We think that it's probably a good idea to leave the string unchanged as a preset so as not to interfere with the webpage.
QCC:
0. We've seen similar syntax in Java, especially with overloaded constructors and typecasting. Here, Flask would be the constructor name, and __name__ is the parameter it takes in.
1. We've seen '/' in file paths when we're working with directories in Terminal, and the character also shows up in URLs, similarly denoting a kind of path.
2. We think this line will print to the console, as that's where print statements have printed in our experience.
3. It'll print whatever __name__ is a placeholder for, perhaps the name of the app.
4. This will appear on the webpage whose local link is given to us when we run this Python file. We know because the address was hyperlinked, and we were able to open it in a web browser.
5. We've seen the dot and empty parentheses used in a lot of class methods in Java. We think that if we interpret line 11 to be a constructor, then perhaps line 18 is running a non-static (or static?) method of the Flask class, though we're not sure if characteristics like staticness translate from Java to Python.
...
INVESTIGATIVE APPROACH:
* First, we didn't modify the code at all, and we just made comparisons to Java and answered the provided questions.
* Without changing the content of the given code, we ran the file for the first time, and we immediately received a ModuleNotFoundError: "No module named 'flask'"
* We replaced __name__ with a string ("bob"), since we assumed __name__ was a placeholder.
* We SSHed into a lab computer and ran the app.py file from there -- we did not receive the ModuleNotFoundError, but we were unable to open the provided webpage on our own machine, since it was the address on the lab machine.
* We realized Flask might be a package that is necessary for Thonny to install. We went to Tools --> Manage packages... --> Flask --> Install
* The next time we ran, we didn't receive the ModuleNotFoundError. We received:
     Serving Flask app 'bob'
     Debug mode: off
     WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    bob
    127.0.0.1 - - [03/Oct/2022 20:56:37] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [03/Oct/2022 20:56:38] "GET /favicon.ico HTTP/1.1" 404 -
* When we visited the http://127.0.0.1:5000 page, we saw "No hablo queso!" on the page.
* We tried modifying the "/" on line 13. We changed it to "/testing," and we didn't receive any errors in the console, but when we opened the webapge, we received a URL Not Found message. We changed back to "/"
'''
