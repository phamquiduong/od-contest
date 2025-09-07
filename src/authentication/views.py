from http import HTTPMethod

from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from authentication.decorators.login import require_login, require_not_login
from authentication.forms.change_password import PasswordChangeForm
from authentication.forms.login import LoginForm
from authentication.forms.register import RegisterForm


@require_not_login
def register_view(request: HttpRequest) -> HttpResponse:
    form = RegisterForm(request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.success(request, 'Hello. Chào mừng bạn đến với <strong>OD Contest</strong>.')
        return redirect('home')

    return render(request, 'auth/pages/register.html', {'form': form})


@require_not_login
def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        login(request=request, user=form.user)
        messages.success(request, '<strong>OD Contest</strong> rất vui khi gặp lại bạn.')
        return redirect('home')
    return render(request, 'auth/pages/login.html', {'form': form})


@require_login
def change_password_view(request: HttpRequest) -> HttpResponse:
    form = PasswordChangeForm(request.POST or None)
    form.user = request.user

    if request.method == HTTPMethod.POST and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.success(request, 'Thay đổi mật khẩu thành công.')
        return redirect('home')

    return render(request, 'auth/pages/change-password.html', {'form': form})
