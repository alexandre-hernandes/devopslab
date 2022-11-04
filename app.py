from flask import Flask

app = Flask(__name__)

csrf = CSRFProtect(app)   

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

if __name__ == '__main__':
    app.run()