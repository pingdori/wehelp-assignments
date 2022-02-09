from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from dotenv import load_dotenv
import mysql.connector
import os
import setting 
load_dotenv()
app=Flask(__name__,static_folder="public",static_url_path="/")
MYSQL_HOST=os.getenv("mysql_host")
MYSQL_PORT=os.getenv("mysql_port")
MYSQL_USER=os.getenv("mysql_user")
MYSQL_PASSWORD=os.getenv("mysql_password")
SECRET_KEY=os.getenv("secret_key")
app.secret_key = SECRET_KEY

@app.route("/")
def index():
    return render_template("sign_in_index.html")

@app.route("/signin", methods = ["POST"])
def verification():
    connection = mysql.connector.connect(host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USER,password=MYSQL_PASSWORD)
    cursor = connection.cursor()
    sql_select = "SELECT * FROM `member` WHERE`username`='"+request.form['account_content']+"' and `password`='"+request.form['password_content']+"'"
    cursor.execute("USE `webside`")
    cursor.execute(sql_select)
    results = cursor.fetchall()
    password_content = request.form["password_content"]
    account_content = request.form["account_content"]
    if len(results) == 1:
        name="SELECT `name` FROM `member` WHERE `username` = '"+request.form['account_content']+"' and `password`='"+request.form['password_content']+"'"
        cursor.execute(name)
        results=cursor.fetchall()
        for i in results:
            name=i[0]
        session["name"]=name
        session["password"]=password_content
        connection.close()
        return  redirect("/member")
    elif account_content == "" or password_content == "":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")
@app.route("/signup" , methods = ["POST"])
def signup():
    connection = mysql.connector.connect(host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USER,password=MYSQL_PASSWORD)
    cursor = connection.cursor()
    sql_insert="INSERT INTO `member`(`name`,`username`,`password`) VALUES ('"+request.form['name_signup']+"','"+request.form['account_signup']+"','"+request.form['password_signup']+"')"
    sql_select="SELECT * FROM `member` WHERE`name`='"+request.form['name_signup']+"' and `username`='"+request.form['account_signup']+"' and `password`='"+request.form['password_signup']+"'"
    cursor.execute("USE `webside`")
    cursor.execute(sql_select)
    results=cursor.fetchall()
    if len(results)!=0:
        connection.close()
        return redirect("/error/?message=帳號已被註冊")
    else:
        cursor.execute(sql_insert)
        connection.commit()
        connection.close()
        return redirect ("/")

@app.route("/member/")
def member_index():
    
    if session["password"] != None:
        return render_template("member.html",username = session["name"])
    elif session["password"] == None:
        return render_template("sign_in_index.html")

@app.route("/error/")
def error_index():
    message=request.args.get("message","")
    return render_template("error.html",data = message)

@app.route("/signout",methods = ["GET"])
def signout():
    session["account"] = None
    session["password"] = None
    return redirect("/")

app.run(port=3000)