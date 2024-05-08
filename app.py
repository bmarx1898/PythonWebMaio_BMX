from flask import Flask
app = Flask("supimpa")
@app.route('/')
def supimpa():
    return "supimpa mundo"
    