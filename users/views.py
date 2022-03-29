from django.shortcuts import redirect
from django.views.generic import CreateView
import users.forms
from django.contrib.auth import login
from core.views import TitleMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


class UserLoginView(TitleMixin, LoginView):
    title = 'Вход'
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('core:home')


class UserLogoutView(LogoutView):
    next_page = 'core:home'


class UserRegisterView(TitleMixin, CreateView):
    title = 'Регистрация'
    form_class = users.forms.UserRegisterForm
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)
        return redirect('core:home')
