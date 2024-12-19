from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request

from tasks.models import Task
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm


def index(request):

    tasks_list = {
        'tasks':Task.objects.all()
    }

    return render(request, 'tasks/index.html',tasks_list)

def add_task(request):

    addtask = Task(name=(request.POST.get('task')))
    addtask.save()

    return redirect('index')

def toggle_task(request, task_id):
    toggletask = (Task.objects.get(pk=task_id))
    toggletask.completed = True
    toggletask.save(update_fields=['completed'])

    return redirect('index')

def delete_task(request, task_id):
    deletetask = (Task.objects.get(pk=task_id))
    deletetask.delete()
    return redirect('index')





def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user.id)
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