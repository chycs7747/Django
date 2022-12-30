from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import Player


class LoginAuthentication(forms.Form):
    fields = ("username", "password1", "password2", "email")
    def clean(self):
        super().clean()
        try:
            player = Player.objects.get(pk='name')
        except:
            pass

class UserForm(LoginAuthentication):
    def __init__(self, post_dict=[]):
        super().__init__()
        self.post_dict = post_dict


'''ß
기존의 유저 form입니다.

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
'''