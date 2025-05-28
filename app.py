from flask import Flask, request, render_template
import cv2
import numpy as np
import os

app = Flask(__name__)

def clasificar_imagen(path):
    imagen = cv2.imread(path)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    promedio = np.mean(gris)
    if promedio > 150:
        return "Pantalla o carcasa externa"
    else:
        return "Batería o componente interno"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        archivo = request.files['archivo']
        ruta = os.path.join("static", archivo.filename)
        archivo.save(ruta)
        resultado = clasificar_imagen(ruta)
    return render_template("index.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
