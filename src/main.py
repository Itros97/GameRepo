from config import config
from flask import Flask
from flask_sqlalchemy import MySQL
import pymysql

pymysql.install_as_MySQLdb()


app = Flask(__name__)

conexion = MySQL(app)


@app.route('/libreria')
def listar_lib():
    try:
        return "Ok"
    except Exception as ex:
        return "Error"


@app.route('/')
def index():
    return "Hola soy una app WEB hecha en Atom"


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)
    app.run(host='localhost', port=5000)
#app.run(host='localhost', port=5000)
