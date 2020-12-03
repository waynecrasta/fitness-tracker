from flask import redirect, render_template
from app.forms import ExerciseInputForm
from sqlalchemy import func, cast, Date
import enum
from app.db import db
from app.models import Exercise
from app import app
from datetime import datetime, timedelta


class ExerciseType(enum.Enum):
    Pushups = 1
    Pullups = 2


class TimeFilterType(enum.Enum):
    DAILY = 1
    WEEKLY = 2


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ExerciseInputForm()
    if form.validate_on_submit():
        exercise_type = ExerciseType[form.name.data]
        insert_exercise(exercise_type, form.quantity.data)
        return redirect('/')

    return render_template("index.html", form=form)


@app.route('/statistics')
def statistics():
    return render_template(
        "statistics.html",
        num_pushups_today=get_quantity_by_type(ExerciseType.Pushups),
        num_pullups_today=get_quantity_by_type(ExerciseType.Pullups),
        num_pushups_this_week=get_quantity_by_type(ExerciseType.Pushups, filter_type=TimeFilterType.WEEKLY),
        num_pullups_this_week = get_quantity_by_type(ExerciseType.Pullups, filter_type=TimeFilterType.WEEKLY)
    )


def get_quantity_by_type(exercise_type: ExerciseType, filter_type: TimeFilterType = TimeFilterType.DAILY) -> int:
    query = db.session.query(func.sum(Exercise.quantity)).filter_by(
        user_id=1,
        type=exercise_type.value
    )
    if filter_type == TimeFilterType.WEEKLY:
        monday = datetime.now() - timedelta(days=datetime.now().weekday())
        return query.filter(
            cast(Exercise.time_created, Date) >= monday.date(),
            cast(Exercise.time_created, Date) <= datetime.today().date()
        ).scalar()
    else:
        return query.filter(
            cast(Exercise.time_created, Date) == datetime.today().date()
        ).scalar()


def insert_exercise(exercise_type: ExerciseType, quantity: int) -> None:
    exercise = Exercise(type=exercise_type.value, quantity=quantity)
    db.session.add(exercise)
    db.session.commit()
    return
