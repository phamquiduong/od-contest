from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    user: User | None = None

    def clean_username(self):
        username = self.cleaned_data.get('username')

        self.user = User.objects.filter(username=username).first()

        if not self.user:
            raise forms.ValidationError('Người dùng này chưa có tài khoản.')

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if self.user and not self.user.check_password(raw_password=password):
            raise forms.ValidationError('Mật khẩu không đúng. Vui lòng kiểm tra lại.')

        return password
