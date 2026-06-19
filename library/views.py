from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            print("Пользователь вошел:")
            print("Username:", user.username)
            print("Email:", user.email)
            print("Is staff:", user.is_staff)
            print("Is superuser:", user.is_superuser)

            return redirect('/')

    return render(request, 'library/login.html')


def create_author(request):
    return HttpResponse("Главная страница")


def logout_view(request):
    logout(request)
    return redirect('/login/')