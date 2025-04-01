from flask import Blueprint, render_template

api_bp = Blueprint('api', __name__)

@api_bp.route("/api")
def api():
    return render_template("api.html")
