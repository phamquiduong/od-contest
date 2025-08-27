from http import HTTPMethod

from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from authentication.forms.login import LoginForm
from authentication.forms.register import RegisterForm


def register_view(request: HttpRequest) -> HttpResponse:
    form = RegisterForm(request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        messages.success(request, "Đăng kí thành công")
        return redirect('home')

    return render(request, 'auth/pages/register.html', {'form': form})


def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        login(request=request, user=form.user)
        messages.success(request, "Đăng nhập thành công.")
        return redirect('home')
    return render(request, 'auth/pages/login.html', {'form': form})
