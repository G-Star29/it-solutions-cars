from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import SignUpUserForm

class SignUpView(CreateView):
    """CreateView для регистрации пользователей"""
    form_class = SignUpUserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('cars:index')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('cars:index')
        return super().dispatch(request, *args, **kwargs)