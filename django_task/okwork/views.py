from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from .models import *
from .forms import *




def home(request):
    items = NavBar.objects.all()
    
    return render(request, 'home.html', {'menu_items': items})

def client(request):    
    items = NavBar.objects.all()
    user = request.user
    print(i := int(user.client.rating))
    stars = range(i)
    return render(request, 'client/profile.html', {'menu_items': items, 'user': user, 'stars': stars})


def client_edit(request):
    items = NavBar.objects.all()
    client = Client.objects.get(user=request.user)

    if request.method == 'POST':
        client_form = ClientForm(request.POST, request.FILES, instance=client)
        if client_form.is_valid():
            client_form.save()
            return redirect('client')
    else:
        client_form = ClientForm(instance=client)

    return render(request, 'client/edit.html', {'menu_items': items,'client_form': client_form})

def perfomancer_edit(request):
    items = NavBar.objects.all()
    performer = Performer.objects.get(user=request.user)

    if request.method == 'POST':
        performer_form = PerfomancerForm(request.POST, request.FILES, instance=performer)
        if performer_form.is_valid():
            performer_form.save()
            return redirect('performer')
    else:
        performer_form = PerfomancerForm(instance=performer)

    return render(request, 'performer/edit.html', {'menu_items': items, 'performer_form': performer_form})

def perfomancer(request):    
    items = NavBar.objects.all()
    return render(request, 'performer/profile.html', {'menu_items': items})


def login_view(request):
    items = NavBar.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу
        else:
            # Возвращение сообщения об ошибке
            return render(request, 'auth/login.html', {'error': 'Неверное имя пользователя или пароль'})
    else:
        return render(request, 'auth/login.html',  {'menu_items': items})


def registration(request):    
    items = NavBar.objects.all()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('home')
        else:
            print(user_form.error_messages)
    else:
        user_form = UserForm()
    
    context = {
        'menu_items': items,
        'user_form': user_form,
     }
    return render(request, 'auth/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')