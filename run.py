import os
from flask import Flask, render_template
# importing Flask class

app = Flask(__name__)
# Creating an instance and storing it in a variable called app
# (__name__) is a built in python variable
# Flask needs this so that it knows where to look 
# for templates

@app.route("/")
# above is a decorator and always starts with @
# This is a way of wrapping functrions
def index():
    return render_template('index.html')


# creating another route of view
@app.route("/about")
def about():
     return render_template('about.html')


# Creating another route. Must have 2 blank lines to keep it PEP 8
# compliant
@app.route("/contact")
def contact():
     return render_template('contact.html')


@app.route("/careers")
def careers():
     return render_template('careers.html')


if __name__ == "__main__": # __main__ is the default module name
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)