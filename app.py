
from flask import Flask, request,redirect
from flask_sqlalchemy import SQLAlchemy
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

class List(db.Model):
    __tablename__ = 'lista'
    id_list = db.Column(db.Integer, primary_key = True, autoincrement = True)
    faculty = db.Column(db.String(30),nullable=False)
    age  = db.Column(db.String(60),nullable=False)
    gender = db.Column(db.String(60),nullable=False)
    genre_of_poetry = db.Column(db.String(60),nullable=False)
    presentation_date = db.Column(db.String(60),nullable=False)

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
                                edad=str(register.date_of_birth).split('-')
                                actual=str(register.registration_date).split('-')
                                condiction= (int(actual[0]))-(int(edad[2]))
                                if condiction > 17:
                                    day=datetime.now()
                                    dia= int(day.day)
                                    mes=int(day.month)
                                    año=int(day.year)
                                    if (str(request.form['genre_of_poetry']).upper())=="LIRICA"  and (str(request.form['carnet'])[5])=="1"  :
                                        cont=0
                                        while (cont<=5):
                                            new=datetime(año,mes,dia)
                                            if (new.weekday()==5) or (new.weekday()==6):
                                                dia=dia+1;
                                            else:
                                                dia=dia+1
                                                cont+=1
                                    else:
                                        if (str(request.form['genre_of_poetry']).upper())=="EPICA" and str(request.form['carnet'])[5]=="3":
                                            numero=0
                                            if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes== 10 or mes== 12):
                                                numero=31;
                                            else:
                                                numero=30
                                                val=False
                                            while (val==False):
                                                new=datetime(año,mes,numero)
                                                if (new.weekday()==5) or (new.weekday()==6):
                                                    numero=numero-1
                                                else:
                                                    break    
                                        else:
                                            val=False
                                            while (val==False):
                                                new=datetime(año,mes,dia)
                                                if (new.weekday()==4):
                                                    break
                                                else:
                                                    dia=dia+1
                                    date_=str(new)[:-9]
                                    register2=List(faculty=request.form['faculty'],age=str(condiction),gender=request.form['gender'],genre_of_poetry=str(request.form['genre_of_poetry']),presentation_date=date_)
                                    db.session.add(register2)
                                    db.session.commit()
                                    db.session.add(register)
                                    db.session.commit()
                                    return {
                                        'faculty': request.form['faculty'],
                                        'age': condiction,
                                        'gender': request.form['gender'],
                                        'genre_of_poetry': request.form['genre_of_poetry'],
                                        'presentation_date': date_
                                    }
                                else:
                                    return "does not meet the age"
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

@app.route('/consult')
def consult():
    consulta=List.query.all()
    retorno=""
    for participant in consulta:
        retorno+="{\n"
        retorno+="  'age': "+ participant.age+",\n"
        retorno+="  'faculty': "+ participant.faculty+",\n"
        retorno+="  'gender': "+ participant.gender+",\n"
        retorno+="  'genre_of_poetry': "+ participant.genre_of_poetry+",\n"
        retorno+="  'presentation_date': "+ participant.presentation_date+",\n},\n" 
    if(retorno==""):
        return "no records" 
    else:
        retorno=retorno[:-2]
        return retorno

if __name__ == '__main__':
    app.run(debug=True)
