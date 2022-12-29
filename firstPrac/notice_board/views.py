from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject
from .models import Board
from django.contrib.auth import authenticate as auth_authenticate, login as auth_login, logout as auth_logout


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth_authenticate(username, password)
    if user is not None:
        auth_login(request, user)
    return redirect('http://127.0.0.1:8000/notice_board/')


def index(request):
    subject_list = Subject.objects.order_by('-date')
    context = {'subject_list': subject_list}
    return render(request, 'notice_board/subject_list.html', context)

def subject_detail(request, subject_id):
    subject = Subject.objects.get(id = subject_id)
    context = {'subject': subject}
    return render(request, 'notice_board/subject_detail.html', context)