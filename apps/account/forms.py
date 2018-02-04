from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
from django.forms import ModelForm

from apps.account.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'birthday', 'number']


class UserCreationForm(AuthUserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'birthday', 'number']
