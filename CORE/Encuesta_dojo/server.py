from flask import Flask, render_template, session, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'mysecretkey'
@app.route('/')
def index():
    return render_template("form.html")


@app.route('/process', methods=['POST'])
def process():
        print(request.form)
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
        return redirect("/result")

@app.route("/result")
def result():
    # Verificar si la sesión existe
    if not session.get("name") or not session.get("location") or not session.get("language"):
        return "Faltan datos. Por favor, completa todos los campos en el formulario."

    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)





