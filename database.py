from flask import Flask, render_template, url_for, request, redirect,session,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship
import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,login_user,current_user,logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:udayan@127.0.0.1/KISSTEMPLE'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)



class all_prasadam(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    address = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    anna = db.Column(db.Integer)
    kanika = db.Column(db.Integer)
    jerraanna = db.Column(db.Integer)
    oriyaanna = db.Column(db.Integer)
    kamalaanna = db.Column(db.Integer)
    gheeanna = db.Column(db.Integer)
    khichudi = db.Column(db.Integer)
    haradadali = db.Column(db.Integer)
    mugadali = db.Column(db.Integer)
    haradadalma = db.Column(db.Integer)
    mugadalma = db.Column(db.Integer)
    puridalma = db.Column(db.Integer)
    purimithadali = db.Column(db.Integer)
    butadali = db.Column(db.Integer)
    beshar = db.Column(db.Integer)
    sagamuga = db.Column(db.Integer)
    bhajachennatarkari = db.Column(db.Integer)
    panneertarkari = db.Column(db.Integer)
    pannerbuta = db.Column(db.Integer)
    mahura = db.Column(db.Integer)
    potalabesanatarkari = db.Column(db.Integer)
    potalarasha = db.Column(db.Integer)
    janhitarkari = db.Column(db.Integer)
    butatarkari = db.Column(db.Integer)
    chips = db.Column(db.Integer)
    kadalibhaja = db.Column(db.Integer)
    potalakurma = db.Column(db.Integer)
    ambularai = db.Column(db.Integer)
    khajurikhatta = db.Column(db.Integer)
    dahibaigana = db.Column(db.Integer)
    sapurikhatta = db.Column(db.Integer)
    fruitsalad = db.Column(db.Integer)
    ambakhatta = db.Column(db.Integer)
    ouukhatta = db.Column(db.Integer)
    dahibundi = db.Column(db.Integer)
    khira = db.Column(db.Integer)
    khiree = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    type_of_order = db.Column(db.String(200))
    date_of_order = db.Column(db.Date)
    def _init_(self,firstname,lastname,address,email,phone,item,price,type_of_order):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.item = item
        self.price = price
        self.type_of_order = type_of_order
        self.date_of_order = date_of_order
        

class donationsignup(UserMixin,db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200))
    address = db.Column(db.String(200))
    email = db.Column(db.String(200),unique = True)
    mobile = db.Column(db.String(200))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(200))
    gotra = db.Column(db.String(200))
    dom = db.Column(db.Date,nullable = True)
    password = db.Column(db.String(280))
    def _init_(self,fname,lname,address,email,mobile,dob,gender,gotra,dom,password):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.email = email
        self.mobile = mobile
        self.dob = dob
        self.gender = gender
        self.gotra = gotra
        self.dom = dom
        self.password = generate_password_hash(password)

class donatemoney(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    amtprice = db.Column(db.Integer)
    email = db.Column(db.String(200))
    date_of_donation = db.Column(db.Date)
    time_of_donation = db.Column(db.Time)
    def _init_(self,amtprice,mode):
        self.amtprice = amtprice
        self.date_of_donation = date_of_donation
        self.time_of_donation = time_of_donation
        
class dailyprasadmanager(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    anna = db.Column(db.Integer)
    haradadali = db.Column(db.Integer)
    beshar = db.Column(db.Integer)
    ambularai = db.Column(db.Integer)
    khiraa = db.Column(db.Integer)
    dahibundi = db.Column(db.Integer)
    price = db.Column(db.NUMERIC)
    def _init_(self,number):
        self.number = number

class specialprasadmanager(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    item = db.Column(db.String(200))
    qty = db.Column(db.Integer)
    price = db.Column(db.Integer)
    def _init_(self,item,qty,price):
        self.item = item
        self.qty = qty
        self.price = price

class foodprice(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    anna = db.Column(db.Integer)
    kanika = db.Column(db.Integer)
    jerraanna = db.Column(db.Integer)
    oriyaanna = db.Column(db.Integer)
    kamalaanna = db.Column(db.Integer)
    gheeanna = db.Column(db.Integer)
    khichudi = db.Column(db.Integer)
    haradadali = db.Column(db.Integer)
    mugadali = db.Column(db.Integer)
    haradadalma = db.Column(db.Integer)
    mugadalma = db.Column(db.Integer)
    puridalma = db.Column(db.Integer)
    purimithadali = db.Column(db.Integer)
    butadali = db.Column(db.Integer)
    beshar = db.Column(db.Integer)
    sagamuga = db.Column(db.Integer)
    bhajachennatarkari = db.Column(db.Integer)
    panneertarkari = db.Column(db.Integer)
    pannerbuta = db.Column(db.Integer)
    mahura = db.Column(db.Integer)
    potalabesanatarkari = db.Column(db.Integer)
    potalarasha = db.Column(db.Integer)
    janhitarkari = db.Column(db.Integer)
    butatarkari = db.Column(db.Integer)
    chips = db.Column(db.Integer)
    kadalibhaja = db.Column(db.Integer)
    potalakurma = db.Column(db.Integer)
    ambularai = db.Column(db.Integer)
    khajurikhatta = db.Column(db.Integer)
    dahibaigana = db.Column(db.Integer)
    sapurikhatta = db.Column(db.Integer)
    fruitsalad = db.Column(db.Integer)
    ambakhatta = db.Column(db.Integer)
    ouukhatta = db.Column(db.Integer)
    dahibundi = db.Column(db.Integer)
    khira = db.Column(db.Integer)
    khiree = db.Column(db.Integer)
    def _init_(self,anna,kanika,jerraanna,oriyaanna,kamalaanna,gheeanna,khichudi,haradadali,mugadali,haradadalma,mugadalma,puridalma,purimithadali,butadali,beshar,sagamuga,bhajachennatarkari,panneertarkari,pannerbuta,mahura,potalabesanatarkari,potalarasha,janhitarkari,butatarkari,chips,kadalibhaja,potalakurma,ambularai,khajurikhatta,dahibaigana,sapurikhatta,fruitsalad,ambakhatta,ouukhatta,dahibundi,khira,khiree):
        self.anna = anna
        self.kanika = kanika
        self.jerraanna = jerraanna
        self.oriyaanna = oriyaanna
        self.kamalaanna = kamalaanna
        self.gheeanna = gheeanna
        self.khichudi = khichudi
        self.haradadali = haradadali
        self.mugadali = mugadali
        self.haradadalma = haradadalma
        self.mugadalma = mugadalma
        self.puridalma = puridalma
        self.purimithadali = purimithadali
        self.butadali = butadali
        self.beshar = beshar
        self.sagamuga = sagamuga
        self.bhajachennatarkari = bhajachennatarkari
        self.panneertarkari = panneertarkari
        self.pannerbuta = pannerbuta
        self.mahura = mahura
        self.potalabesanatarkari = potalabesanatarkari
        self.potalarasha = potalarasha
        self.janhitarkari = janhitarkari
        self.butatarkari = butatarkari
        self.chips = chips
        self.kadalibhaja = kadalibhaja
        self.potalakurma = potalakurma
        self.ambularai = ambularai
        self.khajurikatta = khajurikhatta
        self.dahibaigana = dahibaigana
        self.sapurikhatta = sapurikhatta
        self.fruitsalad = fruitsalad
        self.ambakhatta = ambakhatta
        self.ouukhatta = ouukhatta
        self.dahibundi = dahibundi
        self.khira = khira
        self.khiree = khiree


class hallbook(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    date = db.Column(db.Date)
    hall1_slot1 = db.Column(db.String(200))
    hall1_slot2 = db.Column(db.String(200))
    hall2_slot1 = db.Column(db.String(200))
    hall2_slot2 = db.Column(db.String(200))
    hall3_slot1 = db.Column(db.String(200))
    hall3_slot2 = db.Column(db.String(200))
    hall4_slot1 = db.Column(db.String(200))
    hall4_slot2 = db.Column(db.String(200))
    room_1 = db.Column(db.String(200))
    room_2 = db.Column(db.String(200))
    room_3 = db.Column(db.String(200))
    room_4 = db.Column(db.String(200))
    deco1 = db.Column(db.String(200))
    deco2 = db.Column(db.String(200))
    deco3 = db.Column(db.String(200))
    def _init_(self,date,hall1_slot1,hall1_slot2,hall2_slot1,hall2_slot2,hall3_slot1,hall3_slot2,hall4_slot1,hall4_slot2,room_1,room_2,room_3,room_4,deco1,deco2,deco3):
        self.date = date
        self.hall1_slot1 = hall1_slot1
        self.hall1_slot2 = hall1_slot2
        self.hall2_slot1 = hall2_slot1
        self.hall2_slot2 = hall2_slot2
        self.hall3_slot1 = hall3_slot1
        self.hall3_slot2 = hall3_slot2
        self.hall4_slot1 = hall4_slot1
        self.hall4_slot2 = hall4_slot2
        self.room_1 = room_1
        self.room2 = room_2
        self.room_3 = room_3
        self.room_4 = room_4
        self.deco1 = deco1
        self.deco2 = deco2
        self.deco3 = deco3

class hallbook_details(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200))
    address = db.Column(db.String(200))
    email = db.Column(db.String(200))
    mobile = db.Column(db.String(200))
    nfg = db.Column(db.Integer)
    date_of_book = db.Column(db.Date)
    def _init_(self,fname,lname,address,email,mobile,nfg):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.email = email
        self.mobile = mobile
        self.nfg = nfg
        self.date_of_book = date_of_book

class university_employee(db.Model):
    id = db.Column(db.Integer,nullable = False,primary_key = True)
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200))
    address = db.Column(db.String(200))
    email = db.Column(db.String(200),unique = True)
    mobile = db.Column(db.String(200))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(200))
    empid = db.Column(db.String(200),unique = True)
    department = db.Column(db.String(200))
    gotra = db.Column(db.String(200))
    dom = db.Column(db.Date,nullable = True)
    password = db.Column(db.String(280))
    def _init_(self,fname,lname,address,email,mobile,dob,gender,empid,department,gotra,dom,password):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.email = email
        self.mobile = mobile
        self.dob = dob
        self.gender = gender
        self.empid = empid
        self.department = department
        self.gotra = gotra
        self.dom = dom
        self.password = generate_password_hash(password)
  
class halldetails(db.Model):
    id = db.Column(db.Integer,nullable = True,primary_key = True)
    hall1_slot1 = db.Column(db.Integer)
    hall1_slot2 = db.Column(db.Integer)
    hall2_slot1 = db.Column(db.Integer)
    hall2_slot2 = db.Column(db.Integer)
    hall3_slot1 = db.Column(db.Integer)
    hall3_slot2 = db.Column(db.Integer)
    hall4_slot1 = db.Column(db.Integer)
    hall4_slot2 = db.Column(db.Integer)
    room_1 = db.Column(db.Integer)
    room_2 = db.Column(db.Integer)
    room_3 = db.Column(db.Integer)
    room_4 = db.Column(db.Integer)
    deco1 = db.Column(db.Integer)
    deco2 = db.Column(db.Integer)
    deco3 = db.Column(db.Integer)
    def _init_(self,date,hall1_slot1,hall1_slot2,hall2_slot1,hall2_slot2,hall3_slot1,hall3_slot2,hall4_slot1,hall4_slot2,room_1,room_2,room_3,room_4,deco1,deco2,deco3):
        self.date = date
        self.hall1_slot1 = hall1_slot1
        self.hall1_slot2 = hall1_slot2
        self.hall2_slot1 = hall2_slot1
        self.hall2_slot2 = hall2_slot2
        self.hall3_slot1 = hall3_slot1
        self.hall3_slot2 = hall3_slot2
        self.hall4_slot1 = hall4_slot1
        self.hall4_slot2 = hall4_slot2
        self.room_1 = room_1
        self.room2 = room_2
        self.room_3 = room_3
        self.room_4 = room_4
        self.deco1 = deco1
        self.deco2 = deco2
        self.deco3 = deco3
 
    
