import os
import json
from flask import Flask, render_template
# importing Flask class

app = Flask(__name__)
# Creating an instance and storing it in a variable called app
# (__name__) is a built in python variable
# Flask needs this so that it knows where to look. 
# for templates

@app.route("/")
# above is a decorator and always starts with @
# This is a way of wrapping functrions
def index():
    return render_template('index.html')


# creating another route of view
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
# the above page_title is a variable we made up but can be anything

# in order to add an advanced route we have to add a new @app.route"/about" 
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
# want to check if that object's url key from the file is equal to the member_name
        for obj in data:
             if obj["url"] == member_name:
                 member = obj
    return render_template("member.html", member = member)
    #return "<h1>" + member["name"] + "</h1>" note thge syntax

# Creating another route. Must have 2 blank lines to keep it PEP 8
# compliant
@app.route("/contact")
def contact():
     return render_template('contact.html', page_title="Contact ")


@app.route("/careers")
def careers():
     return render_template('careers.html', page_title="Careers")


if __name__ == "__main__": # __main__ is the default module name
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)