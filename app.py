from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="university",
    database="testing"
)
mycursor = mydb.cursor()
app = Flask(__name__,
            static_url_path='',
            static_folder='static')

@app.route("/welcome")
def welcome():
    if "userName" in session:
        return render_template("welcome.html")
    else:
        return ("You have to Log in First")


@app.route("/")
def first():
    return render_template("first.html")
    # return ("Welcome to page


app.secret_key = "hello"


@app.route("/test", methods=["POST", "GET"])
def login():
    if "userName" in session:
        session.pop("userName")
    
    if request.method == "POST":
        user = request.form.get('name')
        sql = "SELECT lastName FROM customer WHERE lastName = '" + user + "'"
        print(sql)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  
        my=len(myresult) 
        print(my) 
        if my > 0  :
            session["userName"] = user
            #return redirect(url_for("user"))
            return {"status": 200}
        else: 
            return ("You have no acccount ")

    return render_template("/test.html")
    
@app.route("/log", methods=['POST', 'GET'])
def log():
    NName = request.form.get("userName")
    sql = "SELECT * FROM customer WHERE lastName = '" + NName + "'"
    # print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # print(myresult)
    
    return "Welcome to "+ NName


@app.route("/user", methods=["POST", "GET"])
def user():
    if "userName" in session:
        user = session["userName"]
        return render_template("/welcome.html",name=user)
        # return f"<h1>You are logged in , Mr{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout",methods=["POST", "GET"])
def logout():
    # user = session["userName"]
    
    if request.method == "GET":
        session.pop("userName", None)
        return redirect(url_for("login"))
    else:
        return render_template("logout.html",name="user")


@app.route("/date")
def date():
    return "The current date is " + str(datetime.now())


counter = 0


@app.route("/count")
def count():
    global counter
    counter += 1
    return "this page was served "+str(counter)+" times"


@app.route("/add_card")
def add_card():
    return render_template("add_card.html")


@app.route("/showData")
def showData():
    Name = request.form.get("name")
    age = request.form.get("age")
    return render_template("showData.html", name=mycursor.execute("SELECT * FROM customer"), myresult=mycursor.fetchall())


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    Name = request.form.get("name")
    age = request.form.get("age")
    # return render_template("showData.html")
    mycursor = mydb.cursor()
    sql = "INSERT INTO customer (lastName) VALUES (%s)"
    val = [Name]
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return "Name: {} and Age: {} !!!".format(Name, age)


@app.route("/delete", methods=['GET'])
def delete():
    id = request.args.get("id")
    sql = "DELETE FROM customer WHERE id = '" + id + "'"
    mycursor.execute(sql)
    mydb.commit()
    return redirect('/showData')


@app.route("/update", methods=['GET', 'POST'])
def update():
    id = request.args.get("id")
    if request.method == 'POST':
        name = request.form.get("lastName")
        sql = "update customer set lastName = '" + name + "' where id = '" + id + "'"
        mycursor.execute(sql)
        mydb.commit()
        return redirect('/showData')

    sql = "select * from customer where id = '" + id + "'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    return render_template("update.html", id=result[0], name=result[1])


@app.route("/signup")
def signup():
    return render_template("/signup.html")


@app.route("/sign", methods=['GET', 'POST'])
def sign():
    Name = request.form.get("name")
    # return render_template("showData.html")
    mycursor = mydb.cursor()
    sql = "INSERT INTO customer (lastName) VALUES (%s)"
    val = [Name]
    mycursor.execute(sql, val)
    mydb.commit()
    # print(mycursor.rowcount, "record inserted.")
    return "You have finally Signed Up MR {} !!!".format(Name)
