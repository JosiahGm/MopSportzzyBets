# ourapp/forms.py

rom flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from .util.validators import Unique
from .models import User

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(),
        Unique(
            User,
            User.email,
            message='There is already an account with that email.'])
    password = PasswordField('Password', validators=[DataRequired()])

<form action="" method="post">
    {{ form.email.label }}: {{ form.email(placeholder='yourname@email.com') }}
    <br>
    {{ form.password.label }}: {{ form.password }}
    <br>
    {{ form.csrf_token }}
</form>
