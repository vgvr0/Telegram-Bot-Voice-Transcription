from flask import Flask, render_template, redirect, session, request

from db.db import Users
from bot.send_news_letter import send_news
from config import secret, LOGIN, PASSWORD
from utils.passToHash import ExaminationHash

from bot.send_message_to_user import send_message_to_user



app = Flask(__name__)
app.secret_key = secret



@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if ExaminationHash(request.form["password"], PASSWORD) and ExaminationHash(request.form["login"], LOGIN):
            session["ok"] = True
            return redirect("/home")
        return render_template("login.html")

    return render_template("login.html")


@app.route("/home")
def secret():
    if not session.get("ok"):
        return redirect("/")

    db = Users()
    user = db.get_users()
    return render_template("index.html", users=user)


@app.route("/newsletter", methods=["GET", "POST"])
def newsletter():
    if not session.get("ok"):
        return redirect("/")

    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            return render_template("newsletter.html")

        db = Users()
        users_id = db.get_all_users_id()
        send_news(users_id, text)

        return redirect("/newsletter")

    return render_template("newsletter.html")



@app.route("/change_status/<int:user_id>")
def change_status(user_id):
    if not session.get("ok"):
        return redirect("/")


    db = Users()
    db.change_status_user(user_id)

    return redirect("/home")



@app.route("/send_message/<int:user_id>", methods=["GET", "POST"])
def send_message(user_id):
    if not session.get("ok"):
        return redirect("/")



    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            return render_template("send_message.html")



        send_message_to_user(user_id, text)

        return redirect(f"/send_message/{user_id}")



    return render_template("send_message.html")




@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)