from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)  
app.secret_key = 'secret'


@app.route('/')         
def visits():
    if 'visits' in session:
        session['visits'] = session['visits'] + 1  # reading and updating session data
    else:
        session['visits'] = 1
    return render_template("index.html")

@app.route('/destroy_session')         
def destroy():
    session.pop('visits', None)
    return redirect ("/")

@app.route('/add2')         
def add2():
    session['visits'] = session['visits'] + 1
    return redirect ("/")

if __name__=="__main__":   
    app.run(debug=True)    