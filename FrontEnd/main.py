from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hola soy una app WEB hecha en Atom"


app.run(host='localhost', port=5000)
