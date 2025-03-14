from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

#class to create a form 
class NameForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

class getInfoTask(FlaskForm):
    title = StringField("Title of the task", validators=[DataRequired()])
    description = TextAreaField("Enter the description of the task", validators=[DataRequired()])
    submit = SubmitField("Submit")