from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db

from models.models import User
from validators.validators import *


user = Blueprint("user", __name__, template_folder="templates", url_prefix="/user")


# update a user
@user.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            error = user_validator(data)
            if error:
                flash(error)
                return redirect(url_for("user.get_user"))
            user.username = data['username']
            user.height = data['height']
            user.weight = data['weight']
            user.age = data['age']
            db.session.commit()
            return render_template("profile.html", user=user.json())
        return render_template("404.html")
    except e:
        return render_template("500.html")
