from flask import Flask, jsonify,request, url_for, redirect, session, render_template, g
import mysql.connector 

app = Flask(__name__)

mydb = mysql.connector.connect(host='localhost',user='root',password='Ydurga232bhavani@',database='riseslabs') 
mycursor = mydb.cursor() 

@app.route('/')
def home():
    return "hello durga"

@app.route('/signup', methods=['GET','POST']) 
def signup():
    msg = ''
    if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form and 'password' in request.form and 'confpassword' in request.form:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        confpassword = request.form['confpassword']
        if password == confpassword:
            
            mycursor.execute('INSERT INTO users(firstname,lastname,email,password,confpassword) VALUES(%s,%s,%s,%s,%s)', (firstname,lastname,email,password,confpassword))
            mydb.commit()
            msg = "You have successfully registred"
        else:
            msg = "Please enter the same password enterd above"
        
    return render_template("signup.html",msg=msg)

if __name__ == '__main__':
    app.run(debug=True)