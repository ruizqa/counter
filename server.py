from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)  
app.secret_key = 'secret'


@app.route('/')         
def visits():
    
    if 'visits' in session:
        session['visits'] = session['visits'] + 1  # reading and updating session data
    else:
        session['visits'] = 1

    if 'counter' not in session:
        session['counter'] =0
    
    return render_template("index.html")

@app.route('/destroy')         
def destroy():
    session.pop('visits', None)
    session.pop('counter',None)
    return redirect ("/")

@app.route('/add2')         
def add2():
    session['visits'] = session['visits'] + 1
    return redirect ("/")

@app.route('/checkout', methods=['POST'])  
def checkout():
    session['counter'] += int(request.form['number']) -1
    return redirect ("/")
 

if __name__=="__main__":   
    app.run(debug=True)    