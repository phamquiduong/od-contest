from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=32, validators=[UnicodeUsernameValidator()])
    password = forms.CharField(min_length=6, max_length=16, validators=[validate_password])
    password_confirm = forms.CharField()

    def clean_username(self):
        username: str = self.cleaned_data['username']

        username = username.lower()

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Tên tài khoản này đã được sử dụng.')

        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data['password_confirm']

        if password and password != password_confirm:
            raise forms.ValidationError('Mật khẩu nhập lại không trùng khớp.')

        return password_confirm

    def save(self) -> User:
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        return user
