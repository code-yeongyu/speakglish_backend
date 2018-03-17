from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def signup(request) :
    if request.method == "POST" :
        form = UserForm(request.POST)
        if form.is_valid() :
            try :
                str(getattr(User.objects.get(email=request.POST['email']), 'email'))
                return HttpResponse("이미 존재하는 이메일입니다.")
            except :
                new_user = User.objects.create_user(**form.cleaned_data)
                login(request, new_user)
                return redirect('/api/articles/')
        return HttpResponse("양식에 오류가 있습니다.")
    else :
        if request.user.is_authenticated :
            return HttpResponse("당신! 계정이 있잖아!")
        form = UserForm()
        return render(request, 'adduser.html', {'form':form})

def signin(request) :
    if request.method == "POST" :
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user != None :
            login(request, user)
            return redirect('api/articles/')
        else:
            return HttpResponse('로그인에 실패하였습니다.')
    else:
        if request.user.is_authenticated :
            return HttpResponse("당신! 로그인 되어 있잖아!")
        form = LoginForm()
        return render(request, 'login.html', {'form':form})