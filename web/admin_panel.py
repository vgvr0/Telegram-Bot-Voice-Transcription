from flask import Flask, render_template, redirect, session, request
from pip._internal.utils import retry

from db.db import Users


from config import secret, LOGIN, PASSWORD


from utils.passToHash import toHash, ExaminationHash

app = Flask(__name__)



app.secret_key = secret



@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if ExaminationHash(request.form["password"], PASSWORD) and ExaminationHash(request.form['login'], LOGIN):
            session["ok"] = True
            return redirect("/home")


        return render_template('login.html')

    return render_template('login.html')




@app.route("/home")
def secret():
    if not session.get("ok"):
        return redirect("/")


    db = Users()
    user = db.get_users()

    return render_template('index.html', users=user)



@app.route("/newsletter", methods=["GET", "POST"])
def newsletter():
    if request.method == "POST":
        text = request.form.get("text")
        print("рассылка! народ!", text)
        # тут дальше: БД, отправка, логика
        return redirect("newsletter")

    return render_template("newsletter.html")




@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)