from flask import Flask, render_template  # agregado render_template!# Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    
@app.route('/')          
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

#Crea una ruta que responda con "¡Dojo!"   
@app.route('/dojo')
def dojo():
    return "¡Dojo!"

#Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos: localhost:5000/say/flask: haz que diga "¡Hola, Flask!"

@app.route('/say/<nombre>') 
def hola(nombre):
    print(nombre)
    return f'¡Hola, {nombre}!'

@app.route('/repeat/<int:num>/<string:palabra>')
def repetir_palabra(num, palabra):
    if num <= 0:
        return "El número debe ser mayor a cero."
    return palabra * num

@app.errorhandler(404)
def ruta_no_encontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración