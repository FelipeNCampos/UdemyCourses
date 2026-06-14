from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, TextAreaField
from wtforms.validators import NumberRange, Optional


class MovieForm(FlaskForm):
    rating = FloatField("Rating", validators=[Optional(), NumberRange(min=0, max=10)])
    ranking = IntegerField("Ranking", validators=[Optional(), NumberRange(min=1)])
    review = TextAreaField("Review", validators=[Optional()])
