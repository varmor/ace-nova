from copyreg import pickle
from flask import Blueprint, render_template, request, flash, url_for


views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def index():
    return render_template("home.html")

@views.route("/signup", methods = ["POST", "GET"])
def signup():
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