from http import HTTPMethod

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from authentication.forms.register import RegisterForm


def register_view(request: HttpRequest) -> HttpResponse:
    form = RegisterForm(request.POST or None)

    if request.method == HTTPMethod.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'authentication/pages/register.html', {'form': form})
