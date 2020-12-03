from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.fields.html5 import IntegerField


class ExerciseInputForm(FlaskForm):
    name = SelectField("Exercise Name", choices=["Pushups", "Pullups"])
    quantity = IntegerField("How Many?", render_kw={"placeholder": "Quantity"})
    submit = SubmitField('+')
