from http import HTTPMethod

from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from authentication.decorators.login import require_not_login
from authentication.forms import RegisterForm


@require_not_login
def register_view(request: HttpRequest) -> HttpResponse:
    form = RegisterForm(request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.success(request, 'Hello. Chào mừng bạn đến với <strong>OD Contest</strong>.')
        return redirect('home')

    return render(request, 'auth/pages/register.html', {'form': form})
