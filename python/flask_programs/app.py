from flask import Flask

app=Flask(__name__)     #__name__ is a special characher in Flask

@app.route('/')
def index():
    return 'WELCOME TO FLASK....'

@app.route('/home')
def home():
    return 'Welcome To Home'

if(__name__=='__main__'):
    app.run(debug=True)
