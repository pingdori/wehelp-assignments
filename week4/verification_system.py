from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="erythrocytosis"

@app.route("/")
def index():
    return render_template("sign_in_index.html")

@app.route("/signin", methods = ["POST"])
def verification():
    account_content = request.form["account_content"]
    password_content = request.form["password_content"]
    # account_len=len(account_content)
    # password_len=len(password_content)
    if account_content == "test" and password_content == "test":
        session["account"] = account_content
        session["password"] = password_content
        return redirect("/member/")
    elif account_content == "" or password_content == "":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/member/")
def member_index():
    if session["password"] != None:
        return render_template("member.html")
    elif session["password"] == None:
        return render_template("sign_in_index.html")

@app.route("/error/")
def error_index():
    # if session["password"] != None:
    #     return render_template("member.html")
    message=request.args.get("message","")
    return render_template("error.html",data = message)

@app.route("/signout",methods = ["GET"])
def signout():
    session["account"] = None
    session["password"] = None
    return redirect("/")

app.run(port=3000)