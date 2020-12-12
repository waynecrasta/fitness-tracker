from flask import redirect, render_template, Blueprint, flash, url_for
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.enums import ExerciseType, TimeFilterType
from app.forms import ExerciseInputForm, SignupForm, LoginForm
from app.models import User
from app.repository import get_quantity_by_type, insert_exercise, insert_user

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/", methods=["GET", "POST"])
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("main.login"))

    form = ExerciseInputForm()
    if form.validate_on_submit():
        exercise_type = ExerciseType[form.name.data]
        insert_exercise(exercise_type, form.quantity.data)
        flash("Exercise added!")
        return redirect(url_for("main.statistics"))

    return render_template("index.html", form=form)


@main.route("/statistics")
def statistics():
    return render_template(
        "statistics.html",
        num_pushups_today=get_quantity_by_type(ExerciseType.Pushups) or 0,
        num_pullups_today=get_quantity_by_type(ExerciseType.Pullups) or 0,
        num_pushups_this_week=get_quantity_by_type(ExerciseType.Pushups, filter_type=TimeFilterType.WEEKLY) or 0,
        num_pullups_this_week=get_quantity_by_type(ExerciseType.Pullups, filter_type=TimeFilterType.WEEKLY) or 0,
    )


@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=password)
        insert_user(user)
        flash("Sign up successful! Welcome")
        return redirect(url_for("main.home"))

    return render_template(
        "signup.html",
        form=form
    )


@main.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Successful")
            return redirect(url_for("main.home"))
        else:
            flash("Login Failed")
            return redirect(url_for("main.login"))

    return render_template("login.html", form=form)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))
