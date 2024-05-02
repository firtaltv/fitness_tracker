from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from models.models import Activity
from datetime import datetime
from app import db

activity = Blueprint("activity", __name__, template_folder="templates", url_prefix="/activity")


@activity.route("/list")
@login_required
def activity_list():
    _current_user_id = current_user.id
    activities = Activity.get_all(_current_user_id)
    return render_template(
        "activity_history.html", activities=activities
    )


@activity.route("/add")
@login_required
def activity_get():
    return render_template("activity_create.html")


@activity.route("/add", methods=["POST"])
@login_required
def activity_post():
    data = request.form.to_dict()
    data["user_id"] = current_user.id
    # print(data)
    calories = Activity.count_calories(data['type'], float(data['activity_time']))
    new_activity = Activity(
        type=data['type'],
        calories=calories,
        activity_time=data['activity_time'],
        datetime=datetime.utcnow(),
        user_id=current_user.id
    )
    db.session.add(new_activity)
    db.session.commit()
    return redirect(url_for("activity.activity_list"))


@activity.route("/history")
@login_required
def history():
    ideal_weight = current_user.get_weight_score()
    return render_template(
        "profile.html",
        name=current_user.username,
        ideal_weight=ideal_weight['message'],
        height=current_user.height,
        weight=f'{current_user.weight} kgs',
        age=current_user.age,
    )
