from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from email_validator import validate_email, EmailNotValidError


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])

    # Custom email validator using email_validator
    def validate_email(form, field):
        try:
            validate_email(field.data)
        except EmailNotValidError as e:
            raise ValueError(str(e))

    email = StringField('E-mail', validators=[InputRequired(), validate_email])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
    # submit = SubmitField('Send')
