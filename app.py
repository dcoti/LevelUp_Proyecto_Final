import json
from flask import Flask, render_template, request, url_for, redirect,flash,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\Daniel Coti\\Documents\\Codigo\Level Up_Final\\database\\students.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id_student = db.Column(db.Integer, primary_key = True, autoincrement = True)
    carnet = db.Column(db.String(30),nullable=False)
    direction = db.Column(db.String(60),nullable=False)
    gender = db.Column(db.String(60),nullable=False)
    phone = db.Column(db.Integer,nullable=False)
    date_of_birth = db.Column(db.String(60),nullable=False)
    faculty = db.Column(db.String(60),nullable=False)
    genre_of_poetry = db.Column(db.String(60),nullable=False)
    registration_date = db.Column(db.String(60),nullable=False)


@app.route('/healthcheck')
def healthcheck():
    return "service healthy"

@app.route('/')
def index():
    return redirect('/register')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form['carnet']=="" or request.form['direction']=="" or request.form['gender']=="" or request.form['phone']=="" or request.form['date_of_birth']=="" or request.form['faculty']=="" or request.form['genre_of_poetry']=="":
            return  'All fields are required'
        else:
            carne=len(str(request.form['carnet']))
            if carne == 6:
                carne=str(request.form['carnet'])
                val=False
                for caracter in carne:
                    if caracter=="0":
                        val=True
                if val==False:
                    if str(request.form['carnet'])[0]=="A":
                        if str(request.form['carnet'])[2]=="5":
                            if str(request.form['carnet'])[5]=="1" or str(request.form['carnet'])[5]=="3" or str(request.form['carnet'])[5]=="9":
                                register=Student(carnet=request.form['carnet'],direction=request.form['direction'],gender=request.form['gender'],phone=str(request.form['phone']),date_of_birth=str(request.form['date_of_birth']),faculty=str(request.form['faculty']),genre_of_poetry=str(request.form['genre_of_poetry']),registration_date=str(datetime.now())[:-16])
                                print(register.carnet)
                                db.session.add(register)
                                db.session.commit()
                                return "CONGRATULATIONS"
                            else:
                                return "must end in one, three or nine"
                        else:
                            return "Third digit should be five"
                    else:
                        return "must begin with the letter A"
                else: 
                    return "contains zeros"
            else:
                return "invalid card"
    else: 
        return "Welcome"

if __name__ == '__main__':
    app.run(debug=True)

    