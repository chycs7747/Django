from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

from common.models import Player
from django.views.decorators.csrf import csrf_exempt

def signup(request):
    if request.method == "POST":
        print("------------")
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            print("1111111111111")
            form.clean() #id 중복체크
            #username = form.cleaned_data.get('username')
            #password1 = form.cleaned_data.get('password1')
            #password2 = form.cleaned_data.get('password2')
            password1 = form.post_dict['password1']
            password2 = form.post_dict['password2']
            print(password1)
            if password1 == password2:
                Player(form.post_dict['name'],form.post_dict['password1'],form.post_dict['email'])
                Player.save()
                #login(request, user)  # 로그인
                print("여기까지 실행 안됨?\n\n\n\n\n\n\n\n")
                return redirect('index')
            #user = authenticate(username=username, password=raw_password)  # 사용자 인증
    else:
        print("qwewqewqewqewqewqewqewqeqweqwe")
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

'''
#기존의 signup 입니다.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
    '''
