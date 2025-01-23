from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.hashers import make_password
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def index(request):

    tasks_list = {
        'tasks':Task.objects.filter(user=request.user),
    }

    return render(request, 'tasks/index.html',tasks_list)

@login_required
def add_task(request):

    addtask = Task(name=(request.POST.get('task')), completed=False,user=request.user)
    addtask.save()

    return redirect('index')

def toggle_task(request, task_id):
    toggletask = (Task.objects.get(pk=task_id))
    toggletask.completed = True
    toggletask.save(update_fields=['completed'])

    return redirect('index')

@login_required
def profile(request, user_id):

    profiledata = User.objects.get(pk=user_id)
    countTask = Task.objects.filter(user=request.user).count()
    countTaskCompleted = Task.objects.filter(user=request.user, completed=1).count()
    profile_data = {
        'data':profiledata.username,
        'count':countTask,
        'countCompleted':countTaskCompleted
    }

    if user_id == request.user.id:
        return render(request,'tasks/profile.html', profile_data)
    else:
        return HttpResponse('ERROR')

@login_required
def change_password(request, user_id):
    # Получаем текущего пользователя
    user = request.user

    # Обрабатываем только POST-запросы
    if request.method == 'POST':
        new_password = request.POST.get('new-password')

        # Проверяем, что пароль введен
        if not new_password:
            messages.error(request, "Пароль не может быть пустым.")
            return redirect('profile',user_id=user.id)  # Возврат на страницу профиля

        # Обновляем пароль
        user.password = make_password(new_password)  # Хэшируем пароль
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Пароль успешно изменён.")
        return redirect('profile',user_id=user.id)  # Возврат на страницу профиля

    # Если запрос не POST, просто перенаправляем на профиль
    return redirect('profile',user_id=user.id)

def delete_task(request, task_id):
    deletetask = (Task.objects.get(pk=task_id))
    deletetask.delete()
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'tasks/register.html', {'form': form})





def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'tasks/login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'tasks/login.html')



