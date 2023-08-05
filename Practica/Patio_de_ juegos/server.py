from flask import Flask, render_template  # agregado render_template!# Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)   

@app.route('/play')
@app.route('/play/<int:num_cajas>/')
@app.route('/play/<string:color>/')
@app.route('/play/<string:color>/<int:num_cajas>/')
def play(num_cajas=3, color="blue"):
    return render_template('index.html', num_cajas=num_cajas, color=color)

if __name__=="__main__":      
    app.run(debug=True)   