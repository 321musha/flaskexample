from flask import Flask
application=Flask(__name__)

@application.route('/')#default webpage
def hello_world():
    return "looking into the Flask"
