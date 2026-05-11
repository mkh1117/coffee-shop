from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rePassword = request.POST['rePassword']

        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, 'این نام کاربری از قبل موجود است')
            return redirect('account:register')

        if password == rePassword:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.error(request, 'ثبت نام با موفقیت انجام شد')
            return redirect('main:home')
        else:
            messages.error(request, 'رمز های عبور مطابقت ندارند')
            return redirect('account:register')

    return redirect('main:home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()
        if user:
            if user.check_password(password):
                messages.error(request, 'شما با موفقیت وارد شدید')
            else:
                messages.error(request, 'رمز عبور نادرست است')
        else:
            messages.error(request, 'این نام کاربری وجود ندارد')
    return redirect('main:home')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.error(request, 'شما با موفقیت از حساب کاربری خود خارج شدید')
    return redirect('main:home')
