from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from models import Question


class QuestionForm(FlaskForm):
    question = StringField(
        'question', validators=[DataRequired()]
    )
    answer = StringField(
        'answer', validators=[DataRequired()]
    )
    category = IntegerField(
        'category', validators=[DataRequired()]
    )
    difficulty = IntegerField(
        'difficulty', validators=[DataRequired()]
    )
