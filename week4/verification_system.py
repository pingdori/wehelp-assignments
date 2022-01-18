from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="123456"

@app.route("/")
def index():
    return render_template("sign_in_index.html")


@app.route("/signin",methods=["POST"])
def success():
    account_content = request.form["account_content"]
    password_content = request.form["password_content"]
    session["account"]=account_content
    session["password"]=password_content
    if account_content == "test" and password_content == "test":
        return redirect("/member/")
    else:
        return redirect("/error")
        
@app.route("/member/")
def member_index():
    
    if session["password"] != None:
        return render_template("member.html")
    elif session["password"] == None:
        return render_template("sign_in_index.html")
@app.route("/error/")
def error_index():
    account_content=session["account"]
    password_content=session["password"]
    account_content=len(account_content)
    password_content=len(password_content)
    if account_content == 0 or password_content == 0:
        message=request.args.get("message","請輸入帳號、密碼")
        return render_template("error.html",data=message)
    else:
        message=request.args.get("message","帳號、或密碼輸入錯誤")
        return render_template("error.html",data=message)
@app.route("/signout",methods=["GET"])
def signout():
    session["account"] = None
    session["password"] = None
    return redirect("/")

app.run(port=3000)