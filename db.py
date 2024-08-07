import pymysql as ps
from flask import url_for, session, Flask, render_template, request, redirect

app = Flask(__name__)

db= ps.connect(host='localhost', user='root', password='1234', charset='utf8')
cursor  = db.cursor(ps.cursors.DictCursor)

cursor.execute('USE school_db;')
cursor.execute('SELECT * FROM member ;')

value = cursor.fetchall()
cursor.execute('SELECT * FROM member ;')


print(value[0]['member_id'],value[0]['member_pw'])

@app.route('/')
def home():
    return render_template('index.html')
ID= 'mingyu'
PW= '1234'

@app.route('/gbcare-login.netlify.app/')
def home():
    if "userID" in session:
        return render_template("index.html", username = session.get("userID"), login = True)
    else:
        return render_template("index.html", login = False)
    

@app.route("/login", methods= ["get"])
def login():
    _id_ = request.args.get("loginID")
    _password_ = request.args.get("loginPW")

    if value[0]['member_id'] == _id_ and _password_ == value[0]['member_pw']:
        session["userID"] =_id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))


app.run(host ="0.0.0.0")




db.commit()
db.close()






