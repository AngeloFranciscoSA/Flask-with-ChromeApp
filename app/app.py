#import Flask and all things we'll use here
from flask import Flask, session
from flask import render_template, request, redirect, url_for, jsonify, send_from_directory

#reg - Catch Chrome path in windows
import reg
#storage - CRUD
import storage
#hashlib - cryptography for password
import hashlib
#open Chrome process
import subprocess
#os and sys - open OS paths
import os, sys

#catch the Chrome path
chrome = reg.get_chrome_path()

#open chrome in AppMode! - Comment this line for test.
subprocess.Popen([chrome,"-app=http://localhost:5000?"])

#Declare folders!
base_dir = '.'
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

#main process for FLASK, all project in FLASK NEED THIS!!!
app = Flask(__name__,
        static_folder=os.path.join(base_dir, 'static'),
        template_folder=os.path.join(base_dir, 'templates'))

#This is REQUIRED FOR LOGIN SYSTEM!
app.secret_key = os.urandom(24)

#Declare CRUD 
db = storage.carDB()

"""
    Firts part!

        Here we have the @app.route('/'), means, the route in URL will follow! The basic the INDEX here!
        I recommended you search URL paths in HTML to understand better.
"""
@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title= 'Login')
    """
        Will return something! In this case, will render the index page!
        - title = 'login', what this ??
            - This is parament you can pass, and catch on HTML, opening the index.html you will see how to used.
            - Not so much used in this project it.
    """

"""
 LOGIN VERIFICATION !!!

    With this @app.route, you see I pass methods, but what is?
        This methods paramenter, is the methods the page can use, by default used just URL with you not declare nothing!
            - Is good declare this three methods!
                Simple explication!
                    - URL, read the standard HTML
                    - GET, will get the paraments in URL
                    - POST, will get the paraments on body page!

                    (recommeded you read more about that, it's most important thing in this project)
"""
@app.route('/login', methods=['POST','URL','GET'])
def login():
    
    #will see if have some POST call!
    if request.method == 'POST':

        #catch the paraments
        username = request.form['username']
        password = request.form['password']

        #see if the username is not empty!
        if username:
            #see if the password is not empty!
            if password:

                #here we encrypt the password to MD5
                h = hashlib.md5(password.encode())
                pws = h.hexdigest()
                #pass the username and password to check and return the a answer if this user exist or not!
                check = db.check_login(username,pws)

                #check if not empty!
                if check:
                    #if not, creat a session and redirect to the URL home!
                    session['user'] = username 
                    return redirect(url_for('home'))

                #all this else, is empty or something is wrong on if. Will redirect to index to login again!
                else:
                    return redirect(url_for('index'))

            else:
                return redirect(url_for('index'))

        else: 
            return redirect(url_for('index'))

    else: 
        return redirect(url_for('index'))


#HOME!!!
    """
        This is a simple part after pass in Login system!
    """
@app.route('/home', methods=['POST','URL','GET'])
def home():
    
    #see in the session "user" exist, if not you can't access this page!
    if 'user' in session:

        if request.method == "POST":
            car = request.form['car']
            consult = db.consult(car)

            if consult:
                return render_template('car.html', data = consult)

        #If our SESSION exist, we'll render the PAGE
        return render_template('car.html', data = "")

    #NOT EXIST "user" IN SESSION - YOU SHALL NOT PASS!!!
    else:
        #redirect, will send to route /index
        return redirect(url_for('index'))

#Pass our data to edit fields!
@app.route('/consult_edit', methods=['POST'])
def consult_edit():

    if 'user' in session:
        if request.method == "POST":
            id_car = request.form['id']

            consult = db.consult_edit(id_car)

            if consult:
                #jsonify, transform our data in a simple JSON to catch in JQuery
                return jsonify(consult)
    
    else:
        return redirect(url_for('index'))

#Edit route!
@app.route('/edit', methods=['POST'])
def edit():

    if 'user' in session:
        if request.method == "POST":
            id_car      = request.form['id']
            name_car    = request.form['name_car']
            model       = request.form['model']
            year        = request.form['year']
            price       = request.form['price']

            db.update(id_car,name_car,model,year,price)
    
    else:
        return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():

    if 'user' in session:
        if request.method == "POST":
            id_car = request.form['id']

            db.delete(id_car)
    else:
        return redirect(url_for('index'))

#The route to register!
@app.route('/register', methods=['POST','GET','URl'])
def register():

    if 'user' in session:
        if request.method == "POST":
            name_car = request.form['name_car']
            model    = request.form['model']
            year     = request.form['year']
            price    = request.form['price']

            db.create(name_car,model,year,price)

            return render_template('new_car.html')

        return render_template('new_car.html')

    else:
        return redirect(url_for('index'))

#Logout route!
@app.route('/logout')
def logout():
   # remove session!
   session.pop('user', None)
   # finish all process to chrome and our app
   os.system("taskkill /im chrome.exe /f")
   os.system("taskkill /im app.exe /f")
   sys.exit()

#Main process in flask to run in .exe
app.run()