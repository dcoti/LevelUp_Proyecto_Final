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
    created_at = db.Column(db.String(60),nullable=False)


@app.route('/healthcheck')
def healthcheck():
    return "service healthy"

@app.route('/')
def index():
    return redirect('/form')


@app.route('/form', methods=['GET','POST'])
def form():
    return "Bienvenido"

if __name__ == '__main__':
    app.run(debug=True)