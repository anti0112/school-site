from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from users.forms import CustomUserCreationForm

@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(View):
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('http://localhost:8000/code/')  # Укажите свой URL для перенаправления после успешного входа
            else:
                messages.error(request, 'Неверные имя пользователя или пароль.')
        return render(request, self.template_name, {'form': form})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000/api/login/')


        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, 'Вы успешно вышли из системы.')
        return redirect('/login')  # Укажите свой URL для перенаправления после выхода
