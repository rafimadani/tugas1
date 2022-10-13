from todolist.models import Task
from django.http import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todolist.forms import TaskCreationForm

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.models import User
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required


def show_json(request):
    username = request.COOKIES['username']
    user = User.objects.get(username=username)
    data_task = Task.objects.filter(user=user)
    context = {
        'data' : data_task,
        'username' : username,
        'user': user
    }
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")

@login_required(login_url='/todolist/login')
def show_todolist(request):
    username = request.COOKIES['username']
    user = User.objects.get(username=username)
    data_task = Task.objects.filter(user=user)
    context = {
        'data' : data_task,
        'username' : username,
        'user': user
    }
    return render(request, "todolist.html", context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('username', user.get_username()) # membuat cookie username dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login')
def create_task(request):
    form = TaskCreationForm()

    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit = False)
            todolist.user = request.user
            form.save()
            return redirect('todolist:show_todolist')
        
    context = {"forms": form}

    return render(request, 'create_task.html', context)

def create_task_json(request):
    form = TaskCreationForm()
    if request.method == "POST" and request.is_ajax():
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit = False)
            todolist.user = request.user
            form.save()
            return JsonResponse(b"CREATED", status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "todolist_json.html", {"form": form})






# Create your views here.
