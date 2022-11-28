from logging import makeLogRecord
from flask import *

app=Flask(__name__)

@app.route("/error")

def error():

    return make_response("<h1>Page's is not found</h1>")

@app.route("/login")

def login():
    return render_template('login.html')

@app.route("/success",methods=['POST'])

def success():
    
    if request.method=='POST':
        user=request.form['email']
        passw=request.form['password']

    if passw=='sudha':
        resp=make_response(render_template('success.html'))
        resp.set_cookie('email',user)
        return  resp

    else:
        abort(429)

@app.route('/profile')

def profile():
    user=request.cookies.get('email')
    resp=make_response(render_template('profile.html',n=user))
    return resp

if __name__=="__main__":
    app.run(debug=True)

