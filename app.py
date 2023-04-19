from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)   

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps - Entrega Final - 24/04/2023"

if __name__ == '__main__':
    app.run()