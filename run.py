from flask import Flask

app = Flask(__name__)#creamos app
        
@app.route("/")
def index():
    return "Hola mundo"