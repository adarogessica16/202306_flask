from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'miclavesecreta-'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    
    return render_template('index.html', counter=session['counter'])

@app.route('/increment', methods=['POST'])
def increment():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)



