from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Форма регистрации (GET/POST)
def register(request):
    """
    Обработка формы регистрации.
    GET - показывает форму регистрации
    POST - обрабатывает данные регистрации и создает пользователя
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматический вход после регистрации
            login(request, user)
            # Перенаправление в личный кабинет после успешной регистрации
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Личный кабинет после входа
@login_required
def profile(request):
    """
    Личный кабинет пользователя - показывается после входа
    """
    return render(request, 'users/profile.html')