from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

from models import User
from flask import request

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class EditPostForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Post', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_title, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.original_title = original_title




class PostForm(FlaskForm):
    title= StringField('Write your title', validators=[
        DataRequired(), Length(min=1, max=30)])
    post = TextAreaField('Write your post', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class SearchForm(FlaskForm):
    q = StringField('Search', validators=[DataRequired()])

    #def __init__(self, *args, **kwargs):
   #    if 'formdata' not in kwargs:
    #        kwargs['formdata'] = request.args
    #    if 'csrf_enabled' not in kwargs:
    #        kwargs['csrf_enabled'] = False
    #    super(SearchForm, self).__init__(*args, **kwargs)

