from flask import Blueprint,render_template,request,jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("home page",name="True", age=21)

@views.route("/about/<username>")
def about_page(username):
    return render_template("about page",name=username)

@views.route("/json")
def get_json():
    return jsonify({'name':'arun','coolness':10})

