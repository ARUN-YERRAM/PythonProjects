from flask import Blueprint,render_template,request,jsonify,redirect,url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("home page",name="True", age=21)

@views.route("/about/<username>")
def profile(username):
    return render_template("profile.html")

@views.route("/json")
def get_json():
    return jsonify({'name':'arun','coolness':10})

@views.route("/data") 
def search():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")

def go_to_home():
    return redirect(url_for("views.get_json"))
