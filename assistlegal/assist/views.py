from django.shortcuts import render
from django.http import HttpResponse
from assist.models import register
from django.contrib.auth.forms import UserCreationForm
from .models import register
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'home.html')


def service(request):
    return render(request, 'service.html')


def contactus(request):
    return render(request, 'contactus.html')


def location(request):
    return render(request, 'location.html')


def registrationform(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if (User.objects.filter(username=user).exists()):
                return HttpResponse('User name already exist')
            if (User.objects.filter(email=email).exists()):
                return HttpResponse("Email already exist")
            else:
                model = User.objects.create_user(user, email, pass1)
                model.save()
                return render(request, 'home1.html')
        else:
            return HttpResponse('password mismatch')

    else:

        return render(request, 'registrationform.html')


def signin(request):
    if request.method == 'POST':

        user = request.POST['username']
        pass1 = request.POST['password1']
        print(user)
        print(pass1)
        us = authenticate(username=user, password=pass1)
        print(us)
        if us is not None:
            login(request, us)
            return render(request, 'home1.html')

        else:
            return HttpResponse('Password Mismatch')
    else:
        return render(request, 'signin.html')


def visit(request):
    visitors = register.objects.get(id=7)
    return render(request, 'get.html', {'v': visitors})


def all(request):
    value = register.objects.all()
    return render(request, 'all.html', {'v': value})


def filter(request):
    values = register.objects.filter(username='sharina')
    return render(request, 'filter.html', {'f': values})


def exclude(request):
    excludes = register.objects.exclude(username='sree')
    return render(request, 'exclude.html', {'e': excludes})


def order_by(request):
    order = register.objects.order_by("username")
    return render(request, 'order_by.html', {'o': order})


def create(request):
    cap = register.objects.create(username="Thulasi", email="thulasi@gmail.com", password1=1234, password2=1234)
    cap.save()
    cap1 = register.objects.all()
    return render(request, 'create.html', {'c': cap1})


def delete(request):
    boy = register.objects.filter(username='suveena').delete()
    boy = register.objects.all()
    return render(request, 'visitors.html', {'d': boy})


def update(request):
    girl = register.objects.filter(username='Jitha', email='jitha@gmail.com', password1=1234, password2=1234)
    girl.update(username='kamala', email='kamala@gmail.com', password1=1234, password2=1234)
    girl = register.objects.all()
    return render(request, 'update.html', {'u': girl})


def logout(request):
    return render(request, 'home.html')

# ORM-OBJECT RELATIONAL MAPPING-LAYER(CRUD-USING)

