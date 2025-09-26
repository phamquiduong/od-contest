from http import HTTPMethod

from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from authentication.decorators.login import require_not_login
from authentication.forms import LoginForm


@require_not_login
def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        login(request=request, user=form.user)
        messages.success(request, '<strong>OD Contest</strong> rất vui khi gặp lại bạn.')
        return redirect('home')
    return render(request, 'auth/pages/login.html', {'form': form})
