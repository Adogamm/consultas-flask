# Importacion del farmework de Flask
from flask import Flask, render_template, request, redirect
import controlador

app = Flask(__name__)

@app.route("/")
@app.route("/productos")
def menu():
    return render_template("index.html")

@app.route("/ropa")
def consulta_ropa():
    ropa = controlador.obtener_ropa()
    return render_template("tabla_ropa.html", ropa = ropa)

@app.route("/accesorios")
def consulta_accesorio():
    accesorio = controlador.obtener_accesorio()
    return render_template("tabla_accesorios.html", accesorio = accesorio)

@app.route("/calzado")
def consulta_calzado():
    calzado = controlador.obtener_calzado()
    return render_template("tabla_calzado.html", calzado = calzado)

# Iniciar el servidor, indicando el puerto
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
