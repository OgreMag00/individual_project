from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def s(request):
    
    if request.method == 'POST':
        res = request.POST  #{'username': ['ewewewwe'], 'password': ['ewweew'], 'email': ['yegor_poatpov@bk.ru']}
        username = str(res.get('username'))
        password1 = str(res.get('password1'))
        password2 = str(res.get('password2'))
        
        
        if username is None:
            return HttpResponse("<h3>Введите имя пользователя</h3>")
        

        elif password1 is None or password2 is None:
            return render(request, 'auth_app/sign_in.html', {'error': 'Введите пароль'})
        
        elif password1 != password2:
            return render(request, 'auth_app/sign_in.html', {'error': 'Пароли должны совпадать'})
        
        elif User.objects.filter(username=username).first() != None:
            return render(request, 'auth_app/sign_in.html', {'error': 'Имя пользователь уже занято'})
        

        else:
            User.objects.create_user(username,'None@bk.ru', password1).save()
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('/')
            
    else:
        
        return render(request, 'auth_app/sign_in.html')

def l(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = authenticate(username=username, password=password)
            
            
            
            if User.objects.filter(username=username).first() == None:
                return render(request, 'auth_app/log_in.html', {'error':'Имя пользователя не найдено'})
            elif user == None:
                return render(request, 'auth_app/log_in.html', {'error':'Данного пользователя не сущестует'})
            else:
                login(request, user)    
                return redirect('/')
        except KeyError:
            return render(request, 'auth_app/log_in.html', {'error':'Заполните все поля'})

    else:
        return render(request, 'auth_app/log_in.html')
    
def log_out(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))