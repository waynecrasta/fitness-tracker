from datetime import datetime, timedelta

from sqlalchemy import func, Date, cast

from app import db
from app.enums import ExerciseType, TimeFilterType
from app.models import Exercise


def get_quantity_by_type(exercise_type: ExerciseType, filter_type: TimeFilterType = TimeFilterType.DAILY) -> int:
    query = db.session.query(func.sum(Exercise.quantity)).filter_by(
        user_id=1, type=exercise_type.value
    )
    if filter_type == TimeFilterType.WEEKLY:
        monday = datetime.now() - timedelta(days=datetime.now().weekday())
        return query.filter(
            cast(Exercise.time_created, Date) >= monday.date(),
            cast(Exercise.time_created, Date) <= datetime.today().date(),
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
