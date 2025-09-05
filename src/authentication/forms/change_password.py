from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField()
    new_password = forms.CharField(min_length=6, max_length=16, validators=[validate_password])
    new_password_confirm = forms.CharField()

    user: User | None = None

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')

        if self.user and not self.user.check_password(old_password):
            raise forms.ValidationError('Mật khẩu cũ không đúng.')

        return old_password

    def clean_new_password(self):
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')

        if old_password and new_password and old_password == new_password:
            raise forms.ValidationError('Mật khẩu mới không được trùng với mật khẩu hiện tại.')

        return new_password

    def clean_new_password_confirm(self):
        new_password = self.cleaned_data.get('new_password')
        new_password_confirm = self.cleaned_data.get('new_password_confirm')

        if new_password and new_password_confirm and new_password != new_password_confirm:
            raise forms.ValidationError('Mật khẩu nhập lại không trùng khớp.')

        return new_password_confirm

    def save(self):
        new_password = self.cleaned_data['new_password']

        if self.user:
            self.user.set_password(new_password)
            self.user.save()

        return self.user
