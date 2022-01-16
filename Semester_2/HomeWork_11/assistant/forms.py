from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from assistant.models import User


class RegistrationForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), EqualTo('password')])
    password2 = PasswordField('repeat password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                'Please use other email. This one is currently used.')


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember_me = BooleanField(label='Remember Me')
    submit = SubmitField('Sign In')


class NoteForm(FlaskForm):
    note = TextAreaField('Say smth', validators=[
                         DataRequired(), Length(min=1, max=250)])
    submit = SubmitField('Submit')


class AssistantForm(FlaskForm):
    note = TextAreaField('Say smth', validators=[
                         DataRequired(), Length(min=1, max=250)])
    submit = SubmitField('Submit')
