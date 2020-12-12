from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, PasswordField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import InputRequired


class ExerciseInputForm(FlaskForm):
    name = SelectField("Exercise Name", choices=["Pushups", "Pullups"])
    quantity = IntegerField("How Many?", validators=[InputRequired()], render_kw={"placeholder": "Quantity"})
    submit = SubmitField("Add")


class SignupForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             validators=[InputRequired(), ],
                             render_kw={"placeholder": "Password"})
    # confirm = PasswordField('Repeat your Password', validators=[InputRequired()],
    #                         render_kw={"placeholder": "Repeat your password"})
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             validators=[InputRequired(), ],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")
