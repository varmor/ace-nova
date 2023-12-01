from copyreg import pickle
from flask import Blueprint, render_template, request, flash, url_for, request
# from server import db

views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def index():
    return render_template("home.html")

@views.route("/signup", methods = ["POST", "GET"])
def signup():
    if request.method == "POST":
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        department = request.form['department']
        year = request.form['year']
        phone_no = request.form['phone-no']
        preference_1 = request.form['preference1']
        preference_2 = request.form['preference2']
        preference_3 = request.form['preference3']
        # db.ace_members.insert_one({
        #     "first_name": first_name,
        #     "last_name": last_name,
        #     "email": email,
        #     "department": department,
        #     "year": year,
        #     "phone_no": phone_no,
        #     "preference_1": preference_1,
        #     "preference_2": preference_2,
        #     "preference_3": preference_3,
        # })
    print("Get request")
    return render_template("signup.html")

@views.route("/tgc", methods = ["POST", "GET"])
def tgc():
    return render_template("tgc.html")

@views.route("/contributors", methods = ["POST", "GET"])
def contributors():
    return render_template("contributors.html")

@views.route("/community", methods = ["POST", "GET"])
def community():
    return render_template("community.html")