# 載入Flask
from flask import Flask
from flask import request
from flask import render_template,redirect
from flask import session
# 建立 Application 物件，設定靜態檔案的處理
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"   
    )
app.secret_key="any string but secret" # 設定 Session 的密鑰

# 使用 GET 方法，處理路徑 / 的對應函式
@app.route("/", methods=["GET"]) #/代表網站首頁
def index(): #用來回應網站首頁連線的函式
    return render_template("index.html") #回傳網站首頁的內容

# 使用 POST 方法處理路徑 /signin 的對應函式
@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    if (username==password=="test"):
        session["username"]=username #session
        return redirect("/member")
    elif (username=="" or password=="" or username==password==""):
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

# 使用 GET 方法處理路徑 /signout 的對應函式
@app.route("/signout")
def signout():
    return redirect("/")

# 處理路徑 /member 的對應函式
@app.route("/member")
def member():
    return render_template("member.html")

# 處理路徑 /error 的對應函式
@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("membernull.html", message=message)

# 使用 GET 方法，處理路徑 /calculate 的對應函式
@app.route("/calculate")
def calculate():
    maxNumber=request.args.get["max"]
    maxNumber=int(maxNumber)
    # 1+2+...+max
    result=0
    for n in range(1,maxNumber+1):
        result+=n
    return render_template("calculate.html", data=result)

# 啟動網站伺服器在 Port 3000
app.run(port=3000)