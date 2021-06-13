from flask_wtf import FlaskForm

from wtforms import SubmitField, TextAreaField


class DataForm(FlaskForm):
    data = TextAreaField('Enter your parameters')
    submit = SubmitField('Submit')
