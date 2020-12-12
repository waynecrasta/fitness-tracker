from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, PasswordField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import InputRequired, EqualTo


class ExerciseInputForm(FlaskForm):
    name = SelectField("Exercise Name", choices=["Pushups", "Pullups"])
    quantity = IntegerField("How Many?", validators=[InputRequired()], render_kw={"placeholder": "Quantity"})
    submit = SubmitField("Add")


class SignupForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')],
                             render_kw={"placeholder": "Password"})
    confirm = PasswordField('Confirm your Password', validators=[InputRequired()],
                            render_kw={"placeholder": "Confirm your password"})
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             validators=[InputRequired(), ],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")
