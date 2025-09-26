from http import HTTPMethod

from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from authentication.decorators.login import require_login
from authentication.forms import ChangePasswordForm


@require_login
def change_password_view(request: HttpRequest) -> HttpResponse:
    form = ChangePasswordForm(request.POST or None)
    form.user = request.user

    if request.method == HTTPMethod.POST and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.success(request, 'Thay đổi mật khẩu thành công.')
        return redirect('home')

    return render(request, 'auth/pages/change-password.html', {'form': form})
