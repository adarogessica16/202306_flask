from flask import Flask, render_template  # agregado render_template!# Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)   

@app.route('/')
def tablero():
    return render_template('index.html', filas=8, columnas=8)

@app.route('/<int:filas>')
def tablero_filas(filas):
    return render_template('index.html', filas=filas, columnas=8)

@app.route('/<int:filas>/<int:columnas>')
def tablero_filas_columnas(filas, columnas):
    return render_template('index.html', filas=filas, columnas=columnas)

if __name__=="__main__":      
    app.run(debug=True)   