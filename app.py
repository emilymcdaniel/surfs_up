from flask import Flask
# Name the flask "app". Note: __name__ indicates the name of the current function (app)
app = Flask(__name__)
# Define starting point, or "Root"
@app.route('/')
def hello_world():
    return 'Hello world'