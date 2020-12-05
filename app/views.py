from flask import redirect, render_template, Blueprint

from app.enums import ExerciseType, TimeFilterType
from app.forms import ExerciseInputForm
from app.repository import get_quantity_by_type, insert_exercise

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/", methods=["GET", "POST"])
def home():
    form = ExerciseInputForm()
    if form.validate_on_submit():
        exercise_type = ExerciseType[form.name.data]
        insert_exercise(exercise_type, form.quantity.data)
        return redirect("/")

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
