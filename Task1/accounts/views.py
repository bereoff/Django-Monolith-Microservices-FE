
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy("new_post")


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
