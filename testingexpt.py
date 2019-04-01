from flask import Flask,render_template,request,flash,url_for,redirect,session,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship,sessionmaker
from database import all_prasadam,donationsignup,donatemoney,db,app,halldetails,dailyprasadmanager,specialprasadmanager,hallbook,hallbook_details,foodprice,university_employee
import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@app.route('/',methods = ['GET','POST'])
def index():
    return render_template('home.html',login_session = session.get('logged_in'))

@app.route('/about',methods=['GET'])
def about():
    return render_template('aboutktt.html',login_session = session.get('logged_in'))

@app.route('/founder',methods=['GET'])
def founder():
    return render_template('founder.html',login_session = session.get('logged_in'))

@app.route('/puja',methods = ['GET'])
def pujaa():
    return render_template('architecture.html',login_session = session.get('logged_in'))

@app.route('/deities',methods =['GET'])
def deities():
    return render_template('deities.html',login_session = session.get('logged_in'))

@app.route('/festivals',methods = ['GET'])
def festivals():
    return render_template('festivals.html',login_session = session.get('logged_in'))


@app.route('/rituals',methods=['GET'])
def rituals():
    return render_template('rituals.html',login_session = session.get('logged_in'))

@app.route('/education',methods=['GET'])
def education():
    return render_template('education.html',login_session = session.get('logged_in'))

@app.route('/health',methods=['GET'])
def health():
    return render_template('health.html',login_session = session.get('logged_in'))

@app.route('/family',methods=['GET'])
def familycare():
    return render_template('family.html',login_session = session.get('logged_in'))

@app.route('/environment',methods=['GET'])
def environment():
    return render_template('environment.html',login_session = session.get('logged_in'))

@app.route('/rural',methods=['GET'])
def ruraldev():
    return render_template('rural.html',login_session = session.get('logged_in'))


@app.route('/contact',methods = ['GET','POST'])
def contact_us():
    if request.method == 'POST':
        return render_template('contact us.html',login_session = session.get('logged_in'))
    return render_template('contact us.html',login_session = session.get('logged_in'))


#existing user order prasad through only the phone number
@app.route('/existing',methods = ['GET','POST'])
def existing_user():                
    if request.method == 'POST':
        prasad_cust_list = []                                   #details list for the custumer
        check_db = all_prasadam.query.all()                     #fetch the details of all the customers
        if check_db:                                            #check if details exists in the database
            for x in check_db:
                if x.phone == request.form['phone']:            #check if the requsted phone number exists in the database 
                    prasad_cust_list.clear()                    #clear the list declared for once
                    prasad_cust_list.append(x.firstname)        #add on all the details fetched 
                    prasad_cust_list.append(x.lastname)
                    prasad_cust_list.append(x.address)
                    prasad_cust_list.append(x.email)
                    prasad_cust_list.append(x.phone)
                    session['prasad_customer'] = prasad_cust_list   #create a sesssion object for the list
                    return redirect(url_for('thalitype'))           
                return render_template('prasadam.html',login_session = session.get('logged_in'))
        return render_template('prasadam.html',login_session = session.get('logged_in'))
    return render_template('existing_pras.html',login_session = session.get('logged_in'))
    
@app.route('/bhoga',methods = ['GET','POST'])
def form_prasad():
    prasad_cust_list = []
    print("Outside The request")
    if request.method == 'POST':
        print("Inside request form_prasad")
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address = request.form['address']
        email = request.form['emailaddress']
        phone = request.form['phone']
        prasad_cust_list.clear()
        prasad_cust_list.append(firstname)
        prasad_cust_list.append(lastname)
        prasad_cust_list.append(address)
        prasad_cust_list.append(email)
        prasad_cust_list.append(phone)
        session['prasad_customer'] = prasad_cust_list
        return redirect(url_for('thalitype'))
    return render_template('prasadam.html',login_session = session.get('logged_in'))

@app.route('/thalitype',methods = ['GET', 'POST'])
def thalitype():
    qtyprasad = dailyprasadmanager.query.get(30)
    sp_prasad = specialprasadmanager.query.all()
    s = 0
    for x in sp_prasad:
        s = s + int(x.qty)
    if qtyprasad.anna > 0 and s > 0:
        return render_template('thalitype.html',login_session = session.get('logged_in'),statusd = "available",statuss = "available")
    elif qtyprasad.anna <= 0 and s > 0:
        return render_template('thalitype.html',login_session = session.get('logged_in'),statusd = "unavailable",statuss = "available")
    elif qtyprasad.anna > 0 and s <= 0:
        return render_template('thalitype.html',login_session = session.get('logged_in'),statusd = "available",statuss = "unavailable")
    else:
        return render_template('thalitype.html',login_session = session.get('logged_in'),statusd = "unavailable",statuss = "unavailable")

@app.route('/dailythali',methods = ['GET', 'POST'])
def daily_thali():
    qtyprasad = dailyprasadmanager.query.get(30)
    item_dict = {'anna':0,'kanika':0,'jerraanna':0,'oriyaanna':0,'kamalaanna':0,'gheeanna':0,'khichudi':0,
             'haradadali':0,'mugadali':0,'haradadalma':0,'mugadalma':0,'puridalma':0,'purimithadali':0,'butadali':0,
             'beshar':0,'sagamuga':0,'bhajachennatarkari':0,'panneertarkari':0,'pannerbuta':0,'mahura':0,'potalabesanatarkari':0,'potalarasha':0,
             'janhitarkari':0,'butatarkari':0,'chips':0,'kadalibhaja':0,'potalakurma':0,'ambularai':0,'khajurikhatta':0,'dahibaigana':0,'sapurikhatta':0,
             'fruitsalad':0,'ambakhatta':0,'ouukhatta':0,'dahibundi':0,'khira':0,'khiree':0}
    if request.method == 'POST':
        if int(request.form['qty']) <= qtyprasad.anna and int(requesto.form['qty'])>0:
             item_dict['anna'] = request.form['qty']
             item_dict['haradadali'] = request.form['qty']
             item_dict['beshar'] = request.form['qty']
             item_dict['ambularai'] = request.form['qty']
             item_dict['dahibundi'] = request.form['qty']
             item_dict['khira'] = request.form['qty']
             session['qttydaily'] = request.form['qty']
             session['type_of_service'] = request.form['service']
             price = int(request.form['qty'])*int(qtyprasad.price)
             session['daily_pay'] = price
             order_list = session.get('prasad_customer')
             session['item_dict_daily'] = item_dict
             print(session.get('prasad_customer'))
             if order_list[0]!='' or order_list[1]!='' or order_list[2]!='' or order_list[3]!='' or order_list[4]!='':
                 return render_template('prepaymentbilldaily.html',login_session = session.get('logged_in'),msg = 'Daily prasad successfully booked!!',price = session.get('daily_pay'),qtyprasad = qtyprasad)
             return redirect('/bhoga')
        return render_template('dailyprasadam.html',login_session = session.get('logged_in'),msg = 'The required qty is not available',qtyprasad = dailyprasadmanager.query.get(30))
    return render_template("dailyprasadam.html",login_session = session.get('logged_in'),qtyprasad = dailyprasadmanager.query.get(30))
@app.route('/prepaymentbill',methods = ['GET', 'POST'])
def bill_pay_daily():
    qtyprasad = dailyprasadmanager.query.get(30)
    item_dict = session.get('item_dict_daily')
    if request.method == 'POST':
        order_list = session.get('prasad_customer')
        all_obj = all_prasadam(firstname = order_list[0],
                               lastname = order_list[1],
                               address = order_list[2],
                               email = order_list[3],
                               phone = order_list[4],
                               anna = session.get('qttydaily'),
                               haradadali = session.get('qttydaily'),
                               beshar = session.get('qttydaily'),
                               ambularai = session.get('qttydaily'),
                               dahibundi = session.get('qttydaily'),
                               khira = session.get('qttydaily'),
                               price = session.get('daily_pay'),
                               type_of_order = session.get('type_of_service'),
                               date_of_order = datetime.datetime.now().date()
                               )
        db.session.add(all_obj)
        qtyprasad.anna = qtyprasad.anna - int(session.get('qttydaily'))
        qtyprasad.haradadali = qtyprasad.haradadali - int(session.get('qttydaily'))
        qtyprasad.beshar = qtyprasad.beshar - int(session.get('qttydaily'))
        qtyprasad.ambularai = qtyprasad.ambularai - int(session.get('qttydaily'))
        qtyprasad.khiraa = qtyprasad.khiraa - int(session.get('qttydaily'))
        qtyprasad.dahibundi = qtyprasad.dahibundi - int(session.get('qttydaily'))
        db.session.commit() 
        return render_template('prepaymentbilldaily.html',login_session = session.get('logged_in'),msg = "This is to be directed to payment!!",price = session.get('daily_pay'),qtyprasad = qtyprasad)
    return render_template('prepaymentbilldaily.html',login_session = session.get('logged_in'),price = session.get('daily_pay'),qtyprasad = qtyprasad)

@app.route('/specialthali',methods = ['GET', 'POST'])
def special_thali():
    y = specialprasadmanager.query.all()
    print(y)
    item_dict = {'anna':0,'kanika':0,'jerraanna':0,'oriyaanna':0,'kamalaanna':0,'gheeanna':0,'khichudi':0,
             'haradadali':0,'mugadali':0,'haradadalma':0,'mugadalma':0,'puridalma':0,'purimithadali':0,'butadali':0,
             'beshar':0,'sagamuga':0,'bhajachennatarkari':0,'panneertarkari':0,'pannerbuta':0,'mahura':0,'potalabesanatarkari':0,'potalarasha':0,
             'janhitarkari':0,'butatarkari':0,'chips':0,'kadalibhaja':0,'potalakurma':0,'ambularai':0,'khajurikhatta':0,'dahibaigana':0,'sapurikhatta':0,
             'fruitsalad':0,'ambakhatta':0,'ouukhatta':0,'dahibundi':0,'khira':0,'khiree':0}
    if request.method == 'POST':
        print("inside special thali")
        items = request.form.getlist('item')
        session['special_prsd'] = items
        print(items)
        price = 0
        individual_price = 0
        sp_pr_list = []
        quantity = [request.form['qc1'],request.form['qc2'],request.form['qc3'],request.form['qc4'],request.form['qc5']]
        session['quantity'] = quantity
        if int(request.form['qc1']) + int(request.form['qc2']) + int(request.form['qc3']) + int(request.form['qc4']) + int(request.form['qc5']) > 0:
            for x in items:
                if x == y[0].item:
                    if int(request.form['qc1']) <= y[0].qty:
                        item_dict[x] = request.form['qc1']
                        price = price + int(request.form['qc1'])*int(y[0].price)
                        individual_price = int(request.form['qc1'])*int(y[0].price)
                        sp_pr_list.append(individual_price)
                        y[0].qty = y[0].qty - int(request.form['qc1'])
                if x == y[1].item:
                    if int(request.form['qc2']) <= y[1].qty:
                        item_dict[x] = request.form['qc2']
                        price = price + int(request.form['qc2'])*int(y[1].price)
                        individual_price = int(request.form['qc2'])*int(y[1].price)
                        sp_pr_list.append(individual_price)
                        y[1].qty = y[1].qty - int(request.form['qc2'])
                if x == y[2].item:
                    if int(request.form['qc3']) <= y[2].qty:
                        item_dict[x] = request.form['qc3']
                        price = price + int(request.form['qc3'])*int(y[2].price)
                        individual_price = int(request.form['qc3'])*int(y[2].price)
                        sp_pr_list.append(individual_price)
                        y[2].qty = y[2].qty - int(request.form['qc3'])
                if x == y[3].item:
                    if int(request.form['qc4']) <= y[3].qty:
                        item_dict[x] =  request.form['qc4']
                        price = price + int(request.form['qc4'])*int(y[3].price)
                        individual_price = int(request.form['qc4'])*int(y[3].price)
                        sp_pr_list.append(individual_price)
                        y[3].qty = y[3].qty - int(request.form['qc4'])
                if x == y[4].item:
                    if int(request.form['qc5']) <= y[4].qty:
                        item_dict[x] = request.form['qc5']
                        price = price + int(request.form['qc5'])*int(y[4].price)
                        individual_price = int(request.form['qc5'])*int(y[4].price)
                        sp_pr_list.append(individual_price)
                        y[4].qty = y[4].qty - int(request.form['qc5'])
            print("display the details",request.form['qc1'],request.form['qc2'],request.form['qc3'],request.form['qc4'],request.form['qc5'])
            session['sp_prasad_price'] = sp_pr_list
            session['type_of_service'] = request.form['service']
            session['sp_pay'] = price
            order_list = session.get('prasad_customer')
            print(order_list[0],order_list[1],order_list[2],order_list[3],order_list[4])
            print(session.get('prasad_customer'))
            session['item_dict_sp'] = item_dict
            if order_list[0]!='' or order_list[1]!='' or order_list[2]!='' or order_list[3]!='' or order_list[4]!='':
                return render_template('prepaymentbill.html',login_session = session.get('logged_in'),price = session.get('sp_pay'),item_price = session.get('sp_prasad_price'),msg = "Successfull",items = session.get('special_prsd'),item = items)
            return redirect('/bhoga')
        return render_template('specialprasadam.html',login_session = session.get('logged_in'),itm = y)
    return render_template("specialprasadam.html",login_session = session.get('logged_in'),itm = y)

@app.route('/prepaymentbillsp',methods = ['GET','POST'])
def bill_pay_sp():
    y = specialprasadmanager.query.all()
    if request.method == 'POST':
        order_list = session.get('prasad_customer')
        item_dict = session.get('item_dict_sp')
        items = session.get('special_prsd')
        quantity = session.get('quantity')
        for x in items:
            if x == y[0].item:
                if int(quantity[0]) <= y[0].qty:
                    y[0].qty = y[0].qty - int(quantity[0])
            if x == y[1].item:
                if int(quantity[1]) <= y[1].qty:
                    y[1].qty = y[1].qty - int(quantity[1])
            if x == y[2].item:
                if int(quantity[2]) <= y[2].qty:
                    y[2].qty = y[2].qty - int(quantity[2])
            if x == y[3].item:
                if int(quantity[3]) <= y[3].qty:
                    y[3].qty = y[3].qty - int(quantity[3])
            if x == y[4].item:
                if int(quantity[4]) <= y[4].qty:
                    y[4].qty = y[4].qty - int(quantity[4])
        sp_obj = all_prasadam( firstname = order_list[0],
                               lastname = order_list[1],
                               address = order_list[2],
                               email = order_list[3],
                               phone = order_list[4],
                               anna = item_dict['anna'],
                               kanika = item_dict['kanika'],
                               jerraanna = item_dict['jerraanna'],
                               oriyaanna = item_dict['oriyaanna'],
                               kamalaanna = item_dict['kamalaanna'],
                               gheeanna = item_dict['gheeanna'],
                               khichudi = item_dict['khichudi'],
                               haradadali = item_dict['haradadali'],
                               mugadali = item_dict['mugadali'],
                               haradadalma = item_dict['haradadalma'],
                               mugadalma = item_dict['mugadalma'],
                               puridalma = item_dict['puridalma'],
                               purimithadali = item_dict['purimithadali'],
                               butadali = item_dict['butadali'],
                               beshar = item_dict['beshar'],
                               sagamuga = item_dict['sagamuga'],
                               bhajachennatarkari = item_dict['bhajachennatarkari'],
                               panneertarkari = item_dict['panneertarkari'],
                               pannerbuta = item_dict['pannerbuta'],
                               mahura = item_dict['mahura'],
                               potalabesanatarkari = item_dict['potalabesanatarkari'],
                               potalarasha = item_dict['potalarasha'],
                               janhitarkari = item_dict['janhitarkari'],
                               butatarkari = item_dict['butatarkari'],
                               chips = item_dict['chips'],
                               kadalibhaja = item_dict['kadalibhaja'],
                               potalakurma = item_dict['potalakurma'],
                               ambularai = item_dict['ambularai'],
                               khajurikhatta = item_dict['khajurikhatta'],
                               dahibaigana = item_dict['dahibaigana'],
                               sapurikhatta = item_dict['sapurikhatta'],
                               fruitsalad = item_dict['fruitsalad'],
                               ambakhatta = item_dict['ambakhatta'],
                               ouukhatta = item_dict['ouukhatta'],
                               dahibundi = item_dict['dahibundi'],
                               khira = item_dict['khira'],
                               khiree = item_dict['khiree'],
                               price = session.get('sp_pay'),
                               type_of_order = session.get('type_of_service'),
                               date_of_order = datetime.datetime.now().date())
        db.session.add(sp_obj)
        db.session.commit()
        return render_template('prepaymentbill.html',login_session = session.get('logged_in'),price = session.get('sp_pay'),item_price = session.get('sp_prasad_price'),item = session.get('special_prsd'),items = session.get('special_prsd'))
    return render_template('prepaymentbill.html',login_session = session.get('logged_in'),price = session.get('sp_pay'),item_price = session.get('sp_prasad_price'),item = session.get('special_prsd'),items = session.get('special_prsd'))


@app.route('/functionprasad',methods = ['GET', 'POST'] )
def function_prasad():
    if request.method == 'POST':
        item_dict = {'anna':0,'kanika':0,'jerraanna':0,'oriyaanna':0,'kamalaanna':0,'gheeanna':0,'khichudi':0,
             'haradadali':0,'mugadali':0,'haradadalma':0,'mugadalma':0,'puridalma':0,'purimithadali':0,'butadali':0,
             'beshar':0,'sagamuga':0,'bhajachennatarkari':0,'panneertarkari':0,'pannerbuta':0,'mahura':0,'potalabesanatarkari':0,'potalarasha':0,
             'janhitarkari':0,'butatarkari':0,'chips':0,'kadalibhaja':0,'potalakurma':0,'ambularai':0,'khajurikhatta':0,'dahibaigana':0,'sapurikhatta':0,
             'fruitsalad':0,'ambakhatta':0,'ouukhatta':0,'dahibundi':0,'khira':0,'khiree':0}
        items = request.form.getlist('item')
        obj = foodprice.query.filter_by(id = 1).all()
        session['item_bulk'] = items
        qty = request.form['qty1']
        if int(qty) > 0:
            session['Q'] = qty
            price = 0
            individual_price_func = []
            ind_pr = 0
            for x in items:
                if x == "anna":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['anna'])*obj[0].anna
                    ind_pr = int(item_dict['anna'])*obj[0].anna
                    individual_price_func.append(ind_pr)
                if x == "kanika":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['kanika'])*obj[0].kanika
                    ind_pr = int(item_dict['kanika'])*obj[0].kanika
                    individual_price_func.append(ind_pr)
                if x == "jerraanna":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['jerraanna'])*obj[0].jerraanna
                    ind_pr = int(item_dict['jerraanna'])*obj[0].jerraanna
                    individual_price_func.append(ind_pr)
                if x == "oriyaanna":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['oriyaanna'])*obj[0].oriyaanna
                    ind_pr = int(item_dict['oriyaanna'])*obj[0].oriyaanna
                    individual_price_func.append(ind_pr)
                if x == "kamalaanna":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['kamalaanna'])*obj[0].kamalaanna
                    ind_pr = int(item_dict['kamalaanna'])*obj[0].kamalaanna
                    individual_price_func.append(ind_pr)
                if x == "gheeanna":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['gheeanna'])*obj[0].gheeanna
                    ind_pr = int(item_dict['gheeanna'])*obj[0].gheeanna
                    individual_price_func.append(ind_pr)
                if x == "khichudi":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['khichudi'])*obj[0].khichudi
                    ind_pr = int(item_dict['khichudi'])*obj[0].khichudi
                    individual_price_func.append(ind_pr)
                if x == "haradadali":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['haradadali'])*obj[0].haradadali
                    ind_pr = int(item_dict['haradadali'])*obj[0].haradadali
                    individual_price_func.append(ind_pr)
                if x == "mugadali":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['mugadali'])*obj[0].mugadali
                    ind_pr = int(item_dict['mugadali'])*obj[0].mugadali
                    individual_price_func.append(ind_pr)
                if x == "haradadalma":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['haradadalma'])*obj[0].haradadalma
                    ind_pr = int(item_dict['haradadalma'])*obj[0].haradadalma
                    individual_price_func.append(ind_pr)
                if x == "mugadalma":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['mugadalma'])*obj[0].mugadalma
                    ind_pr = int(item_dict['mugadalma'])*obj[0].mugadalma
                    individual_price_func.append(ind_pr)
                if x == "puridalma":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['puridalma'])*obj[0].puridalma
                    ind_pr = int(item_dict['puridalma'])*obj[0].puridalma
                    individual_price_func.append(ind_pr)
                if x == "purimithadali":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['purimithadali'])*obj[0].purimithadali
                    ind_pr = int(item_dict['purimithadali'])*obj[0].purimithadali
                    individual_price_func.append(ind_pr)
                if x == "butadali":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['butadali'])*obj[0].butadali
                    ind_pr = int(item_dict['butadali'])*obj[0].butadali
                    individual_price_func.append(ind_pr)
                if x == "beshar":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['beshar'])*obj[0].beshar
                    ind_pr = int(item_dict['beshar'])*obj[0].beshar
                    individual_price_func.append(ind_pr)
                if x == "sagamuga":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['sagamuga'])*obj[0].sagamuga
                    ind_pr = int(item_dict['sagamuga'])*obj[0].sagamuga
                    individual_price_func.append(ind_pr)
                if x == "bhajachennatarkari":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['bhajachennatarkari'])*obj[0].bhajachennatarkari
                    ind_pr = int(item_dict['bhajachennatarkari'])*obj[0].bhajachennatarkari
                    individual_price_func.append(ind_pr)
                if x == "panneertarkari":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['panneertarkari'])*obj[0].panneertarkari
                    ind_pr = int(item_dict['panneertarkari'])*obj[0].panneertarkari
                    individual_price_func.append(ind_pr)
                if x == "pannerbuta":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['pannerbuta'])*obj[0].pannerbuta
                    ind_pr = int(item_dict['pannerbuta'])*obj[0].pannerbuta
                    individual_price_func.append(ind_pr)
                if x == "mahura":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['mahura'])*obj[0].mahura
                    ind_pr = int(item_dict['mahura'])*obj[0].mahura
                    individual_price_func.append(ind_pr)
                if x == "potalabesanatarkari":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['potalabesanatarkari'])*obj[0].potalabesanatarkari
                    ind_pr = int(item_dict['potalabesanatarkari'])*obj[0].potalabesanatarkari
                    individual_price_func.append(ind_pr)
                if x == "potalarasha":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['potalarasha'])*obj[0].potalarasha
                    ind_pr = int(item_dict['potalarasha'])*obj[0].potalarasha
                    individual_price_func.append(ind_pr)
                if x == "janhitarkari":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['janhitarkari'])*obj[0].janhitarkari
                    ind_pr = int(item_dict['janhitarkari'])*obj[0].janhitarkari
                    individual_price_func.append(ind_pr)
                if x == "butatarkari":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['butatarkari'])*obj[0].butatarkari
                    ind_pr = int(item_dict['butatarkari'])*obj[0].butatarkari
                    individual_price_func.append(ind_pr)
                if x == "chips":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['chips'])*obj[0].chips
                    ind_pr = int(item_dict['chips'])*obj[0].chips
                    individual_price_func.append(ind_pr)
                if x == "kadalibhaja":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['kadalibhaja'])*obj[0].kadalibhaja
                    ind_pr = int(item_dict['kadalibhaja'])*obj[0].kadalibhaja
                    individual_price_func.append(ind_pr)
                if x == "potalakurma":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['potalakurma'])*obj[0].potalakurma
                    ind_pr = int(item_dict['potalakurma'])*obj[0].potalakurma
                    individual_price_func.append(ind_pr)
                if x == "ambularai":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['ambularai'])*obj[0].ambularai
                    ind_pr = int(item_dict['ambularai'])*obj[0].ambularai
                    individual_price_func.append(ind_pr)
                if x == "khajurikhatta":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['khajurikhatta'])*obj[0].khajurikhatta
                    ind_pr = int(item_dict['khajurikhatta'])*obj[0].khajurikhatta
                    individual_price_func.append(ind_pr)
                if x == "dahibaigana":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['dahibaigana'])*obj[0].dahibaigana
                    ind_pr = int(item_dict['dahibaigana'])*obj[0].dahibaigana
                    individual_price_func.append(ind_pr)
                if x == "sapurikhatta":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['sapurikhatta'])*obj[0].sapurikhatta
                    ind_pr = int(item_dict['sapurikhatta'])*obj[0].sapurikhatta
                    individual_price_func.append(ind_pr)
                if x == "fruitsalad":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['fruitsalad'])*obj[0].fruitsalad
                    ind_pr = int(item_dict['fruitsalad'])*obj[0].fruitsalad
                    individual_price_func.append(ind_pr)
                if x == "ambakhatta":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['ambakhatta'])*obj[0].ambakhatta
                    ind_pr = int(item_dict['ambakhatta'])*obj[0].ambakhatta
                    individual_price_func.append(ind_pr)
                if x == "ouukhatta":
                    item_dict[x] =  request.form['qty1']
                    price = price + int(item_dict['ouukhatta'])*obj[0].ouukhatta
                    ind_pr = int(item_dict['ouukhatta'])*obj[0].ouukhatta
                    individual_price_func.append(ind_pr)
                if x == "dahibundi":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['dahibundi'])*obj[0].dahibundi
                    ind_pr = int(item_dict['dahibundi'])*obj[0].dahibundi
                    individual_price_func.append(ind_pr)
                if x == "khira":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['khira'])*obj[0].khira
                    ind_pr = int(item_dict['khira'])*obj[0].khira
                    individual_price_func.append(ind_pr)
                if x == "khiree":
                    item_dict[x] = request.form['qty1']
                    price = price + int(item_dict['khiree'])*obj[0].khiree
                    ind_pr = int(item_dict['khiree'])*obj[0].khiree
                    individual_price_func.append(ind_pr)
            session['func_pay'] = price
            session['func_price'] = individual_price_func
            order_list = session.get('prasad_customer')
            session['item_dict_party'] = item_dict
            print(session.get('prasad_customer'))
            if order_list[0]!='' or order_list[1]!='' or order_list[2]!='' or order_list[3]!='' or order_list[4]!='':
                return render_template('prepaymentpartybill.html',login_session = session.get('logged_in'),msg = "successfull !!",price = session.get('func_pay'),items = zip(session.get('item_bulk'),session.get('func_price')))
        return redirect('/')
    return render_template('functionprasadam.html',obj = foodprice.query.all())


@app.route('/functionbill',methods = ['GET','POST'])
def bill_pay_func():
    if request.method == 'POST':
        item_dict = session.get('item_dict_party')
        order_list = session.get('prasad_customer')
        func_obj = all_prasadam(firstname = order_list[0],
                                   lastname = order_list[1],
                                   address = order_list[2],
                                   email = order_list[3],
                                   phone = order_list[4],
                                   anna = item_dict['anna'],
                                   kanika = item_dict['kanika'],
                                   jerraanna = item_dict['jerraanna'],
                                   oriyaanna = item_dict['oriyaanna'],
                                   kamalaanna = item_dict['kamalaanna'],
                                   gheeanna = item_dict['gheeanna'],
                                   khichudi = item_dict['khichudi'],
                                   haradadali = item_dict['haradadali'],
                                   mugadali = item_dict['mugadali'],
                                   haradadalma = item_dict['haradadalma'],
                                   mugadalma = item_dict['mugadalma'],
                                   puridalma = item_dict['puridalma'],
                                   purimithadali = item_dict['purimithadali'],
                                   butadali = item_dict['butadali'],
                                   beshar = item_dict['beshar'],
                                   sagamuga = item_dict['sagamuga'],
                                   bhajachennatarkari = item_dict['bhajachennatarkari'],
                                   panneertarkari = item_dict['panneertarkari'],
                                   pannerbuta = item_dict['pannerbuta'],
                                   mahura = item_dict['mahura'],
                                   potalabesanatarkari = item_dict['potalabesanatarkari'],
                                   potalarasha = item_dict['potalarasha'],
                                   janhitarkari = item_dict['janhitarkari'],
                                   butatarkari = item_dict['butatarkari'],
                                   chips = item_dict['chips'],
                                   kadalibhaja = item_dict['kadalibhaja'],
                                   potalakurma = item_dict['potalakurma'],
                                   ambularai = item_dict['ambularai'],
                                   khajurikhatta = item_dict['khajurikhatta'],
                                   dahibaigana = item_dict['dahibaigana'],
                                   sapurikhatta = item_dict['sapurikhatta'],
                                   fruitsalad = item_dict['fruitsalad'],
                                   ambakhatta = item_dict['ambakhatta'],
                                   ouukhatta = item_dict['ouukhatta'],
                                   dahibundi = item_dict['dahibundi'],
                                   khira = item_dict['khira'],
                                   khiree = item_dict['khiree'],
                                   price =  session.get('func_pay'),
                                   type_of_order = "Temple Premise",
                                   date_of_order = datetime.datetime.now().date())
        db.session.add(func_obj)
        db.session.commit()
        return render_template('prepaymentpartybill.html',login_session = session.get('logged_in'),price = session.get('func_pay'),items = zip(session.get('item_bulk'),session.get('func_price')))
    return render_template('prepaymenpartytbill.html',login_session = session.get('logged_in'),price = session.get('func_pay'),items = zip(session.get('item_bulk'),session.get('func_price')))



@app.route('/hall',methods = ['GET','POST'])
def hall():
    print("Outside hall post!!!")
    if request.method == 'POST':
        print("Inside hall post but outside status!!!")
        lit = ['unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied']
        status = hallbook.query.all()
        date = request.form['date']
        session['date_of_event'] = date
        print("date session created")
        print(status)
        if status:
            print("Inside as status exists")
            for x in status:
                print("Inside status!!!")
                print("request date",date)
                print("database date",x.date)
                if str(x.date) == str(date):
                    print("Inside date match!!!")
                    print(x)
                    print(x.date,x.hall1_slot1,x.hall1_slot2,x.hall2_slot1,x.hall2_slot2,x.hall3_slot1,x.hall3_slot2,x.hall4_slot1,x.hall4_slot2)
                    if  x.hall1_slot1 != 'unoccupied':
                        lit[0] = x.hall1_slot1    
                    if  x.hall1_slot2 != 'unoccupied':
                        lit[1] = x.hall1_slot2
                    if  x.hall2_slot1 != 'unoccupied':
                        lit[2] = x.hall2_slot1
                    if  x.hall2_slot2 != 'unoccupied':
                        lit[3] = x.hall2_slot2
                    if  x.hall3_slot1 != 'unoccupied':
                        lit[4] = x.hall3_slot1
                    if  x.hall3_slot2 != 'unoccupied':
                        lit[5] = x.hall3_slot2
                    if  x.hall4_slot1 != 'unoccupied':
                        lit[6] = x.hall4_slot1
                    if  x.hall4_slot2 != 'unoccupied':
                        lit[7] = x.hall4_slot2
                    if x.room_1 != 'unoccupied':
                        lit[8] = x.room_1
                    if x.room_2 != 'unoccupied':
                        lit[9] = x.room_2
                    if x.room_3 != 'unoccupied':
                        lit[10] = x.room_3
                    if x.room_4 != 'unoccupied':
                        lit[11] = x.room_4
                    print("lit value into session",lit)
                    session['anada_bazar'] = lit
                else:
                    print("date doesn't match!!")
                    print("lit value into session",lit)
                    session['anada_bazar'] = lit
            return render_template('hall2.html',price_hall = halldetails.query.all(),obj = foodprice.query.all(),login_session = session.get('logged_in'),kk = session.get('anada_bazar'))
        else:
            print("status doesn't exist")
            print("lit value into session",lit)
            session['anada_bazar'] = lit
            return render_template('hall2.html',price_hall = halldetails.query.all(),obj = foodprice.query.all(),login_session = session.get('logged_in'),kk = session.get('anada_bazar'))
    return render_template('hallnewpage.html',login_session = session.get('logged_in'))

@app.route('/hallop',methods = ['GET','POST'])
def hall_op():
    if request.method == 'POST':
        item_dict = {'anna':0,'kanika':0,'jerraanna':0,'oriyaanna':0,'kamalaanna':0,'gheeanna':0,'khichudi':0,
             'haradadali':0,'mugadali':0,'haradadalma':0,'mugadalma':0,'puridalma':0,'purimithadali':0,'butadali':0,
             'beshar':0,'sagamuga':0,'bhajachennatarkari':0,'panneertarkari':0,'pannerbuta':0,'mahura':0,'potalabesanatarkari':0,'potalarasha':0,
             'janhitarkari':0,'butatarkari':0,'chips':0,'kadalibhaja':0,'potalakurma':0,'ambularai':0,'khajurikhatta':0,'dahibaigana':0,'sapurikhatta':0,
             'fruitsalad':0,'ambakhatta':0,'ouukhatta':0,'dahibundi':0,'khira':0,'khiree':0}
        hall = request.form.getlist('hall')
        print(hall)
        room = request.form.getlist('room')
        print(room)
        deco = request.form.getlist('deco')
        print(deco)
        slots = request.form.getlist('slot')
        print(slots)
        items = request.form.getlist('item')
        print(items)
        obj = foodprice.query.all()
        session['slot'] = slots
        session['hall'] = hall
        session['room'] = room
        session['deco'] = deco
        session['itemparty'] =items
        price = 0
        individual_price_func = []
        ind_pr = 0
        for x in items:
            if x == "anna":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['anna'])*obj[0].anna
                ind_pr = int(item_dict['anna'])*obj[0].anna
                individual_price_func.append(ind_pr)
            if x == "kanika":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['kanika'])*obj[0].kanika
                ind_pr = int(item_dict['kanika'])*obj[0].kanika
                individual_price_func.append(ind_pr)
            if x == "jerraanna":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['jerraanna'])*obj[0].jerraanna
                ind_pr = int(item_dict['jerraanna'])*obj[0].jerraanna
                individual_price_func.append(ind_pr)
            if x == "oriyaanna":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['oriyaanna'])*obj[0].oriyaanna
                ind_pr = int(item_dict['oriyaanna'])*obj[0].oriyaanna
                individual_price_func.append(ind_pr)
            if x == "kamalaanna":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['kamalaanna'])*obj[0].kamalaanna
                ind_pr = int(item_dict['kamalaanna'])*obj[0].kamalaanna
                individual_price_func.append(ind_pr)
            if x == "gheeanna":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['gheeanna'])*obj[0].gheeanna
                ind_pr = int(item_dict['gheeanna'])*obj[0].gheeanna
                individual_price_func.append(ind_pr)
            if x == "khichudi":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['khichudi'])*obj[0].khichudi
                ind_pr = int(item_dict['khichudi'])*obj[0].khichudi
                individual_price_func.append(ind_pr)
            if x == "haradadali":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['haradadali'])*obj[0].haradadali
                ind_pr = int(item_dict['haradadali'])*obj[0].haradadali
                individual_price_func.append(ind_pr)
            if x == "mugadali":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['mugadali'])*obj[0].mugadali
                ind_pr = int(item_dict['mugadali'])*obj[0].mugadali
                individual_price_func.append(ind_pr)
            if x == "haradadalma":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['haradadalma'])*obj[0].haradadalma
                ind_pr = int(item_dict['haradadalma'])*obj[0].haradadalma
                individual_price_func.append(ind_pr)
            if x == "mugadalma":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['mugadalma'])*obj[0].mugadalma
                ind_pr = int(item_dict['mugadalma'])*obj[0].mugadalma
                individual_price_func.append(ind_pr)
            if x == "puridalma":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['puridalma'])*obj[0].puridalma
                ind_pr = int(item_dict['puridalma'])*obj[0].puridalma
                individual_price_func.append(ind_pr)
            if x == "purimithadali":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['purimithadali'])*obj[0].purimithadali
                ind_pr = int(item_dict['purimithadali'])*obj[0].purimithadali
                individual_price_func.append(ind_pr)
            if x == "butadali":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['butadali'])*obj[0].butadali
                ind_pr = int(item_dict['butadali'])*obj[0].butadali
                individual_price_func.append(ind_pr)
            if x == "beshar":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['beshar'])*obj[0].beshar
                ind_pr = int(item_dict['beshar'])*obj[0].beshar
                individual_price_func.append(ind_pr)
            if x == "sagamuga":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['sagamuga'])*obj[0].sagamuga
                ind_pr = int(item_dict['sagamuga'])*obj[0].sagamuga
                individual_price_func.append(ind_pr)
            if x == "bhajachennatarkari":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['bhajachennatarkari'])*obj[0].bhajachennatarkari
                ind_pr = int(item_dict['bhajachennatarkari'])*obj[0].bhajachennatarkari
                individual_price_func.append(ind_pr)
            if x == "panneertarkari":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['panneertarkari'])*obj[0].panneertarkari
                ind_pr = int(item_dict['panneertarkari'])*obj[0].panneertarkari
                individual_price_func.append(ind_pr)
            if x == "pannerbuta":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['pannerbuta'])*obj[0].pannerbuta
                ind_pr = int(item_dict['pannerbuta'])*obj[0].pannerbuta
                individual_price_func.append(ind_pr)
            if x == "mahura":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['mahura'])*obj[0].mahura
                ind_pr = int(item_dict['mahura'])*obj[0].mahura
                individual_price_func.append(ind_pr)
            if x == "potalabesanatarkari":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['potalabesanatarkari'])*obj[0].potalabesanatarkari
                ind_pr = int(item_dict['potalabesanatarkari'])*obj[0].potalabesanatarkari
                individual_price_func.append(ind_pr)
            if x == "potalarasha":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['potalarasha'])*obj[0].potalarasha
                ind_pr = int(item_dict['potalarasha'])*obj[0].potalarasha
                individual_price_func.append(ind_pr)
            if x == "janhitarkari":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['janhitarkari'])*obj[0].janhitarkari
                ind_pr = int(item_dict['janhitarkari'])*obj[0].janhitarkari
                individual_price_func.append(ind_pr)
            if x == "butatarkari":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['butatarkari'])*obj[0].butatarkari
                ind_pr = int(item_dict['butatarkari'])*obj[0].butatarkari
                individual_price_func.append(ind_pr)
            if x == "chips":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['chips'])*obj[0].chips
                ind_pr = int(item_dict['chips'])*obj[0].chips
                individual_price_func.append(ind_pr)
            if x == "kadalibhaja":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['kadalibhaja'])*obj[0].kadalibhaja
                ind_pr = int(item_dict['kadalibhaja'])*obj[0].kadalibhaja
                individual_price_func.append(ind_pr)
            if x == "potalakurma":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['potalakurma'])*obj[0].potalakurma
                ind_pr = int(item_dict['potalakurma'])*obj[0].potalakurma
                individual_price_func.append(ind_pr)
            if x == "ambularai":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['ambularai'])*obj[0].ambularai
                ind_pr = int(item_dict['ambularai'])*obj[0].ambularai
                individual_price_func.append(ind_pr)
            if x == "khajurikhatta":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['khajurikhatta'])*obj[0].khajurikhatta
                ind_pr = int(item_dict['khajurikhatta'])*obj[0].khajurikhatta
                individual_price_func.append(ind_pr)
            if x == "dahibaigana":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['dahibaigana'])*obj[0].dahibaigana
                ind_pr = int(item_dict['dahibaigana'])*obj[0].dahibaigana
                individual_price_func.append(ind_pr)
            if x == "sapurikhatta":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['sapurikhatta'])*obj[0].sapurikhatta
                ind_pr = int(item_dict['sapurikhatta'])*obj[0].sapurikhatta
                individual_price_func.append(ind_pr)
            if x == "fruitsalad":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['fruitsalad'])*obj[0].fruitsalad
                ind_pr = int(item_dict['fruitsalad'])*obj[0].fruitsalad
                individual_price_func.append(ind_pr)
            if x == "ambakhatta":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['ambakhatta'])*obj[0].ambakhatta
                ind_pr = int(item_dict['ambakhatta'])*obj[0].ambakhatta
                individual_price_func.append(ind_pr)
            if x == "ouukhatta":
                item_dict[x] =  request.form['qty1']
                price = price + int(item_dict['ouukhatta'])*obj[0].ouukhatta
                ind_pr = int(item_dict['ouukhatta'])*obj[0].ouukhatta
                individual_price_func.append(ind_pr)
            if x == "dahibundi":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['dahibundi'])*obj[0].dahibundi
                ind_pr = int(item_dict['dahibundi'])*obj[0].dahibundi
                individual_price_func.append(ind_pr)
            if x == "khira":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['khira'])*obj[0].khira
                ind_pr = int(item_dict['khira'])*obj[0].khira
                individual_price_func.append(ind_pr)
            if x == "khiree":
                item_dict[x] = request.form['qty1']
                price = price + int(item_dict['khiree'])*obj[0].khiree
                ind_pr = int(item_dict['khiree'])*obj[0].khiree
                individual_price_func.append(ind_pr)
        session['func_pay'] = price
        session['func_price'] = individual_price_func
        session['nofg'] = request.form['qty1']
        lit_check = ['unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied']
        lit = session.get('anada_bazar')
        if hall:
            lit_check = ['unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied','unoccupied']
            lit = session.get('anada_bazar')
            for xt in hall:
                for slot in slots:
                        if xt == "hall1" and slot == '11':
                          lit_check[0] = 'occupied'  
                        elif xt == "hall1" and slot == '12':
                            lit_check[1] = 'occupied'
                        elif xt == "hall1" and slot == '13':
                            lit_check[0] = 'occupied'
                            lit_check[1] = 'occupied'
                        elif xt == "hall2" and slot == '21':
                            lit_check[2] = 'occupied'
                        elif xt == "hall2" and slot == '22':
                            lit_check[3] = 'occupied'
                        elif xt == "hall2" and slot == '23':
                            lit_check[2] = 'occupied'
                            lit_check[3] = 'occupied'
                        elif xt == "hall3" and slot == '31':
                            lit_check[4] = 'occupied'
                        elif xt == "hall3" and slot == '32':
                            lit_check[5] = 'occupied'
                        elif xt == "hall3" and slot == '33':
                            lit_check[4] = 'occupied'
                            lit_check[5] = 'occupied'
                        elif xt == "hall4" and slot == '41':
                            lit_check[6] = 'occupied'
                        elif xt == "hall4" and slot == '42':
                            lit_check[7] = 'occupied'
                        elif xt == "hall4" and slot == '43':
                            lit_check[6] = 'occupied'
                            lit_check[7] = 'occupied'
            for yt in room:
                if yt == 'room1':
                    lit_check[8] = 'occupied'
                elif yt == 'room2':
                    lit_check[9] = 'occupied'
                elif yt == 'room3':
                    lit_check[10] = 'occupied'
                else:
                    lit_check[11] = 'occupied'
            session['lit_check'] = lit_check
            print("lit:",lit)
            print("lit_check:",lit_check)
            for i in range(0,10):
                if lit[i] == lit_check[i] and lit[i]=='occupied' and lit_check[i]=='occupied':
                    return render_template('hall2.html',price_hall = halldetails.query.all(),obj = foodprice.query.all(),login_session = session.get('logged_in'),kk = session.get('anada_bazar'))
            if session.get('date_of_event'):
                return render_template('hallform.html',login_session = session.get('logged_in'),qty = session.get('nofg'))
            else:
                return render_template('hallnewpage.html',login_session = session.get('logged_in'))
    return render_template('hall2.html',price_hall = halldetails.query.all(),obj = foodprice.query.all(),login_session = session.get('logged_in'),kk =session.get('anada_bazar'))

@app.route('/existing_hall',methods = ['GET','POST'])
def existing_hallbook():
    if request.method == 'POST':
        liii = []
        check_db = hallbook_details.query.all()
        if check_db:
            for x in check_db:
                if x.mobile == request.form['phone']:
                    liii.append(x.fname)
                    liii.append(x.lname)
                    liii.append(x.address)
                    liii.append(x.email)
                    liii.append(x.mobile)
                    liii.append(session.get('nofg'))
                    session['liii'] = liii
                    liii = []
                    return render_template('hallform.html',login_session = session.get('logged_in'),liii = session.get('liii'),date = session.get('date_of_event'),qty = session.get('nofg'))
        else:
            return render_template('hallform.html',login_session = session.get('logged_in'))
    return render_template('existing_hall.html',login_session = session.get('logged_in'))



@app.route('/hallform',methods = ['GET','POST'])
def hall_book():
    print("Outside hall book")
    if request.method == 'POST':
        print("Inside hall_book")
        lit_check = session.get('lit_check')
        print("lit_check session created")
        db_checks = hallbook.query.filter_by(date = session.get('date_of_event')).all()
        print(db_checks)
        deco_list = ['null','null','null']
        print("fetched db_check")
        lit = session.get('anada_bazar')
        if db_checks:
            print("if db_check")
            for db_check in db_checks:
                print("Inside for loop db_check")
                if lit_check[0] == "occupied":
                    lit_check[0] = db_check.hall1_slot1
                elif lit_check[1] == "occupied":
                    lit_check[1] = db_check.hall1_slot2
                elif lit_check[2] == "occupied":
                    lit_check[2] = db_check.hall2_slot1
                elif lit_check[3] == "occupied":
                    lit_check[3] = db_check.hall2_slot2
                elif lit_check[4] == "occupied":
                    lit_check[4] = db_check.hall3_slot1
                elif lit_check[5] == "occupied":
                    lit_check[5] = db_check.hall3_slot2
                elif lit_check[6] == "occupied":
                    lit_check[6] = db_check.hall4_slot1
                elif lit_check[7] == "occupied":
                    lit_check[7] = db_check.hall4_slot2
                elif lit_check[8] == "occupied":
                    lit_check[8] = db_check.room_1
                elif lit_check[9] == "occupied":
                    lit_check[9] = db_check.room_2
                elif lit_check[10] == "occupied":
                    lit_check[10] = db_check.room_3
                elif lit_check[11] == "occupied":
                    lit_check[11] = db_check.room_4
        x = session.get('hall')    
        y = session.get('room')
        z = session.get('deco')
        slots = session.get('slot')
        hall_price = halldetails.query.get(1)
        total_price = 0
        for xt in x:
            for slot in slots:
                print("Inside slots and halls")
                if xt == "hall1" and slot == '11':
                    lit[0] = request.form['fname']
                    total_price = total_price + hall_price.hall1_slot1
                elif xt == "hall1" and slot == '12':
                    lit[1] = request.form['fname']
                    total_price = total_price + hall_price.hall1_slot2
                elif xt == "hall1" and slot == '13':
                    lit[0] = request.form['fname']
                    lit[1] = request.form['fname']
                    total_price = total_price + hall_price.hall1_slot1 + hall_price.hall1_slot2
                elif xt == "hall2" and slot == '21':
                    lit[2] = request.form['fname']
                    total_price = total_price + hall_price.hall2_slot1
                elif xt == "hall2" and slot == '22':
                    lit[3] = request.form['fname']
                    total_price = total_price + hall_price.hall2_slot2
                elif xt == "hall2" and slot == '23':
                    lit[2] = request.form['fname']
                    lit[3] = request.form['fname']
                    total_price = total_price + hall_price.hall2_slot1 + hall_price.hall2_slot2
                elif xt == "hall3" and slot == '31':
                    lit[4] = request.form['fname']
                    total_price = total_price + hall_price.hall3_slot1
                elif xt == "hall3" and slot == '32':
                    lit[5] = request.form['fname']
                    total_price = total_price + hall_price.hall3_slot2
                elif xt == "hall3" and slot == '33':
                    lit[4] = request.form['fname']
                    lit[5] = request.form['fname']
                    total_price = total_price + hall_price.hall3_slot1 + hall_price.hall3_slot2
                elif xt == "hall4" and slot == '41':
                    lit[6] = request.form['fname']
                    total_price = total_price + hall_price.hall4_slot1
                elif xt == "hall4" and slot == '42':
                    lit[7] = request.form['fname']
                    total_price = total_price + hall_price.hall4_slot2
                elif xt == "hall4" and slot == '43':
                    lit[6] = request.form['fname']
                    lit[7] = request.form['fname']
                    total_price = total_price + hall_price.hall4_slot1 + hall_price.hall4_slot2
        for yt in y:
            if yt == 'room1':
                lit[8] = request.form['fname']
                total_price = total_price + hall_price.room_1
            if yt == 'room2':
                lit[9] = request.form['fname']
                total_price = total_price + hall_price.room_2
            if yt == 'room3':
                lit[10] = request.form['fname']
                total_price = total_price + hall_price.room_3
            if yt == 'room4':
                lit[11] = request.form['fname']
                total_price = total_price + hall_price.room_4
        for zx in z:
            if zx == 'deco1':
                deco_list[0] = request.form['fname']
                total_price = total_price + hall_price.deco1
            elif zx == 'deco2':
                deco_list[1] = request.form['fname']
                total_price = total_price + hall_price.deco2
            else:
                deco_list[2] = request.form['fname']
                total_price = total_price + hall_price.deco3
        print("Outside iterative looping")
        print("check lit_check",lit)
        session['hall_list_room_list'] = lit
        session['deco_list'] = deco_list
        session['hall_budget'] = total_price
        print("hall,rooom,deco session creeated")
        liii =[request.form['fname'],request.form['lname'],request.form['address'],request.form['email'],request.form['mobile'],request.form['nofg']]
        print(liii)
        session['liii'] = liii
        liii = session.get('liii')
        print("just before rendering template billing")
        return render_template('billing.html',hall_price = session.get('hall_budget') + session.get('func_pay'),login_session = session.get('logged_in'),liii = liii,date = session.get('date_of_event'),items = zip(session.get('itemparty'),session.get('func_price')),hall = session.get('hall'),slot = session.get('slot'),room = session.get('room'),deco = session.get('deco'))
    return render_template('hallform.html',login_session = session.get('logged_in'))
        
@app.route('/billing',methods = ['GET','POST'])
def billing():
    if request.method == "POST":
        liii = session.get('liii')
        liii.append(session.get('nofg'))
        lit_check = session.get('hall_list_room_list')
        deco_list = session.get('deco_list')
        print(lit_check)
        print(deco_list)
        check_db = hallbook.query.all()
        if check_db:
            for x in check_db:
                print("inside check db for loop")
                if session.get('date_of_event') == x.date:
                    print("date found")
                    x.date = session.get('date_of_event')
                    #if x.hall1_slot1 == "unoccupied":
                    x.hall1_slot1 = lit_check[0]
                    #if x.hall1_slot2 == "unoccupied":
                    x.hall1_slot2 = lit_check[1]
                    #if x.hall2_slot1 == "unoccupied":
                    x.hall2_slot2 = lit_check[2]
                    #if x.hall2_slot2 == "unoccupied":
                    x.hall2_slot2 = lit_check[3]
                    #if x.hall3_slot1 == "unoccupied":
                    x.hall3_slot1 = lit_check[4]
                    #if x.hall3_slot2 == "unoccupied":
                    x.hall3_slot2 = lit_check[5]
                    #if x.hall4_slot1 == "unoccupied":
                    x.hall4_slot1 = lit_check[6]
                    #if x.hall4_slot2 == "unoccupied":
                    x.hall4_slot2 = lit_check[7]
                    break
                else:
                    print("date not found")
                    obj = hallbook(date = session.get('date_of_event'),
                           hall1_slot1 = lit_check[0],
                           hall1_slot2 = lit_check[1],
                           hall2_slot1 = lit_check[2],
                           hall2_slot2 = lit_check[3],
                           hall3_slot1 = lit_check[4],
                           hall3_slot2 = lit_check[5],
                           hall4_slot1 = lit_check[6],
                           hall4_slot2 = lit_check[7],
                           room_1 = lit_check[8],
                           room_2 = lit_check[9],
                           room_3 = lit_check[10],
                           room_4 = lit_check[11],
                           deco1 = deco_list[0],
                           deco2 = deco_list[1],
                           deco3 = deco_list[2])
                    db.session.add(obj)
                    break
        else:
            print("first object")
            obj = hallbook(date = session.get('date_of_event'),
                           hall1_slot1 = lit_check[0],
                           hall1_slot2 = lit_check[1],
                           hall2_slot1 = lit_check[2],
                           hall2_slot2 = lit_check[3],
                           hall3_slot1 = lit_check[4],
                           hall3_slot2 = lit_check[5],
                           hall4_slot1 = lit_check[6],
                           hall4_slot2 = lit_check[7],
                           room_1 = lit_check[8],
                           room_2 = lit_check[9],
                           room_3 = lit_check[10],
                           room_4 = lit_check[11],
                           deco1 = deco_list[0],
                           deco2 = deco_list[1],
                           deco3 = deco_list[2])
            db.session.add(obj)
        objj = hallbook_details(fname = liii[0],
                                lname = liii[1],
                                address = liii[2],
                                email = liii[3],
                                mobile = liii[4],
                                nfg = liii[5],
                                date_of_book = session.get('date_of_event'))
        item = session.get('itemparty')
        item_dict = {'anna':0,'kanika':0,'jerraanna':0,'oriyaanna':0,'kamalaanna':0,'gheeanna':0,'khichudi':0,
             'haradadali':0,'mugadali':0,'haradadalma':0,'mugadalma':0,'puridalma':0,'purimithadali':0,'butadali':0,
             'beshar':0,'sagamuga':0,'bhajachennatarkari':0,'panneertarkari':0,'pannerbuta':0,'mahura':0,'potalabesanatarkari':0,'potalarasha':0,
             'janhitarkari':0,'butatarkari':0,'chips':0,'kadalibhaja':0,'potalakurma':0,'ambularai':0,'khajurikhatta':0,'dahibaigana':0,'sapurikhatta':0,
             'fruitsalad':0,'ambakhatta':0,'ouukhatta':0,'dahibundi':0,'khira':0,'khiree':0}
        for x in item:
            item_dict[x] = session.get('nofg')
            
        func_obj = all_prasadam(firstname = liii[0],
                               lastname = liii[1],
                               address = liii[2],
                               email = liii[3],
                               phone = liii[4],
                               anna = item_dict['anna'],
                               kanika = item_dict['kanika'],
                               jerraanna = item_dict['jerraanna'],
                               oriyaanna = item_dict['oriyaanna'],
                               kamalaanna = item_dict['kamalaanna'],
                               gheeanna = item_dict['gheeanna'],
                               khichudi = item_dict['khichudi'],
                               haradadali = item_dict['haradadali'],
                               mugadali = item_dict['mugadali'],
                               haradadalma = item_dict['haradadalma'],
                               mugadalma = item_dict['mugadalma'],
                               puridalma = item_dict['puridalma'],
                               purimithadali = item_dict['purimithadali'],
                               butadali = item_dict['butadali'],
                               beshar = item_dict['beshar'],
                               sagamuga = item_dict['sagamuga'],
                               bhajachennatarkari = item_dict['bhajachennatarkari'],
                               panneertarkari = item_dict['panneertarkari'],
                               pannerbuta = item_dict['pannerbuta'],
                               mahura = item_dict['mahura'],
                               potalabesanatarkari = item_dict['potalabesanatarkari'],
                               potalarasha = item_dict['potalarasha'],
                               janhitarkari = item_dict['janhitarkari'],
                               butatarkari = item_dict['butatarkari'],
                               chips = item_dict['chips'],
                               kadalibhaja = item_dict['kadalibhaja'],
                               potalakurma = item_dict['potalakurma'],
                               ambularai = item_dict['ambularai'],
                               khajurikhatta = item_dict['khajurikhatta'],
                               dahibaigana = item_dict['dahibaigana'],
                               sapurikhatta = item_dict['sapurikhatta'],
                               fruitsalad = item_dict['fruitsalad'],
                               ambakhatta = item_dict['ambakhatta'],
                               ouukhatta = item_dict['ouukhatta'],
                               dahibundi = item_dict['dahibundi'],
                               khira = item_dict['khira'],
                               khiree = item_dict['khiree'],
                               price =  session.get('func_pay'),
                               type_of_order = "At Temple",
                               date_of_order = session.get('date_of_event'))
        db.session.add(func_obj)
        items = zip(session.get('itemparty'),session.get('func_price'))    
        for x,y in items:
            print(x,"-->",y)    
        db.session.add(objj)
        db.session.commit()
        liii = []
        return render_template('billing.html',hall_price = session.get('hall_budget') + session.get('func_pay'),login_session = session.get('logged_in'),liii = session.get('liii'),date = session.get('date_of_event'),items = zip(session.get('itemparty'),session.get('func_price')),hall = session.get('hall'),slot = session.get('slot'),room = session.get('room'),deco = session.get('deco'))
    return render_template('billing.html',hall_price = session.get('hall_budget') + session.get('func_pay'),login_session = session.get('logged_in'),liii = session.get('liii'),date = session.get('date_of_event'),items = zip(session.get('itemparty'),session.get('func_price')),hall = session.get('hall'),slot = session.get('slot'),room = session.get('room'),deco = session.get('deco'))

@app.route('/newsignup',methods = ['GET','POST'])
def new_donation():
    if request.method == 'POST':
        print("Inside donation post")
        e_mail = university_employee.query.all()
        print(e_mail)
        if e_mail:
            for x in e_mail:
                print("Inside for loop")
                if request.form['emailaddress'] not in x.email:
                    dom = request.form['date2']
                    print("dom = request.form['date2']")
                    if dom == '':
                        dom = None
                        print("No_date")
                    else:
                        dom = dom
                        print("date set")
                    print("donation is inside POST",request.form['firstname'],request.form['lastname'],request.form['address'],request.form['emailaddress'],request.form['phone'],request.form['date'],request.form['gender'],request.form['Gotra'],request.form['date2'],request.form['pwd2'])
                    obj = university_employee(fname = request.form['firstname'],
                                         lname = request.form['lastname'],
                                         address = request.form['address'],
                                         email = request.form['emailaddress'],
                                         mobile = request.form['phone'],
                                         dob = request.form['date'],
                                         gender = request.form['gender'],
                                         empid = request.form['empid'],
                                         department = request.form['department'],
                                         gotra = request.form['Gotra'],
                                         dom = dom,
                                         password = generate_password_hash(request.form['pwd2']))
                    db.session.add(obj)
                    db.session.commit()
                    return render_template('modes-of-donation.html',msg = "Signed up successfully please login!!!")
                else:
                    return render_template('new-signup.html',msg = "Already mail_id used please try again later!!")
        else:
            dom = request.form['date2']
            print("dom = request.form['date2']")
            if dom == '':
                dom = None
                print("No_date")
            else:
                dom = dom
                print("date set")
            obj = university_employee(fname = request.form['firstname'],
                                         lname = request.form['lastname'],
                                         address = request.form['address'],
                                         email = request.form['emailaddress'],
                                         mobile = request.form['phone'],
                                         dob = request.form['date'],
                                         gender = request.form['gender'],
                                         empid = request.form['empid'],
                                         department = request.form['department'],
                                         gotra = request.form['Gotra'],
                                         dom = dom,
                                         password = generate_password_hash(request.form['pwd2']))
            db.session.add(obj)
            db.session.commit()
            return render_template('modes-of-donation.html',msg = "Signed up successfully please login!!!")
    return render_template('new-signup.html')



    
@app.route('/signup',methods = ['GET','POST'])
def donation():
    if request.method == "POST":
        print("Inside donation post")
        e_mail = donationsignup.query.all()
        print(e_mail)
        if e_mail:
            for x in e_mail:
                print("Inside for loop")
                if request.form['emailaddress'] not in x.email:
                    dom = request.form['date2']
                    print("dom = request.form['date2']")
                    if dom == '':
                        dom = None
                        print("No_date")
                    else:
                        dom = dom
                        print("date set")
                    print("donation is inside POST",request.form['firstname'],request.form['lastname'],request.form['address'],request.form['emailaddress'],request.form['phone'],request.form['date'],request.form['gender'],request.form['Gotra'],request.form['date2'],request.form['pwd2'])
                    obj = donationsignup(fname = request.form['firstname'],
                                         lname = request.form['lastname'],
                                         address = request.form['address'],
                                         email = request.form['emailaddress'],
                                         mobile = request.form['phone'],
                                         dob = request.form['date'],
                                         gender = request.form['gender'],
                                         gotra = request.form['Gotra'],
                                         dom = dom,
                                         password = generate_password_hash(request.form['pwd2']))
                    db.session.add(obj)
                    db.session.commit()
                    return render_template('modes-of-donation.html',msg = "Signed up successfully please login!!!")
                else:
                    return render_template('Logsign.html',msg = "Already mail_id used please try again later!!")
        else:
            dom = request.form['date2']
            print("dom = request.form['date2']")
            if dom == '':
                dom = None
                print("No_date")
            else:
                dom = dom
                print("date set")
            obj = donationsignup(fname = request.form['firstname'],
                                         lname = request.form['lastname'],
                                         address = request.form['address'],
                                         email = request.form['emailaddress'],
                                         mobile = request.form['phone'],
                                         dob = request.form['date'],
                                         gender = request.form['gender'],
                                         gotra = request.form['Gotra'],
                                         dom = dom,
                                         password = request.form['pwd2'])
            db.session.add(obj)
            db.session.commit()
            return render_template('modes-of-donation.html',msg = "Signed up successfully please login!!!")
    return render_template('Logsign.html')


@app.route('/startlogin',methods = ['POST','GET'])
def home():
    if session.get('logged_in'):
        return render_template('amount-donation.html')
    elif session.get('logged_in')==False:
        return render_template('modes-of-donation.html')
    else:
        return  render_template('Logsign.html')
    
@app.route('/donation',methods = ['GET', 'POST'])
def mode():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['email'])
        POST_PASSWORD = str(request.form['password'])
        querys = donationsignup.query.filter_by(email = POST_USERNAME).all()
        for query in querys:
            if check_password_hash(query.password,POST_PASSWORD):
                session['logged_in'] = True
                session['email'] = query.email
                return render_template('amount-donation.html',login_session = session.get('logged_in'))
            else:
                return redirect('/startlogin')
    return render_template('modes-of-donation.html')


@app.route('/amtdonate',methods = ['GET'])
def amtdonate():
    return render_template('amount-donation.html',login_session = session.get('logged_in'))
    

@app.route('/logout',methods = ['POST','GET'])
def logout():
    session['logged_in'] = False
    return redirect('/startlogin')

@app.route('/funds',methods = ['GET', 'POST'])
def amount():
    if request.method == 'POST':
        obj = donatemoney(amtprice = request.form['amtprice'],
                          email = session.get('email'),
                          date_of_donation = datetime.datetime.now().date(),
                          time_of_donation = datetime.datetime.now().time())
        db.session.add(obj)
        db.session.commit()
        return render_template('funds_don.html',login_session = session.get('logged_in'))
    return render_template('funds_don.html',login_session = session.get('logged_in'))

@app.route('/kind',methods = ['GET','POST'])
def kind():
    if request.method == 'POST':
        return render_template('kindpage.html',login_session = session.get('logged_in'))
    return render_template('kindpage.html',login_session = session.get('logged_in'))


@app.route('/admin',methods = ['GET','POST'])
def admin_login():
    if request.method == 'POST':
        if request.form['admin_user'] == 'kiit@123' and request.form['admin_password'] == 'kiit':
            session['admin_login_in'] = True
            obj = foodprice.query.filter_by(id = 1).all()
            sp_obj = specialprasadmanager.query.all()
            return render_template('adminbhoga.html',obj = obj,sp_obj = sp_obj)
        else:
            return render_template('adminlogin.html')
    return render_template('adminlogin.html')


@app.route('/adminbhoga',methods = ['GET','POST'])
def admin_bhoga():
    obj = foodprice.query.filter_by(id = 1).all()
    show_obj = all_prasadam.query.all()
    sp_obj = specialprasadmanager.query.all()
    if request.method == 'POST':
        return render_template('adminbhoga.html',obj = obj,sp_obj = sp_obj,show_obj = show_obj)
    return render_template('adminbhoga.html',obj = obj,sp_obj = sp_obj,show_obj = show_obj)

@app.route('/admindaily',methods = ['GET','POST'])
def admin_daily():
    show_obj = all_prasadam.query.filter_by(date_of_order = datetime.datetime.now().date()).with_entities(all_prasadam.firstname,all_prasadam.lastname,all_prasadam.address,all_prasadam.email,all_prasadam.phone,all_prasadam.anna,all_prasadam.price,all_prasadam.type_of_order)
    count_obj = show_obj.count()
    print("show 1:",show_obj)
    if request.method == "POST":
        #show_obj = all_prasadam.query.filter_by(date_of_order = request.form['details'])
        show_obj = all_prasadam.query.filter_by(date_of_order = request.form['details']).with_entities(all_prasadam.firstname,all_prasadam.lastname,all_prasadam.address,all_prasadam.email,all_prasadam.phone,all_prasadam.anna,all_prasadam.price,all_prasadam.type_of_order)
        print("show 2:",show_obj)
        return render_template('admindaily.html',show_obj = show_obj)
    return render_template('admindaily.html',show_obj = show_obj,count_obj = count_obj)


@app.route('/admindailythali',methods = ['GET','POST'])
def admin_daily_thali():
    if request.method == 'POST':
        obj = dailyprasadmanager.query.filter_by(id = 30).all()
        #show_obj = all_prasadam.query.filter_by(date_of_order = request.form['details']).all()
        sp_obj = specialprasadmanager.query.all()
        print(obj)
        obj[0].anna = request.form['qty']
        obj[0].haradadali = request.form['qty']
        obj[0].beshar = request.form['qty']
        obj[0].ambularai = request.form['qty']
        obj[0].khiraa = request.form['qty']
        obj[0].dahibundi = request.form['qty']
        obj[0].price = request.form['price']
        db.session.commit()
        return render_template('admindaily.html')#,obj = obj,sp_obj = sp_obj,show_obj = show_obj)
    return render_template('admindaily.html')#,obj = obj,sp_obj = sp_obj,show_obj = show_obj)

@app.route('/adminspecial',methods = ['GET','POST'])
def admin_special():
    show_obj = all_prasadam.query.all()
    obj = foodprice.query.all()
    if request.method == "POST":
        return render_template('adminspecial.html',obj = obj,sp_obj = specialprasadmanager.query.all(),show_obj = show_obj)
    return render_template('adminspecial.html',obj = obj,sp_obj = specialprasadmanager.query.all(),show_obj = show_obj)

@app.route('/adminparty',methods = ['GET','POST'])
def admin_party():
    if request.method == "POST":
        return render_template('adminparty.html')
    return render_template('adminparty.html')


@app.route('/adminspecialthali',methods = ['GET','POST'])
def admin_special_thali():
    show_obj = all_prasadam.query.all()
    if request.method == 'POST':
        obj = foodprice.query.all()
        obj = vars(obj[0])
        print(obj)
        a = request.form.getlist('item')
        l = len(a)
        print(a)
        x = specialprasadmanager.query.get(1)
        if x and l >= 1:
            #db.session.delete(x)
            #b = specialprasadmanager(item = a[0],qty = request.form[a[0]],price = obj[a[0]])
            #db.session.add(b)
            x.item = a[0]
            x.qty = request.form[a[0]]
            x.price = float(obj[a[0]])
            print(obj[a[0]])
            db.session.commit()
        elif l >= 1:
            b = specialprasadmanager(item = a[0],qty = request.form[a[0]],price = float(obj[a[0]]))
            db.session.add(b)
        x = specialprasadmanager.query.get(2)
        if x and l >= 2:
            #db.session.delete(x)
            #b = specialprasadmanager(item = a[1],qty = request.form[a[1]],price = obj[a[1]])
            #db.session.add(b)
            x.item = a[1]
            x.qty = request.form[a[1]]
            x.price = float(obj[a[1]])
            print(obj[a[1]])
            db.session.commit()
        elif l >= 2:
            b = specialprasadmanager(item = a[1],qty = request.form[a[1]],price = float(obj[a[1]]))
            db.session.add(b)
        x = specialprasadmanager.query.get(3)
        if x and l >= 3:
            #db.session.delete(x)
            #b = specialprasadmanager(item = a[2],qty = request.form[a[2]],price = obj[a[2]])
            #db.session.add(b)
            x.item = a[2]
            x.qty = request.form[a[2]]
            x.price = float(obj[a[2]])
            print(obj[a[2]])
            db.session.commit()
        elif l >= 3:
            b = specialprasadmanager(item = a[2],qty = request.form[a[2]],price = float(obj[a[2]]))
            db.session.add(b)
        x = specialprasadmanager.query.get(4)
        if x and l >= 4:
            #db.session.delete(x)
            #b = specialprasadmanager(item = a[3],qty = request.form[a[3]],price = obj[a[3]])
            #db.session.add(b)
            x.item = a[3]
            x.qty = request.form[a[3]]
            x.price = float(obj[a[3]])
            print(obj[a[3]])
            db.session.commit()
        elif l >= 4:
            b = specialprasadmanager(item = a[3],qty = request.form[a[3]],price = float(obj[a[3]]))
            db.session.add(b)
        x = specialprasadmanager.query.get(5)
        if x and l >= 5:
            #db.session.delete(x)
            #b = specialprasadmanager(item = a[4],qty = request.form[a[4]],price = obj[a[4]])
            #db.session.add(b)
            x.item = a[4]
            x.qty = request.form[a[4]]
            x.price = float(obj[a[4]])
            print(obj[a[4]])
            db.session.commit()
        elif l >= 5:
            b = specialprasadmanager(item = a[4],qty = request.form[a[4]],price = float(obj[a[4]]))
            db.session.add(b)
        xt = x
        #for a in items_admin:
        #    b = specialprasadmanager(item = a,qty = request.form[a],price = obj[a])
        #    db.session.add(b)
        #    print(request.form[a])
        if request.form['price1'] or request.form['price2'] or request.form['price3'] or request.form['price4'] or request.form['price5'] or request.form['price6'] or request.form['price7'] or request.form['price8'] or request.form['price9'] or request.form['price10'] or request.form['price11'] or request.form['price12'] or request.form['price13'] or request.form['price14'] or request.form['price15'] or request.form['price16']or request.form['price17'] or request.form['price18'] or request.form['price19'] or request.form['price20'] or request.form['price21'] or request.form['price22'] or request.form['price23'] or request.form['price24'] or request.form['price25'] or request.form['price26'] or request.form['price27'] or request.form['price28'] or request.form['price29'] or request.form['price30'] or request.form['price31'] or request.form['price32'] or request.form['price33'] or request.form['price34'] or request.form['price35'] or request.form['price36'] or request.form['price37']:
            obj = foodprice.query.filter_by(id = 1).all()
            obj[0].anna = request.form['price1']
            obj[0].kanika = request.form['price2']
            obj[0].jerraanna = request.form['price3']
            obj[0].oriyaanna = request.form['price4']
            obj[0].kamalaanna = request.form['price5']
            obj[0].gheeanna = request.form['price6']
            obj[0].khichudi = request.form['price7']
            obj[0].haradadali = request.form['price8']
            obj[0].mugadali = request.form['price9']
            obj[0].haradadalma = request.form['price10']
            obj[0].mugadalma = request.form['price11']
            obj[0].puridalma = request.form['price12']
            obj[0].purimithadali = request.form['price13']
            obj[0].butadali = request.form['price14']
            obj[0].beshar = request.form['price15']
            obj[0].sagamuga = request.form['price16']
            obj[0].bhajachennatarkari = request.form['price17']
            obj[0].panneertarkari = request.form['price18']
            obj[0].pannerbuta = request.form['price19']
            obj[0].mahura = request.form['price20']
            obj[0].potalabesanatarkari = request.form['price21']
            obj[0].potalarasha = request.form['price22']
            obj[0].janhitarkari = request.form['price23']
            obj[0].butatarkari = request.form['price24']
            obj[0].chips = request.form['price25']
            obj[0].kadalibhaja = request.form['price26']
            obj[0].potalakurma = request.form['price27']
            obj[0].ambularai = request.form['price28']
            obj[0].khajurikhatta = request.form['price29']
            obj[0].dahibaigana = request.form['price30']
            obj[0].sapurikhatta = request.form['price31']
            obj[0].fruitsalad = request.form['price32']
            obj[0].ambakhatta = request.form['price33']
            obj[0].ouukhatta = request.form['price34']
            obj[0].dahibundi = request.form['price35']
            obj[0].khira = request.form['price36']
            obj[0].khiree = request.form['price37']
        db.session.commit()
        return render_template('adminbhoga.html',obj = obj,sp_obj = specialprasadmanager.query.all(),show_obj = show_obj)
    return render_template('adminbhoga.html',obj = obj,sp_obj = specialprasadmanager.query.all(),show_obj = show_obj)

@app.route('/showbhogadetails',methods = ['GET','POST'])
def admin_show_bhoga_details():
    obj = foodprice.query.filter_by(id = 1).all()
    show_obj = all_prasadam.query.all()
    sp_obj = specialprasadmanager.query.all()
    if request.method == 'POST':
        return render_template('adminbhoga.html',obj = obj,sp_obj = sp_obj,show_obj = show_obj)
    return render_template('adminbhoga.html',obj = obj,sp_obj = sp_obj,show_obj = show_obj)

@app.route('/admindonation',methods = ['GET','POST'])
def admin_donation_details():
    dono_obj = donationsignup.query.all()
    mon_obj = donatemoney.query.all()
    if request.method == 'POST':
        return render_template('admindonation.html',dono_obj = dono_obj,mon_obj = mon_obj)
    return render_template('admindonation.html',dono_obj = dono_obj,mon_obj = mon_obj)


@app.route('/adminhallbook',methods = ['GET','POST'])
def admin_hall_book():
    obj_hallbook = hallbook.query.all()
    obj_details_hall = hallbook_details.query.all()
    if request.method == 'POST':
        return render_template('adminhallbook.html',obj_hallbook = obj_hallbook,obj_details_hall = obj_details_hall)
    return render_template('adminhallbook.html',obj_hallbook = obj_hallbook,obj_details_hall = obj_details_hall)



@app.route('/adminlogout',methods = ['GET','POST'])
def admin_logout():
    session['admin_login_in'] = False
    return redirect('/admin')

if  __name__ == "__main__":
    db.create_all()
    app.run()




