from flask import Blueprint, render_template
from flask_login import current_user, login_required


home = Blueprint("home", __name__, template_folder="templates")


@home.route("/")
def index():
    return render_template("index.html")


@home.route("/profile")
@login_required
def profile():
    ideal_weight = current_user.get_weight_score()
    return render_template(
        "profile.html",
        name=current_user.username,
        ideal_weight=ideal_weight['message'],
        height=current_user.height,
        weight=f'{current_user.weight} kgs',
        age=current_user.age,
    )
