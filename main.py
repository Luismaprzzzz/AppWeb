#importacion de librerias
from flask import Flask, render_template
#creacion de obj de flask
app = Flask(__name__)
#creacion de ruta para la pagina principal
@app.route("/")
#creacion de funcion para index
def index():
    return render_template("index.html")



#definicion de servidor web
if __name__ == '__main__':
    app.run(port = 3000,debug = True)


