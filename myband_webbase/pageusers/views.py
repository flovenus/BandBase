from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bands.forms import UserForm
from bands.models import MyUser

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list-bands')
        else:
            messages.success(request, ('There was an Error'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out successfully'))
    return redirect('list-bands')


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, ('Applied for Registration successfully!'))
            return redirect('list-bands')
    else:
        form = UserForm()
    return render(request, 'authenticate/register.html', {'form': form})


def user_list(request):
    User = get_user_model()
    users = User.objects.all()

    unchecked_users = MyUser.objects.all()

    return render(request, 'authenticate/userlist.html', {'users': users, 'unchecked_users': unchecked_users})


def verify_user(request, user_id):
    user = MyUser.objects.get(pk=user_id)
    username = user.username
    password = user.suggested_password
    mail = user.email
    V_user = User.objects.create_user(username=username, password=password, email=mail)
    user.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect(request.META.get('HTTP_REFERER'))