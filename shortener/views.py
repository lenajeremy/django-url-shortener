from django.shortcuts import render, reverse
from django.contrib.auth.password_validation import validate_password, ValidationError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.hashers import PBKDF2PasswordHasher
import random

from .models import *

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'dashboard.html', context={'urls': request.user.urls.all()})


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email_address = request.POST['email_address']
        password = request.POST['password']
        password_confirmation = request.POST['conf_password']

        if password == password_confirmation:
            try:
                validate_password(password)
                hasher = PBKDF2PasswordHasher()
                password = hasher.encode(password, salt=hasher.salt())
                user = User.objects.create(username=username, last_name=lastname,
                                           first_name=firstname, email=email_address, password=password)
                login(request, user=user)
                return HttpResponseRedirect(reverse('dashboard'))
            except Exception as e:
                return render(request, 'register.html', context={'firstname': firstname, 'username': username, 'lastname': lastname, 'errors': e})
        else:
            return render(request, 'register.html', context={'firstname': firstname, 'username': username, 'lastname': lastname, 'email_address': email_address, 'errors': ['Passwords do not match']})
    return render(request, 'register.html', context={'firstname': '', 'username': '', 'lastname': '', 'password': '', 'conf_password': '', 'email_address': ''})


def login_user(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user=user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'login.html', context={'username': request.POST['username'], 'password': '', 'error': 'Invalid Credentials'})
    return render(request, 'login.html', context={'username': '', 'password': ''})


def new_url(request):
    if request.method == "POST":
        url = request.POST['url']
        text_to_remember = request.POST['url_alias']
        alias = generate_random_string(7)
        createdUrl = 'http://localhost:8000/' + alias
        Url.objects.create(redirectToUrl=url, creator=request.user,
                           text_to_remember=text_to_remember, alias=alias, createdUrl=createdUrl)
        return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'newurl.html')


def get_url(request, url_alias):
    try:
        url = Url.objects.get(alias=url_alias)
        return HttpResponseRedirect(url.redirectToUrl)
    except Url.DoesNotExist:
        return render(request, '404.html')


def generate_random_string(length):
    characters = ['abcdefghijklmopqrstuvwxyz0123456789-'[i]
                  for i in range(0, len('abcdefghijklmopqrstuvwxyz0123456789-'))]
    return_stuff = ''
    for i in range(0, length):
        return_stuff += characters[random.randint(0, len(characters)-1)]
    return return_stuff


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def delete_url(request, url_id):
    try:
        url = Url.objects.get(id=url_id)
        url.delete()
        return HttpResponseRedirect(reverse('dashboard'))
    except Url.DoesNotExist:
        return render(request, '404.html')
