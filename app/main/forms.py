from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, Length


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell Us About Yourself...',validators = [Required()])
    submit = SubmitField('Submit')