from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task') 
        if task:
            new_todo = Todo.objects.create(user=request.user, Todo_name=task)
            new_todo.save()

    if request.user.is_authenticated:
        all_todos = Todo.objects.filter(user=request.user)
        context = {
            'todos': all_todos
        }
        return render(request, 'todo.html', context)
    else:
        # Handle the case where the user is not authenticated
        return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']

        if len(password) < 3:
            messages.error(request, 'Password must contain at least 3 characters')
            return redirect('registers')  # Check if this should redirect to 'register' instead of 'registers'

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username.exists():
            messages.error(request, 'Error, username already exists!!!')
            return redirect('registers')  # Check if this should redirect to 'register' instead of 'registers'

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'User successfully created, login now!!!')
        return redirect('login')

    return render(request, 'register.html', {})



def login_page(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pword']

        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home')
        else:
            messages.error(request,'Error, user does not exists!!!')
            return redirect('login')

    return render(request,'login.html',{})

@login_required
def deletetask(request,name):
    get_todo=Todo.objects.get(user=request.user,Todo_name=name)
    get_todo.delete()
    return redirect('home')

@login_required
def updatetask(request,name):
     get_todo=Todo.objects.get(user=request.user,Todo_name=name)
     get_todo.status=True
     get_todo.save()
     return redirect('home')

def logouts(request):
    logout(request)
    return redirect('login')