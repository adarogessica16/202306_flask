from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'mysecretkey'
@app.route('/', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        print(request.form)
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
        return redirect("/result")
    return render_template('form.html')

@app.route("/result")
def result():
    # Verificar si la sesión existe
    if not session.get("name") or not session.get("location") or not session.get("language"):
        return "Faltan datos. Por favor, completa todos los campos en el formulario."

    # Obtener los datos de la sesión
    name = session.get("name")
    location = session.get("location")
    language = session.get("language")
    comment = session.get("comment")

    return render_template("info.html", name=name, location=location, language=language, comment=comment)


if __name__ == "__main__":
    app.run(debug=True)





