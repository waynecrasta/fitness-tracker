from datetime import datetime, timedelta

from sqlalchemy import func, Date, cast

from app import db
from app.enums import ExerciseType, TimeFilterType
from app.models import Exercise, User


def get_quantity_by_type(
        exercise_type: ExerciseType,
        user: User,
        filter_type: TimeFilterType = TimeFilterType.DAILY
) -> int:
    query = db.session.query(func.sum(Exercise.quantity)).filter_by(
        user_id=user.id, type=exercise_type.value
    )
    if filter_type == TimeFilterType.WEEKLY:
        monday = datetime.now() - timedelta(days=datetime.now().weekday())
        return query.filter(
            cast(Exercise.time_created, Date) >= monday.date(),
            cast(Exercise.time_created, Date) <= datetime.today().date(),
        ).scalar()
    elif filter_type == TimeFilterType.DAILY:
        return query.filter(
            cast(Exercise.time_created, Date) == datetime.today().date()
        ).scalar()
    else:
        return query.scalar()


def get_exercises_by_user(user: User):
    return db.session.query(Exercise).filter_by(user_id=user.id).order_by(Exercise.time_created.desc()).all()


def insert_exercise(exercise_type: ExerciseType, quantity: int, user: User) -> None:
    exercise = Exercise(type=exercise_type.value, quantity=quantity, user_id=user.id)
    db.session.add(exercise)
    db.session.commit()
    return


def insert_user(user: User):
    db.session.add(user)
    db.session.commit()
    return
