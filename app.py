from flask import url_for, session, Flask, render_template, request, redirect


application = Flask(__name__, template_folder="templates")
application.secret_key = "mingyu"

ID = "mingyu"
PW = "0000"

@application.route("/")
def home():
    if "userID" in session:
        return render_template("home폴더/home.html", username=session.get("userID"), login=True)
    else:
        return render_template("home폴더/home.html", login=False)

@application.route("/login", methods=["get"])
def login():
    _id_ = request.args.get("loginID")
    _password_ = request.args.get("loginPW")

    if ID == _id_ and _password_ == PW:
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@application.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))

# 급식 페이지                                                                                                                                     
@application.route("/templates/급식/page1.html")
def lunch():
    return (f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/급식.css">
    <title>GB.급식</title>
</head>
<body>
    <header>
        <h1><a href="/templates/home폴더/home.html">GB.CARE</a></h1>
        <h2>경주정보고 프로젝트</h2>
        <h3>급식 순서</h3>
    </header>

    <main>
        <div id="mealOrder" class="mealorder"></div>
        <script  src="/static/js폴더/page_01_script.js"></script> <!-- 'js' 폴더에 있는 script.js 파일을 불러옴 -->
    </main>
</body>
</html>''')


# 점수 페이지
@application.route("/templates/상벌점/page2.html")
def count():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/static/css/점수.css">
</head>
<body>
    <h1> 여기는 page2입니다.</h1>
</body>
</html>'''

# 소식 페이지
@application.route("/templates/소식/page3.html")
def new():
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/static/css/소식.css">
</head>
<body>
    <h1> 여기는 page3입니다. </h1>
</body>
</html>'''

# 질문 페이지
@application.route("/templates/소식/page4.html")
def ques():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/static/css/질문.css">
</head>
<body>
    <h1> 여기는 page4입니다. </h1>
</body>
</html>'''






application.run(debug=True)
# application.run(host="0.0.0.0")
