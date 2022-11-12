# 載入Flask
from flask import Flask,json
from flask import request
from flask import render_template,redirect
from flask import session
import mysql.connector
from flask import jsonify
# 建立 Application 物件，設定靜態檔案的處理
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"   
    )
app.secret_key="any string but secret" # 設定 Session 的密鑰

# 建立 MySQL 連線
memberdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="website",
    charset="utf-8"
)
cursor = memberdb.cursor()

# 查詢會員資料
@app.route("/api/member", methods=["GET"])
def member_search():
    username=request.args.get("username","")
    sql = ("SELECT id,name,username FROM member WHERE username = %s")
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    if result :
        return jsonify({ "data":{
                "id":result[0],
                "name":result[1],
                "username":result[2]
                }})
    else:
        return jsonify({"data":None})

# 更新會員資料
@app.route("/api/member", methods=["PATCH"])
def member_update():
    member = session.get("username")
    if member:
        newname = request.get_json()
        username = session["username"]
        sql = ("UPDATE member SET name = %s WHERE username = %s")
        cursor.execute(sql, (newname['name'], username,))
        check_username = cursor.fetchone()
        memberdb.commit()
        return {"ok": "true"}
    else:
        return {"error": "true"}

# 主頁 (使用 GET 方法，處理路徑 / 的對應函式)
@app.route("/", methods=["GET"]) #/代表網站首頁
def index(): #用來回應網站首頁連線的函式
    return render_template("index.html") #回傳網站首頁的內容

# 註冊頁 (使用 POST 方法處理路徑 /signup 的對應函式)
@app.route("/signup", methods=["POST"])
def signup():
    user=request.form["user"]
    username=request.form["username"]
    password=request.form["password"]
    sql = ("SELECT username FROM member WHERE username = %s")
    cursor.execute(sql, (username,))
    check_username = cursor.fetchone()
    if check_username :
        return redirect("/error?message=帳號已經被註冊")
    else:
        sql_insert = "INSERT INTO member(name,username,password)VALUES (%s, %s, %s)"
        val = (user, username, password)
        cursor.execute(sql_insert, val)
        memberdb.commit()
        return redirect("/")

# 登入 (使用 POST 方法處理路徑 /signin 的對應函式)
@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    sql = ("SELECT username,password FROM member WHERE username = %s and password = %s")
    cursor.execute(sql, (username,password,))
    check_username = cursor.fetchone()
    if check_username :
        session["username"]=username #session
        sql = ("SELECT name FROM member WHERE username = %s and password = %s")
        cursor.execute(sql, (username,password,))
        member_name = cursor.fetchone()
        session["name"]= member_name[0]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

# 登出 (使用 GET 方法處理路徑 /signout 的對應函式)
@app.route("/signout")
def signout():
    session["username"] = False
    return redirect("/")

# 登入成功 (處理路徑 /member 的對應函式)
@app.route("/member")
def member():
    member = session.get("username")
    name = session.get("name")
    if not member:
        return redirect("/")
    return render_template("member.html",user_name=name)
        

# 登入失敗 (處理路徑 /error 的對應函式)
@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("failure.html", message=message)

# 啟動網站伺服器在 Port 3000
app.run(port=3000)
