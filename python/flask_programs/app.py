from flask import Flask, render_template, request

app=Flask(__name__)     #__name__ is a special character in Flask

@app.route('/send', methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['name']
        getMail=request.form['mail']
        getNumber=request.form['number']
        getSubject=request.form['subject']
        getMessage=request.form['message']
        return render_template('result.html',newName=getName, newMail=getMail, newNumber=getNumber, newSubject=getSubject, newMessage=getMessage)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactus')
def contact():
    return render_template('contactus.html')

if(__name__=='__main__'):
    app.run(debug=True)
