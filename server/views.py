from copyreg import pickle
from flask import Blueprint, render_template, request, flash

views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def index():
    return render_template("base.html")

@views.route("/", methods = ["POST", "GET"])
def about():
    return render_template("base.html")

@views.route("/", methods = ["POST", "GET"])
def appointment():
    return render_template("base.html")

@views.route("/", methods = ["POST", "GET"])
def admin():
    return render_template("base.html")