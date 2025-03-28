from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
